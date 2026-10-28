# Core building blocks

## Type and Profile

1. 0.FDO/Type:
    - Purpose: Defines the type of the current object.
    - Value: 
        - Always "0.FDO/Profile" for definitions, it tells the system: "This is a profile definition."
        - Not specified for FDOs

2. 0.FDO/Profile
    - Purpose: Defines what kind of profile this is.
    - Values:
        - 0.FDO/ProfileDef → a template for new profiles
        - 0.FDO/AttributeDef → a template for new attributes
        - 0.FDO/AttributeDefSyntax → for attributes with syntax rules (e.g., string, regex)
        - 0.FDO/AttributeDefProfileRef → for attributes that reference another profile
        - 0.FDO/AttributeDefAttrRef → for attributes that reference another attribute
        - 0.FDO/AttributeDefComb → for inline combinations
        - 0.FDO/AttributeDefUnion → for unions (e.g., "either A or B")


## Data, Name, Description 

1. 0.FDO/Data
    - Purpose: Where the value of the attribute is stored.
    - Value: 
        - Always "self" for definitions
        - Reference for FDOs (uses Attribute Referencing)

2. 0.FDO/Name
    - Purpose: The human-readable name of the attribute or profile.
    - Value: A string (e.g., "URL", "category")

3. 0.FDO/Description
    - Purpose: A human-readable explanation of the attribute.
    - Value: A string.

## For Validation

1. 0.FDO/Cardinality
    - Purpose: How many times this attribute can appear.
    - Values:
        - 0..1 → optional, one value
        - 1..1 → required, one value
        - 0..* → optional, zero or more
        - 1..* → required, one or more

2. 0.FDO/PrimitiveDataType
    - Purpose: The basic type of the value.
    - Values: "string", "number", "integer", "boolean"

3. 0.FDO/Regex
    - Purpose: A regular expression to validate the value.
    - Value: A string (e.g., ^https?://...)

4. 0.FDO/Whitelist
    - Purpose: A list of allowed values.
    - Value: A string (e.g., "CorporateBody")

5. 0.FDO/Blacklist
    - Purpose: A list of rejected values.
    - Value: A string (e.g., "admin")


## Profiles

1. 0.FDO/ProfileDef
    - Purpose: The template for creating new profiles.
    - Extends: 0.FDO/Root

2. 0.FDO/AttributeDef
    - Purpose: The base template for attributes.
    - Extends: 0.FDO/Root

3. 0.FDO/AttributeDefSyntax
    - Purpose: For attributes with syntax rules (e.g., string, regex).
    - Extends: 0.FDO/AttributeDef

4. 0.FDO/AttributeDefProfileRef
    - Purpose: For attributes that reference another profile.
    - Extends: 0.FDO/AttributeDef

5. 0.FDO/AttributeDefAttrRef
    - Purpose: For attributes that reference another attribute.
    - Extends: 0.FDO/AttributeDef

6. 0.FDO/AttributeDefComb
    - Purpose: For inline combinations (e.g., "either A or B").
    - Extends: 0.FDO/AttributeDef

7. 0.FDO/AttributeDefUnion
    - Purpose: For unions (e.g., "A or B").
    - Extends: 0.FDO/AttributeDef