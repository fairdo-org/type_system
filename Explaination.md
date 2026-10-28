# Core building blocks

The type system is build of 35 profiles.

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

3. 0.FDO/Root
    - Purpose: All Records must validate against this profile

## Data, Metadata, Name, Description 

1. 0.FDO/Data
    - Purpose: Where the value of the attribute is stored.
    - Value: 
        - Always "self" for definitions
        - Reference for FDOs (uses Attribute Referencing)

2. 0.FDO/Metadata
    - Purpose: Where is the metadata located, only used in FDO instantations
    - Value: inline or by reference

3. 0.FDO/Name
    - Purpose: The human-readable name of the attribute or profile.
    - Value: A string (e.g., "URL", "category")

4. 0.FDO/Description
    - Purpose: A human-readable explanation of the attribute.
    - Value: A string.

## Restriction on mata and metadata attributes

5. 0.FDO/DataAsAttrRef
    - Purpose: references a digital resource via an attribute reference (i.e., a PID pointing to another attribute)
    - value: A PID that resolves to an attribute definition (e.g., 0.FDO/AttributeDefURL, 0.FDO/AttributeDefFile)

6. 0.FDO/DataAsSelf
    - Purpose: Indicates that the identified resource is physical or conceptual
    - value: self

7. 0.FDO/MetadataAsAttrRef
    - Purpose: references a digital resource via an attribute reference (i.e., a PID pointing to another attribute)
    - value: A PID that resolves to an attribute definition (e.g., 0.FDO/AttributeDefURL, 0.FDO/AttributeDefFile)

8. 0.FDO/MetadataAsSelf
    - Purpose: Indicates that the identified resource is physical or conceptual
    - value: self

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

3. 0.FDO/NumericInterval
    - Purpose: To define a numeric interval
    - Values: form (a,b) (a,b] [a,b) or [a,b]

4. 0.FDO/Regex
    - Purpose: A regular expression to validate the value.
    - Value: A string (e.g., ^https?://...)

5. 0.FDO/Whitelist
    - Purpose: A list of allowed values.
    - Value: A string (e.g., "CorporateBody")

6. 0.FDO/Blacklist
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

## Helper Profiles to build attribute definitions
1. 0.FDO/AllowedAttributeInAttrRef
2. 0.FDO/AllowedAttributeInCombination
3. 0.FDO/AllowedAttributeInUnion
4. 0.FDO/AllowedPlainNameInAttrRef
5. 0.FDO/AllowedProfileInProfileRef
6. 0.FDO/ValidationStrategyForCombination


## Helper Profiles 
0.FDO/Extends
0.FDO/Attribute
0.FDO/BasicAttribute
0.FDO/RefinedAttribute
0.FDO/DenyAdditionalAttributes
