```mermaid
erDiagram
  OFDO-Type{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefAttrRef`
    OFDO-Data `self`
    OFDO-Name `FDO_type`
    OFDO-Description `The FDO type gives a hint to a machine how the identified 
resource may be processed. It points to the attribute 
that further specifies the FDO type. `
    OFDO-Cardinality `1..n`
}
  OFDO-Data{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefUnion`
    OFDO-Data `self`
    OFDO-Name `FDO_data`
    OFDO-Description `The OFDO-Data attribute is the entry point to find 
the data associated with an FDO. If the identified 
resource is physical or conceptual, the string "self" 
is used. If the resource it digital, OFDO-Data points 
to the Attribute that references the digital resource. 
`
    OFDO-Cardinality `1..n`
    OFDO-AllowedAttribute `OFDO-DataAsSelf`
    OFDO-AllowedAttribute `OFDO-DataAsAttrRef`
}
  OFDO-DataAsSelf{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_data_as_self`
    OFDO-Description `If identified resource is physical or conceptual, 
the string "self" is used as the value of OFDO-Data. 
`
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
    OFDO-Whitelist `self`
}
  OFDO-DataAsAttrRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefAttrRef`
    OFDO-Data `self`
    OFDO-Name `FDO_data_as_attr`
    OFDO-Description `If the identified resource it digital, OFDO-Data 
points to the attribute that references the digital 
resource. `
    OFDO-Cardinality `0..n`
}
  OFDO-Profile{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefProfileRef`
    OFDO-Data `self`
    OFDO-Name `FDO_profile`
    OFDO-Description `This attribute points to a FDO profile. The FDO profile 
is a template for any FDO record instantiating this 
profile. `
    OFDO-Cardinality `1..n`
    OFDO-AllowedProfile `OFDO-ProfileDef`
}
  OFDO-Name{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_resource_name`
    OFDO-Description `A localized human-readable name for the identified 
resource `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
}
  OFDO-Description{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_resource_description`
    OFDO-Description `A localized human-readable description for the 
identified resource `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
}
  OFDO-Cardinality{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_cardinality`
    OFDO-Description `Obligation and repeatability of the given attribute 
in an FDO record that uses this attribute. `
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
    OFDO-Regex `^(\d+)(\.\.(\d+|\*))?$`
}
  OFDO-PrimitiveDataType{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_primitive_data_type`
    OFDO-Description `A basic classification of which type of value an attribute 
is allowed to take on. `
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
    OFDO-Whitelist `string`
    OFDO-Whitelist `number`
    OFDO-Whitelist `integer`
    OFDO-Whitelist `boolean`
}
  OFDO-Regex{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_regular_expression`
    OFDO-Description `A string defining a regular expression`
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
}
  OFDO-NumericInterval{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_numeric_interval`
    OFDO-Description `A numeric interval of the form (a,b) (a,b] [a,b) or 
[a,b]. A square bracket means including the boundary, 
round bracket means excluding the boundary. a and 
b are decimal numbers. `
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
    OFDO-Regex `^\s*(?:\[\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\]|\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)|\[\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)|\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\])\s*$ 
`
}
  OFDO-Whitelist{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_whitelist`
    OFDO-Description `An exhaustive enumeration of values (strings) to 
accept. Other values are rejected. `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
}
  OFDO-Blacklist{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_blacklist`
    OFDO-Description `A non-exhaustive enumeration of values (strings) 
to reject. `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
}
  OFDO-AllowedAttributeInAttrRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefProfileRef`
    OFDO-Data `self`
    OFDO-Name `FDO_allowed_attribute_in_attr`
    OFDO-Description `An attribute definition PID that is allowed as the 
value of an attribute that uses attribute referencing. 
`
    OFDO-Cardinality `0..*`
    OFDO-AllowedProfileInProfileRef `OFDO-AttributeDef`
}
  OFDO-AllowedPlainNameInAttrRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_allowed_plain_name_in_attr_ref`
    OFDO-Description `A plain name that is allowed as the value of an attribute 
that uses attribute referencing. `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
}
  OFDO-AllowedProfileInProfileRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefProfileRef`
    OFDO-Data `self`
    OFDO-Name `FDO_allowed_profile_in_profile`
    OFDO-Description `PID of a profile that is allowed as the value of an attribute 
that uses profile referencing. `
    OFDO-Cardinality `0..*`
    OFDO-AllowedProfileInProfileRef `OFDO-ProfileDef`
}
  OFDO-AllowedAttributeInCombination{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefUnion`
    OFDO-Data `self`
    OFDO-Name `FDO_allowed_attribute_in_combination`
    OFDO-Description `An attribute that is part of an inline combination. 
The value is either a reference to an attribute, or 
a combination of an attribute and a localized cardinality. 
`
    OFDO-Cardinality `0..*`
    OFDO-AllowedAttributeInUnion `OFDO-BasicAttribute`
    OFDO-AllowedAttributeInUnion `OFDO-RefinedAttribute`
}
  OFDO-AllowedAttributeInUnion{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefUnion`
    OFDO-Data `self`
    OFDO-Name `FDO_allowed_attribute_in_union`
    OFDO-Description `An attribute that is part of a union. The value is either 
a reference to an attribute, or a combination of an 
attribute and a localized cardinality. `
    OFDO-Cardinality `0..*`
    OFDO-AllowedAttributeInUnion `OFDO-RefinedAttribute`
    OFDO-AllowedAttributeInUnion `OFDO-BasicAttribute`
}
  OFDO-BasicAttribute{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefProfileRef`
    OFDO-Data `self`
    OFDO-Name `FDO_basic_attribute`
    OFDO-Description `A reference (PID) to an FDO attribute. Used in profiles, 
unions and inline combinations to specify which 
attributes must be in FDOs. `
    OFDO-Cardinality `0..*`
    OFDO-AllowedProfileInProfileRef `OFDO-AttributeDef`
}
  OFDO-RefinedAttribute{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefComb`
    OFDO-Data `self`
    OFDO-Name `FDO_refined_attribute`
    OFDO-Description `An attribute that is refined in a new context. The 
value is a combination of an attribute and a localized 
cardinality adapted to the new context. `
    OFDO-Cardinality `0..*`
    OFDO-Attribute `OFDO-Cardinality`
    OFDO-Attribute `OFDO-BasicAttribute`
}
  OFDO-DenyAdditionalAttributes{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_prohibition_of_additional_ attributes `
    OFDO-Description `If this attribute is not set or has a false value, additional 
attributes are allowed (recommended value) `
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `boolean`
}
  OFDO-Extends{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefProfileRef`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_extends_profile`
    OFDO-Description `Reference to another profile that is extended by 
this profile. `
    OFDO-Cardinality `0..*`
    OFDO-PrimitiveDataType `string`
    OFDO-AllowedProfileInProfileRef `OFDO-ProfileDef`
}
  OFDO-Attribute{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefUnion`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute`
    OFDO-Description `The attributes that are required by this profile. 
One can either use an attribute as it is, or refine 
it to adapt it to the given context by providing a localized 
cardinality. `
    OFDO-Cardinality `0..*`
    OFDO-AllowedAttributeInUnion `OFDO-RefinedAttribute`
    OFDO-AllowedAttributeInUnion `OFDO-BasicAttribute`
}
  OFDO-Root{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_root_profile`
    OFDO-Description `This FDO defines the root profile. Any FDO must be 
valid against the root profile. The root profile 
requires three attributes: OFDO-Type, OFDO-Profile, 
OFDO-Data.These three attributes must be used in 
any FDO. The root profile can and should be extended 
by other profiles. `
    OFDO-Attribute `OFDO-Type`
    OFDO-Attribute `OFDO-Data`
    OFDO-Attribute `OFDO-Profile`
}
  OFDO-ProfileDef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_profile_definition`
    OFDO-Description `This FDO defines the profile definition profile. 
It is the profile that validates any other profile, 
including itself. It is the template for defining 
new FDO profiles. Any FDO profile must be valid against 
this profile. `
    OFDO-Attribute `OFDO-Description`
    OFDO-Attribute `OFDO-Name`
    OFDO-Attribute `OFDO-DenyAdditionalAttributes`
    OFDO-Attribute `OFDO-Extends`
    OFDO-Attribute `OFDO-Attribute`
    OFDO-Extends `OFDO-Root`
}
  OFDO-AttributeDefSyntax{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile_`
    OFDO-Description `This profile is the template to define new basic attributes 
(i.e., attributes that are based on syntactically 
validatable expressions). `
    OFDO-Extends `OFDO-AttributeDef`
    OFDO-Attribute `OFDO-Regex`
    OFDO-Attribute `OFDO-NumericInterval`
    OFDO-Attribute `OFDO-Whitelist`
    OFDO-Attribute `OFDO-Blacklist`
    OFDO-Attribute `OFDO-PrimitiveDataType`
}
  OFDO-AttributeDefProfileRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile_for_profile_referencing 
`
    OFDO-Description `This profile is the template to define a new attribute 
that uses the profile referencing mechanism.  `
    OFDO-Attribute `OFDO-AllowedProfilesInProfileRef`
    OFDO-Extends `OFDO-AttributeDef`
}
  OFDO-AttributeDefAttrRef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile_`
    OFDO-Description `This profile is the template to define a new attribute 
that uses the attribute referencing mechanism.  
`
    OFDO-Extends `OFDO-AttributeDef`
    OFDO-Attribute `OFDO-AllowedAttributesInAttrRef`
    OFDO-Attribute `OFDO-AllowedPlainNamesInAttrRef`
}
  OFDO-AttributeDefComb{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile_for_inline_combination 
`
    OFDO-Description `This profile is the template to define a new attribute 
that is an inline combination of existing attributes.  
`
    OFDO-Attribute `OFDO-AllowedAttributeIn`
    OFDO-Extends `OFDO-AttributeDef`
}
  OFDO-AttributeDefUnion{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile_for_union 
`
    OFDO-Description `This profile is the template to define a new attribute 
that is a union of existing attributes.  `
    OFDO-Extends `OFDO-AttributeDef`
    OFDO-Attribute `OFDO-AllowedAttributeInUnion`
}
  OFDO-AttributeDef{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-ProfileDef`
    OFDO-Data `self`
    OFDO-Name `FDO_attribute_definition_profile`
    OFDO-Description `This FDO profile is the base template to define new 
attributes. It is extended by five different templates:  
OFDO-AttributeDefSyntax, OFDO-AttributeDefComb, 
OFDO-AttributeDefUnion, OFDO-AttributeDefProfileRef, 
and OFDO-AttributeDefAttrRef. Each of those templates 
can be instantiated to define new attributes based 
on certain validation rules. An attribute that only 
instantiates OFDO-AttributeDef (and none of the 
extending templates) is validated to be a string. 
`
    OFDO-Extends `OFDO-Root`
    OFDO-Attribute `OFDO-Name`
    OFDO-Attribute `OFDO-Description`
    OFDO-Attribute `OFDO-Cardinality`
    OFDO-Attribute `OFDO-ValidationStrategyForCombination`
}
  OFDO-ValidationStrategyForCombination{    OFDO-Type `OFDO-Profile`
    OFDO-Profile `OFDO-AttributeDefSyntax`
    OFDO-Data `self`
    OFDO-Name `FDO_validation_strategy_for_combination`
    OFDO-Description `An attribute can use several validation mechanisms 
simultaneously. Which validation mechanism applies 
depends on the profile(s) used by the attribute definition: 
OFDO-AttributeDefSyntax, OFDO-AttributeDefComb, 
OFDO-AttributeDefUnion, OFDO-AttributeDefProfileRef, 
and OFDO-AttributeDefAttrRef. If several of these 
profiles are used by one attribute definition, OFDO-ValidationStrategyForCombination 
determines whether at least one validation mechanism 
must apply (anyof), or all of them (allof). The default 
is allof, in which case the attribute can be omitted. 
`
    OFDO-Cardinality `0..1`
    OFDO-PrimitiveDataType `string`
    OFDO-Whitelist `anyof`
    OFDO-Whitelist `allof`
}
OFDO-PrimitiveDataType ||--|| OFDO-Description : requires 
OFDO-NumericInterval ||--|| OFDO-Name : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Type : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Cardinality : requires 
OFDO-Regex ||--|| OFDO-Description : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Description : requires 
OFDO-RefinedAttribute ||--|| OFDO-Data : requires 
OFDO-Attribute ||--|| OFDO-Data : requires 
OFDO-Attribute ||--|| OFDO-Profile : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Description : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Description : requires 
OFDO-ProfileDef ||--|| OFDO-Extends : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Data : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Description : requires 
OFDO-BasicAttribute ||--|| OFDO-AllowedProfileInProfileRef : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Description : requires 
OFDO-Name ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Name : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Name : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Type : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-AllowedProfileInProfileRef : requires 
OFDO-AttributeDefComb ||--|| OFDO-Description : requires 
OFDO-BasicAttribute ||--|| OFDO-Description : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Cardinality : requires 
OFDO-DataAsSelf ||--|| OFDO-Data : requires 
OFDO-NumericInterval ||--|| OFDO-PrimitiveDataType : requires 
OFDO-Type ||--|| OFDO-Type : requires 
OFDO-RefinedAttribute ||--|| OFDO-Type : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Data : requires 
OFDO-RefinedAttribute ||--|| OFDO-Cardinality : requires 
OFDO-Extends ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AttributeDefComb ||--|| OFDO-Profile : requires 
OFDO-Profile ||--|| OFDO-Data : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Profile : requires 
OFDO-Blacklist ||--|| OFDO-Type : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Cardinality : requires 
OFDO-Attribute ||--|| OFDO-AllowedAttributeInUnion : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Whitelist : requires 
OFDO-Cardinality ||--|| OFDO-Cardinality : requires 
OFDO-ProfileDef ||--|| OFDO-Name : requires 
OFDO-Data ||--|| OFDO-Name : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Profile : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Profile : requires 
OFDO-AttributeDefComb ||--|| OFDO-Extends : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Name : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Extends : requires 
OFDO-DataAsSelf ||--|| OFDO-PrimitiveDataType : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Profile : requires 
OFDO-Extends ||--|| OFDO-Cardinality : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Type : requires 
OFDO-PrimitiveDataType ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-AllowedAttributeInUnion : requires 
OFDO-Root ||--|| OFDO-Data : requires 
OFDO-DataAsSelf ||--|| OFDO-Description : requires 
OFDO-Extends ||--|| OFDO-Name : requires 
OFDO-DataAsSelf ||--|| OFDO-Whitelist : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Profile : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Cardinality : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Name : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Type : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Name : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Name : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Data : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Cardinality : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Data : requires 
OFDO-Type ||--|| OFDO-Description : requires 
OFDO-Cardinality ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Data : requires 
OFDO-AttributeDefComb ||--|| OFDO-Data : requires 
OFDO-AttributeDefComb ||--|| OFDO-Attribute : requires 
OFDO-RefinedAttribute ||--|| OFDO-Description : requires 
OFDO-AttributeDef ||--|| OFDO-Type : requires 
OFDO-AttributeDef ||--|| OFDO-Data : requires 
OFDO-Blacklist ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Name : requires 
OFDO-Description ||--|| OFDO-Type : requires 
OFDO-Profile ||--|| OFDO-Profile : requires 
OFDO-Description ||--|| OFDO-Cardinality : requires 
OFDO-NumericInterval ||--|| OFDO-Cardinality : requires 
OFDO-Root ||--|| OFDO-Profile : requires 
OFDO-NumericInterval ||--|| OFDO-Description : requires 
OFDO-DataAsSelf ||--|| OFDO-Type : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Data : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Attribute : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Name : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Name : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Profile : requires 
OFDO-Whitelist ||--|| OFDO-Description : requires 
OFDO-Root ||--|| OFDO-Name : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Type : requires 
OFDO-Whitelist ||--|| OFDO-Type : requires 
OFDO-RefinedAttribute ||--|| OFDO-Name : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Description : requires 
OFDO-Attribute ||--|| OFDO-Type : requires 
OFDO-Description ||--|| OFDO-Description : requires 
OFDO-Extends ||--|| OFDO-AllowedProfileInProfileRef : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Extends : requires 
OFDO-Extends ||--|| OFDO-Description : requires 
OFDO-Extends ||--|| OFDO-Profile : requires 
OFDO-ProfileDef ||--|| OFDO-Description : requires 
OFDO-Blacklist ||--|| OFDO-Cardinality : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Description : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Type : requires 
OFDO-NumericInterval ||--|| OFDO-Data : requires 
OFDO-AttributeDefComb ||--|| OFDO-Name : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Description : requires 
OFDO-Regex ||--|| OFDO-Profile : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Cardinality : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Name : requires 
OFDO-AttributeDef ||--|| OFDO-Description : requires 
OFDO-Data ||--|| OFDO-Profile : requires 
OFDO-Data ||--|| OFDO-AllowedAttribute : requires 
OFDO-Whitelist ||--|| OFDO-Name : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Type : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Description : requires 
OFDO-ProfileDef ||--|| OFDO-Profile : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Extends : requires 
OFDO-Blacklist ||--|| OFDO-Data : requires 
OFDO-Cardinality ||--|| OFDO-Regex : requires 
OFDO-ProfileDef ||--|| OFDO-Data : requires 
OFDO-Name ||--|| OFDO-Cardinality : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Description : requires 
OFDO-Blacklist ||--|| OFDO-Description : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Profile : requires 
OFDO-Profile ||--|| OFDO-Type : requires 
OFDO-Regex ||--|| OFDO-Data : requires 
OFDO-Whitelist ||--|| OFDO-Data : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-Data : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Type : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Name : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Data : requires 
OFDO-AttributeDef ||--|| OFDO-Name : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-PrimitiveDataType : requires 
OFDO-AttributeDef ||--|| OFDO-Extends : requires 
OFDO-NumericInterval ||--|| OFDO-Regex : requires 
OFDO-Attribute ||--|| OFDO-Description : requires 
OFDO-AllowedProfileInProfileRef ||--|| OFDO-AllowedProfileInProfileRef : requires 
OFDO-Description ||--|| OFDO-PrimitiveDataType : requires 
OFDO-Type ||--|| OFDO-Name : requires 
OFDO-Type ||--|| OFDO-Cardinality : requires 
OFDO-DataAsSelf ||--|| OFDO-Cardinality : requires 
OFDO-Name ||--|| OFDO-Description : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Profile : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Name : requires 
OFDO-Regex ||--|| OFDO-Cardinality : requires 
OFDO-Profile ||--|| OFDO-Name : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Profile : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Cardinality : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Type : requires 
OFDO-Name ||--|| OFDO-Name : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Profile : requires 
OFDO-Type ||--|| OFDO-Data : requires 
OFDO-DataAsSelf ||--|| OFDO-Name : requires 
OFDO-RefinedAttribute ||--|| OFDO-Attribute : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Data : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Extends : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Attribute : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Data : requires 
OFDO-AllowedAttributeInUnion ||--|| OFDO-Type : requires 
OFDO-AttributeDef ||--|| OFDO-Profile : requires 
OFDO-Whitelist ||--|| OFDO-Profile : requires 
OFDO-Extends ||--|| OFDO-Data : requires 
OFDO-Type ||--|| OFDO-Profile : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Attribute : requires 
OFDO-DataAsSelf ||--|| OFDO-Profile : requires 
OFDO-Blacklist ||--|| OFDO-Name : requires 
OFDO-NumericInterval ||--|| OFDO-Profile : requires 
OFDO-Root ||--|| OFDO-Type : requires 
OFDO-BasicAttribute ||--|| OFDO-Data : requires 
OFDO-AttributeDefComb ||--|| OFDO-Type : requires 
OFDO-BasicAttribute ||--|| OFDO-Type : requires 
OFDO-Regex ||--|| OFDO-PrimitiveDataType : requires 
OFDO-Name ||--|| OFDO-Data : requires 
OFDO-Data ||--|| OFDO-Type : requires 
OFDO-BasicAttribute ||--|| OFDO-Cardinality : requires 
OFDO-Profile ||--|| OFDO-Cardinality : requires 
OFDO-Cardinality ||--|| OFDO-Type : requires 
OFDO-BasicAttribute ||--|| OFDO-Profile : requires 
OFDO-AttributeDefUnion ||--|| OFDO-Type : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Profile : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Cardinality : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Data : requires 
OFDO-Data ||--|| OFDO-Data : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Cardinality : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-Description : requires 
OFDO-Attribute ||--|| OFDO-Cardinality : requires 
OFDO-Data ||--|| OFDO-Cardinality : requires 
OFDO-PrimitiveDataType ||--|| OFDO-Type : requires 
OFDO-NumericInterval ||--|| OFDO-Type : requires 
OFDO-Whitelist ||--|| OFDO-Cardinality : requires 
OFDO-Blacklist ||--|| OFDO-Profile : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Data : requires 
OFDO-Name ||--|| OFDO-Type : requires 
OFDO-Cardinality ||--|| OFDO-Data : requires 
OFDO-Cardinality ||--|| OFDO-Description : requires 
OFDO-DenyAdditionalAttributes ||--|| OFDO-PrimitiveDataType : requires 
OFDO-Root ||--|| OFDO-Attribute : requires 
OFDO-Root ||--|| OFDO-Description : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-Profile : requires 
OFDO-AllowedAttributeInAttrRef ||--|| OFDO-Data : requires 
OFDO-AllowedAttributeInCombination ||--|| OFDO-AllowedAttributeInUnion : requires 
OFDO-Extends ||--|| OFDO-Type : requires 
OFDO-Description ||--|| OFDO-Data : requires 
OFDO-Whitelist ||--|| OFDO-PrimitiveDataType : requires 
OFDO-ProfileDef ||--|| OFDO-Attribute : requires 
OFDO-Profile ||--|| OFDO-Description : requires 
OFDO-Name ||--|| OFDO-Profile : requires 
OFDO-Regex ||--|| OFDO-Name : requires 
OFDO-AttributeDefSyntax ||--|| OFDO-Attribute : requires 
OFDO-AttributeDefProfileRef ||--|| OFDO-Profile : requires 
OFDO-Cardinality ||--|| OFDO-Name : requires 
OFDO-ProfileDef ||--|| OFDO-Type : requires 
OFDO-ValidationStrategyForCombination ||--|| OFDO-Whitelist : requires 
OFDO-Regex ||--|| OFDO-Type : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-PrimitiveDataType : requires 
OFDO-Data ||--|| OFDO-Description : requires 
OFDO-BasicAttribute ||--|| OFDO-Name : requires 
OFDO-Description ||--|| OFDO-Profile : requires 
OFDO-Description ||--|| OFDO-Name : requires 
OFDO-Attribute ||--|| OFDO-Name : requires 
OFDO-AttributeDefAttrRef ||--|| OFDO-Description : requires 
OFDO-AttributeDef ||--|| OFDO-Attribute : requires 
OFDO-RefinedAttribute ||--|| OFDO-Profile : requires 
OFDO-DataAsAttrRef ||--|| OFDO-Type : requires 
OFDO-Profile ||--|| OFDO-AllowedProfile : requires 
OFDO-Cardinality ||--|| OFDO-Profile : requires 
OFDO-AllowedPlainNameInAttrRef ||--|| OFDO-Name : requires 
```