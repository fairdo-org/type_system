#!/usr/bin/env python3
"""
handle_validator.py

Validate a handle record of instance against the profile it references.

Features
--------
* Resolves handles via the public Handle REST API (GET /api/handles/<handle>)
* Retrieves profile objects and attribute-definition objects.
* Checks:
    - profile reference exists
    - every attribute listed in the profile has a definition
    - cardinality (min..max) is respected
    - primitive data type matches the stored value
    - whitelist constraints (if any) are honoured
* Can be used as a library or as a CLI tool.

Requirements
------------
pip install requests tqdm
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from typing import Any, Dict, List, Tuple

import requests
from tqdm import tqdm

# ----------------------------------------------------------------------
# Configuration – change only if your handle service lives at a different URL
# ----------------------------------------------------------------------
BASE_URL = "http://hdl.handle.net/api/handles"   
TIMEOUT = 30  # seconds for each HTTP request


# ----------------------------------------------------------------------
# Helper functions for the Handle API
# ----------------------------------------------------------------------
def resolve_handle(handle: str) -> Dict[str, Any]:
    """
    Resolve a handle and return the JSON payload.
    Raises RuntimeError if the handle cannot be resolved.
    """
    url = f"{BASE_URL}/{handle}"
    try:
        resp = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error while resolving {handle!r}: {exc}")

    if resp.status_code == 404:
        raise RuntimeError(f"Handle {handle!r} not found (404).")
    if resp.status_code != 200:
        raise RuntimeError(
            f"Unexpected HTTP {resp.status_code} while resolving {handle!r}: {resp.text}"
        )

    data = resp.json()
    if data.get("responseCode") != 1:
        # 100 = not found, other codes may indicate other problems
        raise RuntimeError(
            f"Handle {handle!r} could not be resolved – responseCode={data.get('responseCode')}, message={data.get('response_message')}"
        )
    return data


def get_value_by_type(values: List[Dict[str, Any]], typ: str) -> Any:
    """
    Return the first value dict whose 'type' matches *typ*.
    If not found, returns None.
    """
    for v in values:
        #print(typ + '############'+v.get("type"))
        if v.get("type") == typ:
            return v
    return None


# ----------------------------------------------------------------------
# Profile & attribute‑definition parsing
# ----------------------------------------------------------------------
def parse_cardinality(card: str) -> Tuple[int, int]:
    """
    Convert a cardinality string like "0..1", "1..1", "2..*" into (min, max).
    '*' is interpreted as sys.maxsize.
    """
    if ".." not in card:
        raise ValueError(f"Invalid cardinality format: {card!r}")

    lo, hi = card.split("..")
    lo_i = int(lo)
    hi_i = sys.maxsize if hi == "*" else int(hi)
    return lo_i, hi_i


def extract_whitelist(values: List[Dict[str, Any]]) -> List[str]:
    """
    In an attribute‑definition object, every entry with type
    ".../Whitelist" holds a single allowed value.
    Return the list of those values (as strings).
    """
    whitelist = []
    for v in values:
        if v.get("type", "").endswith("/Whitelist"):
            # The actual value is stored under v["data"]["value"]
            val = v.get("data", {}).get("value")
            if val is not None:
                whitelist.append(str(val))
    return whitelist


def load_attribute_definition(attr_pid: str) -> Dict[str, Any]:
    """
    Resolve an attribute-definition PID and return a dict with the
    information we need for validation.
    """
    data = resolve_handle(attr_pid)
    vals = data.get("values", [])
    
    # Basic fields
    name = get_value_by_type(vals, "21.T11970/Name")
    description = get_value_by_type(vals, "21.T11970/Description")
    cardinality = get_value_by_type(vals, "21.T11970/Cardinality")
    primitive = get_value_by_type(vals, "21.T11970/PrimitiveDataType")
    whitelist = extract_whitelist(vals)
    # Build a clean dict
    result = {
        "pid": attr_pid,
        "name": name["data"]["value"] if name else None,
        "description": description["data"]["value"] if description else None,
        "cardinality": cardinality["data"]["value"] if cardinality else "1..1",
        "primitive": primitive["data"]["value"] if primitive else "string",
        "whitelist": whitelist,
    }
    return result


def load_profile(profile_pid: str) -> Dict[str, Any]:
    """
    Resolve a profile PID and return:
        {
            "pid": "...",
            "attributes": [list of attribute‑definition PIDs],
            "name": "...",
            "description": "..."
        }
    """
    data = resolve_handle(profile_pid)
    vals = data.get("values", [])

    # Name / description are optional but nice for reporting
    name = get_value_by_type(vals, "21.T11970/Name")
    print('---------------',profile_pid)
    description = get_value_by_type(vals, "21.T11970/Description")

    # All entries with type ".../Attribute" hold a reference to an attribute definition
    attr_pids = []
    for v in vals:
        if v.get("type", "").endswith("/Attribute"):
            attr_pids.append(v["data"]["value"])

    return {
        "pid": profile_pid,
        "name": name["data"]["value"] if name else None,
        "description": description["data"]["value"] if description else None,
        "attributes": attr_pids,
    }


# ----------------------------------------------------------------------
# Instance validation
# ----------------------------------------------------------------------
def validate_instance(instance_handle: str, ignore_type: bool = True) -> Tuple[bool, List[str], Dict[str, Any]]:
    """
    Validate a handle instance against its profile.

    Returns (is_valid, list_of_error_messages, detailed_report_dict)
    """
    errors: List[str] = []
    report: Dict[str, Any] = {"instance": instance_handle, "checks": {}}

    # ------------------------------------------------------------------
    # 1 Resolve the instance itself
    # ------------------------------------------------------------------
    try:
        instance = resolve_handle(instance_handle)
    except RuntimeError as exc:
        return False, [str(exc)], report

    instance_vals = instance.get("values", [])

    # ------------------------------------------------------------------
    # 2 Find the profile PID 
    # ------------------------------------------------------------------
    profile_entry = None
    for v in instance_vals:
        if v.get("type", "").endswith("/Profile"):
            profile_entry = v
            break

    if not profile_entry:
        errors.append("Instance does not contain a '/Profile' entry.")
        return False, errors, report

    profile_pid = profile_entry["data"]["value"]
    report["profile_pid"] = profile_pid

    # ------------------------------------------------------------------
    # 3 Load the profile and its attribute definitions
    # ------------------------------------------------------------------
    try:
        profile = load_profile(profile_pid)
    except RuntimeError as exc:
        errors.append(f"Could not load profile {profile_pid!r}: {exc}")
        return False, errors, report

    report["profile"] = {
        "name": profile["name"],
        "description": profile["description"],
        "attributes": profile["attributes"],
    }

    # Resolve all attribute definitions once (cached)
    attr_defs: Dict[str, Dict[str, Any]] = {}
    for attr_pid in tqdm(
        profile["attributes"], desc="Loading attribute definitions", unit="attr"
    ):
        try:
            attr_defs[attr_pid] = load_attribute_definition(attr_pid)
        except RuntimeError as exc:
            errors.append(f"Failed to load attribute definition {attr_pid!r}: {exc}")

    if errors:
        # If any attribute definition could not be loaded we cannot continue reliably.
        return False, errors, report

    # ------------------------------------------------------------------
    # 4 Build a map of instance values keyed by attribute‑definition PID
    # ------------------------------------------------------------------
    instance_by_attr: Dict[str, List[Any]] = defaultdict(list)
    for v in instance_vals:
        typ = v.get("type")
        if typ in attr_defs:  # only keep entries that correspond to a known attribute
            instance_by_attr[typ].append(v["data"]["value"])

    # ------------------------------------------------------------------
    # 5 Validate each attribute definition against the instance values
    # ------------------------------------------------------------------
    for attr_pid, definition in attr_defs.items():
        values = instance_by_attr.get(attr_pid, [])
        min_card, max_card = parse_cardinality(definition["cardinality"])

        # Cardinality check
        if not (min_card <= len(values) <= max_card):
            errors.append(
                f"Attribute '{definition['name'] or attr_pid}' (PID {attr_pid}) "
                f"has {len(values)} value(s) but cardinality is {definition['cardinality']}."
            )
            continue  # further checks are meaningless if cardinality already fails

        # Primitive type & whitelist checks (only if a value is present)
        for val in values:
            # Primitive type validation
            primitive = definition["primitive"].lower()
            if primitive == "integer":
                if not re.fullmatch(r"-?\d+", str(val)):
                    errors.append(
                        f"Attribute '{definition['name']}' expects integer, got {val!r}."
                    )
            elif primitive == "float" or primitive == "double":
                try:
                    float(val)
                except ValueError:
                    errors.append(
                        f"Attribute '{definition['name']}' expects floating‑point, got {val!r}."
                    )
            elif primitive == "string":
                # everything is a string already – no check needed
                pass
            else:
                # Unknown primitive – just warn
                errors.append(
                    f"Attribute '{definition['name']}' has unknown primitive type '{primitive}'."
                )

            # Whitelist validation
            if definition["whitelist"]:
                if str(val) not in definition["whitelist"]:
                    errors.append(
                        f"Attribute '{definition['name']}' value {val!r} not in whitelist {definition['whitelist']}."
                    )

        # Record the successful check for reporting
        report["checks"][attr_pid] = {
            "name": definition["name"],
            "found_values": values,
            "cardinality_ok": True,
            "primitive_ok": True,
            "whitelist_ok": True,
        }

    # ------------------------------------------------------------------
    # 6 Detect stray attributes (values that are not listed in the profile)
    # ------------------------------------------------------------------
    stray_attrs = [
        typ for typ in instance_by_attr.keys() if typ not in attr_defs
    ]
    if stray_attrs:
        errors.append(
            f"The instance contains attribute entries that are not part of the profile: {stray_attrs}"
        )

    # ------------------------------------------------------------------
    # 7 Final result
    # ------------------------------------------------------------------
    is_valid = len(errors) == 0
    return is_valid, errors, report


# ----------------------------------------------------------------------
# CLI entry point
# ----------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a handle record against its profile definition."
    )
    parser.add_argument(
        "handle",
        help="Handle to validate, e.g. 21.T11970/car1",
    )
    parser.add_argument(
        "--ignore-type",
        action="store_true",
        default=True,
        help="Ignore the 'type' field (default: true).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full validation report as JSON (instead of a short human‑readable summary).",
    )
    args = parser.parse_args()

    print(f"🔎 Resolving and validating handle {args.handle!r} …")
    valid, errs, rpt = validate_instance(args.handle, ignore_type=args.ignore_type)

    if args.json:
        # Dump the whole report (including the error list) as JSON
        output = {"valid": valid, "errors": errs, "report": rpt}
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        # Human‑readable summary
        if valid:
            print("Validation succeeded – the instance conforms to its profile.")
        else:
            print("Validation failed with the following problems:")
            for e in errs:
                print(f"   • {e}")

        # Optional: show a tiny summary of what was checked
        print("\n--- Summary ---")
        print(f"Profile PID          : {rpt.get('profile_pid')}")
        print(f"Profile name         : {rpt.get('profile', {}).get('name')}")
        print(f"Number of attributes : {len(rpt.get('profile', {}).get('attributes', []))}")

        if not valid:
            print("\n(Use --json for the full machine‑readable report.)")


if __name__ == "__main__":
    main()

