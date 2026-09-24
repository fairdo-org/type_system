```mermaid
erDiagram
  O.FDO-Type{    O.FDO-Type `O.FDO-Profile`
    O.FDO-Profile `O.FDO-AttributeDefAttrRef`
    O.FDO-Data `self`
    O.FDO-Name `FDO_type `
    O.FDO-Description `The FDO type gives a hint to a machine how the identified 
resource may be processed. It points to the attribute 
that further specifies the FDO type.  `
    O.FDO-Cardinality `1..n`
}
  O.FDO-Data{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefUnion `
    O.FDO-Data `self `
    O.FDO-Name `FDO_data `
    O.FDO-Description `The O.FDO-Data attribute is the entry point to find 
the data associated with an FDO. If the identified 
resource is physical or conceptual, the string "self" 
is used. If the resource it digital, O.FDO-Data points 
to the Attribute that references the digital resource. 
 `
    O.FDO-Cardinality `1..n `
    O.FDO-AllowedAttribute `O.FDO-DataAsSelf `
    O.FDO-AllowedAttribute `O.FDO-DataAsAttrRef`
}
  O.FDO-DataAsSelf{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_data_as_self `
    O.FDO-Description `If identified resource is physical or conceptual, 
the string "self" is used as the value of O.FDO-Data. 
 `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string `
    O.FDO-Whitelist `self`
}
  O.FDO-DataAsAttrRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefAttrRef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_data_as_attr `
    O.FDO-Description `If the identified resource it digital, O.FDO-Data 
points to the attribute that references the digital 
resource.  `
    O.FDO-Cardinality `0..n`
}
  O.FDO-Profile{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefProfileRef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_profile `
    O.FDO-Description `This attribute points to a FDO profile. The FDO profile 
is a template for any FDO record instantiating this 
profile.  `
    O.FDO-Cardinality `1..n `
    O.FDO-AllowedProfile `O.FDO-ProfileDef`
}
  O.FDO-Name{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_resource_name `
    O.FDO-Description `A localized human-readable name for the identified 
resource  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-Description{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_resource_description `
    O.FDO-Description `A localized human-readable description for the 
identified resource  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-Cardinality{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_cardinality `
    O.FDO-Description `Obligation and repeatability of the given attribute 
in an FDO record that uses this attribute.  `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string `
    O.FDO-Regex `^(\d+)(\.\.(\d+|\*))?$`
}
  O.FDO-PrimitiveDataType{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_primitive_data_type `
    O.FDO-Description `A basic classification of which type of value an attribute 
is allowed to take on.  `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string `
    O.FDO-Whitelist `string `
    O.FDO-Whitelist `number `
    O.FDO-Whitelist `integer `
    O.FDO-Whitelist `boolean`
}
  O.FDO-Regex{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_regular_expression `
    O.FDO-Description `A string defining a regular expression `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-NumericInterval{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_numeric_interval `
    O.FDO-Description `A numeric interval of the form (a,b) (a,b] [a,b) or 
[a,b]. A square bracket means including the boundary, 
round bracket means excluding the boundary. a and 
b are decimal numbers.  `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string `
    O.FDO-Regex `^\s*(?:\[\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\]|\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)|\[\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)|\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\])\s*$ 
`
}
  O.FDO-Whitelist{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_whitelist `
    O.FDO-Description `An exhaustive enumeration of values (strings) to 
accept. Other values are rejected.  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-Blacklist{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_blacklist `
    O.FDO-Description `A non-exhaustive enumeration of values (strings) 
to reject.  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-AllowedAttributeInAttrRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefProfileRef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_allowed_attribute_in_attr `
    O.FDO-Description `An attribute definition PID that is allowed as the 
value of an attribute that uses attribute referencing. 
 `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefProfileRef `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefAttrRef `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefComb `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefUnion `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefSyntax `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDef`
}
  O.FDO-AllowedPlainNameInAttrRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_allowed_plain_name_in_attr_ref `
    O.FDO-Description `A plain name that is allowed as the value of an attribute 
that uses attribute referencing.  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string`
}
  O.FDO-AllowedProfileInProfileRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefProfileRef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_allowed_profile_in_profile `
    O.FDO-Description `PID of a profile that is allowed as the value of an attribute 
that uses profile referencing.  `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedProfileInProfileRef `O.FDO-ProfileDef`
}
  O.FDO-AllowedAttributeInCombination{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefUnion `
    O.FDO-Data `self `
    O.FDO-Name `FDO_allowed_attribute_in_combination `
    O.FDO-Description `An attribute that is part of an inline combination. 
The value is either a reference to an attribute, or 
a combination of an attribute and a localized cardinality. 
 `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedAttributeInUnion `O.FDO-BasicAttribute `
    O.FDO-AllowedAttributeInUnion `O.FDO-RefinedAttribute`
}
  O.FDO-AllowedAttributeInUnion{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefUnion `
    O.FDO-Data `self `
    O.FDO-Name `FDO_allowed_attribute_in_union `
    O.FDO-Description `An attribute that is part of a union. The value is either 
a reference to an attribute, or a combination of an 
attribute and a localized cardinality.  `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedAttributeInUnion `O.FDO-RefinedAttribute `
    O.FDO-AllowedAttributeInUnion `O.FDO-BasicAttribute`
}
  O.FDO-BasicAttribute{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefProfileRef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_basic_attribute `
    O.FDO-Description `A reference (PID) to an FDO attribute. Used in profiles, 
unions and inline combinations to specify which 
attributes must be in FDOs.  `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefSyntax `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefUnion `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefComb `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefAttrRef `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDefProfileRef `
    O.FDO-AllowedProfileInProfileRef `O.FDO-AttributeDef`
}
  O.FDO-RefinedAttribute{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefComb `
    O.FDO-Data `self `
    O.FDO-Name `FDO_refined_attribute `
    O.FDO-Description `An attribute that is refined in a new context. The 
value is a combination of an attribute and a localized 
cardinality adapted to the new context.  `
    O.FDO-Cardinality `0..* `
    O.FDO-Attribute `O.FDO-Cardinality `
    O.FDO-Attribute `O.FDO-BasicAttribute`
}
  O.FDO-DenyAdditionalAttributes{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_prohibition_of_additional_ attributes  `
    O.FDO-Description `If this attribute is not set or has a false value, additional 
attributes are allowed (recommended value)  `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `boolean`
}
  O.FDO-Extends{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefProfileRef `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_extends_profile `
    O.FDO-Description `Reference to another profile that is extended by 
this profile.  `
    O.FDO-Cardinality `0..* `
    O.FDO-PrimitiveDataType `string `
    O.FDO-AllowedProfileInProfileRef `O.FDO-ProfileDef`
}
  O.FDO-Attribute{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefUnion `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute `
    O.FDO-Description `The attributes that are required by this profile. 
One can either use an attribute as it is, or refine 
it to adapt it to the given context by providing a localized 
cardinality.  `
    O.FDO-Cardinality `0..* `
    O.FDO-AllowedAttributeInUnion `O.FDO-RefinedAttribute `
    O.FDO-AllowedAttributeInUnion `O.FDO-BasicAttribute`
}
  O.FDO-Root{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_root_profile `
    O.FDO-Description `This FDO defines the root profile. Any FDO must be 
valid against the root profile. The root profile 
requires three attributes: O.FDO-Type, O.FDO-Profile, 
O.FDO-Data.These three attributes must be used 
in any FDO. The root profile can and should be extended 
by other profiles.  `
    O.FDO-Attribute `O.FDO-Type `
    O.FDO-Attribute `O.FDO-Data `
    O.FDO-Attribute `O.FDO-Profile`
}
  O.FDO-ProfileDef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_profile_definition `
    O.FDO-Description `This FDO defines the profile definition profile. 
It is the profile that validates any other profile, 
including itself. It is the template for defining 
new FDO profiles. Any FDO profile must be valid against 
this profile.  `
    O.FDO-Attribute `O.FDO-Description `
    O.FDO-Attribute `O.FDO-Name `
    O.FDO-Attribute `O.FDO-DenyAdditionalAttributes `
    O.FDO-Attribute `O.FDO-Extends `
    O.FDO-Attribute `O.FDO-Attribute `
    O.FDO-Extends `O.FDO-Root`
}
  O.FDO-AttributeDefSyntax{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile_ `
    O.FDO-Description `This profile is the template to define new basic attributes 
(i.e., attributes that are based on syntactically 
validatable expressions).  `
    O.FDO-Extends `O.FDO-AttributeDef `
    O.FDO-Attribute `O.FDO-Regex `
    O.FDO-Attribute `O.FDO-NumericInterval `
    O.FDO-Attribute `O.FDO-Whitelist `
    O.FDO-Attribute `O.FDO-Blacklist `
    O.FDO-Attribute `O.FDO-PrimitiveDataType`
}
  O.FDO-AttributeDefProfileRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile_for_profile_referencing 
 `
    O.FDO-Description `This profile is the template to define a new attribute 
that uses the profile referencing mechanism.   `
    O.FDO-Attribute `O.FDO-AllowedProfilesInProfileRef `
    O.FDO-Extends `O.FDO-AttributeDef`
}
  O.FDO-AttributeDefAttrRef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile_ `
    O.FDO-Description `This profile is the template to define a new attribute 
that uses the attribute referencing mechanism.  
 `
    O.FDO-Extends `O.FDO-AttributeDef `
    O.FDO-Attribute `O.FDO-AllowedAttributesInAttrRef `
    O.FDO-Attribute `O.FDO-AllowedPlainNamesInAttrRef`
}
  O.FDO-AttributeDefComb{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile_for_inline_combination 
 `
    O.FDO-Description `This profile is the template to define a new attribute 
that is an inline combination of existing attributes.  
 `
    O.FDO-Attribute `O.FDO-AllowedAttributeIn `
    O.FDO-Extends `O.FDO-AttributeDef`
}
  O.FDO-AttributeDefUnion{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile_for_union 
 `
    O.FDO-Description `This profile is the template to define a new attribute 
that is a union of existing attributes.   `
    O.FDO-Extends `O.FDO-AttributeDef `
    O.FDO-Attribute `O.FDO-AllowedAttributeInUnion`
}
  O.FDO-AttributeDef{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-ProfileDef `
    O.FDO-Data `self `
    O.FDO-Name `FDO_attribute_definition_profile `
    O.FDO-Description `This FDO profile is the base template to define new 
attributes. It is extended by five different templates:  
O.FDO-AttributeDefSyntax, O.FDO-AttributeDefComb, 
O.FDO-AttributeDefUnion, O.FDO-AttributeDefProfileRef, 
and O.FDO-AttributeDefAttrRef. Each of those templates 
can be instantiated to define new attributes based 
on certain validation rules. An attribute that only 
instantiates O.FDO-AttributeDef (and none of the 
extending templates) is validated to be a string. 
 `
    O.FDO-Extends `O.FDO-Root `
    O.FDO-Attribute `O.FDO-Name `
    O.FDO-Attribute `O.FDO-Description `
    O.FDO-Attribute `O.FDO-Cardinality `
    O.FDO-Attribute `O.FDO-ValidationStrategyForCombination`
}
  O.FDO-ValidationStrategyForCombination{    O.FDO-Type `O.FDO-Profile `
    O.FDO-Profile `O.FDO-AttributeDefSyntax `
    O.FDO-Data `self `
    O.FDO-Name `FDO_validation_strategy_for_combination `
    O.FDO-Description `An attribute can use several validation mechanisms 
simultaneously. Which validation mechanism applies 
depends on the profile(s) used by the attribute definition: 
O.FDO-AttributeDefSyntax, O.FDO-AttributeDefComb, 
O.FDO-AttributeDefUnion, O.FDO-AttributeDefProfileRef, 
and O.FDO-AttributeDefAttrRef. If several of these 
profiles are used by one attribute definition, O.FDO-ValidationStrategyForCombination 
determines whether at least one validation mechanism 
must apply (anyof), or all of them (allof). The default 
is allof, in which case the attribute can be omitted. 
 `
    O.FDO-Cardinality `0..1 `
    O.FDO-PrimitiveDataType `string `
    O.FDO-Whitelist `anyof `
    O.FDO-Whitelist `allof`
}
O.FDO-Type ||--|| O.FDO-Root : ref 
O.FDO-Data ||--|| O.FDO-Root : ref 
O.FDO-DataAsSelf ||--|| O.FDO-Data : ref 
O.FDO-DataAsAttrRef ||--|| O.FDO-Data : ref 
O.FDO-Profile ||--|| O.FDO-Type : ref 
O.FDO-Profile ||--|| O.FDO-Data : ref 
O.FDO-Profile ||--|| O.FDO-DataAsSelf : ref 
O.FDO-Profile ||--|| O.FDO-DataAsAttrRef : ref 
O.FDO-Profile ||--|| O.FDO-Name : ref 
O.FDO-Profile ||--|| O.FDO-Description : ref 
O.FDO-Profile ||--|| O.FDO-Cardinality : ref 
O.FDO-Profile ||--|| O.FDO-PrimitiveDataType : ref 
O.FDO-Profile ||--|| O.FDO-Regex : ref 
O.FDO-Profile ||--|| O.FDO-NumericInterval : ref 
O.FDO-Profile ||--|| O.FDO-Whitelist : ref 
O.FDO-Profile ||--|| O.FDO-Blacklist : ref 
O.FDO-Profile ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-Profile ||--|| O.FDO-AllowedPlainNameInAttrRef : ref 
O.FDO-Profile ||--|| O.FDO-AllowedProfileInProfileRef : ref 
O.FDO-Profile ||--|| O.FDO-AllowedAttributeInCombination : ref 
O.FDO-Profile ||--|| O.FDO-AllowedAttributeInUnion : ref 
O.FDO-Profile ||--|| O.FDO-BasicAttribute : ref 
O.FDO-Profile ||--|| O.FDO-RefinedAttribute : ref 
O.FDO-Profile ||--|| O.FDO-DenyAdditionalAttributes : ref 
O.FDO-Profile ||--|| O.FDO-Extends : ref 
O.FDO-Profile ||--|| O.FDO-Attribute : ref 
O.FDO-Profile ||--|| O.FDO-Root : ref 
O.FDO-Profile ||--|| O.FDO-ProfileDef : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDefProfileRef : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDefAttrRef : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDefComb : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDefUnion : ref 
O.FDO-Profile ||--|| O.FDO-AttributeDef : ref 
O.FDO-Profile ||--|| O.FDO-ValidationStrategyForCombination : ref 
O.FDO-Name ||--|| O.FDO-ProfileDef : ref 
O.FDO-Name ||--|| O.FDO-AttributeDef : ref 
O.FDO-Description ||--|| O.FDO-ProfileDef : ref 
O.FDO-Description ||--|| O.FDO-AttributeDef : ref 
O.FDO-Cardinality ||--|| O.FDO-RefinedAttribute : ref 
O.FDO-Cardinality ||--|| O.FDO-AttributeDef : ref 
O.FDO-PrimitiveDataType ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-Regex ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-NumericInterval ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-Whitelist ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-Blacklist ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-AllowedAttributeInUnion ||--|| O.FDO-AttributeDefUnion : ref 
O.FDO-BasicAttribute ||--|| O.FDO-AllowedAttributeInCombination : ref 
O.FDO-BasicAttribute ||--|| O.FDO-AllowedAttributeInUnion : ref 
O.FDO-BasicAttribute ||--|| O.FDO-RefinedAttribute : ref 
O.FDO-BasicAttribute ||--|| O.FDO-Attribute : ref 
O.FDO-RefinedAttribute ||--|| O.FDO-AllowedAttributeInCombination : ref 
O.FDO-RefinedAttribute ||--|| O.FDO-AllowedAttributeInUnion : ref 
O.FDO-RefinedAttribute ||--|| O.FDO-Attribute : ref 
O.FDO-DenyAdditionalAttributes ||--|| O.FDO-ProfileDef : ref 
O.FDO-Extends ||--|| O.FDO-ProfileDef : ref 
O.FDO-Attribute ||--|| O.FDO-ProfileDef : ref 
O.FDO-Root ||--|| O.FDO-ProfileDef : ref 
O.FDO-Root ||--|| O.FDO-AttributeDef : ref 
O.FDO-ProfileDef ||--|| O.FDO-Profile : ref 
O.FDO-ProfileDef ||--|| O.FDO-AllowedProfileInProfileRef : ref 
O.FDO-ProfileDef ||--|| O.FDO-Extends : ref 
O.FDO-ProfileDef ||--|| O.FDO-Root : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDefProfileRef : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDefAttrRef : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDefComb : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDefUnion : ref 
O.FDO-ProfileDef ||--|| O.FDO-AttributeDef : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-DataAsSelf : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Name : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Description : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Cardinality : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-PrimitiveDataType : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Regex : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-NumericInterval : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Whitelist : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Blacklist : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-AllowedPlainNameInAttrRef : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-DenyAdditionalAttributes : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-Extends : ref 
O.FDO-AttributeDefSyntax ||--|| O.FDO-ValidationStrategyForCombination : ref 
O.FDO-AttributeDefProfileRef ||--|| O.FDO-Profile : ref 
O.FDO-AttributeDefProfileRef ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDefProfileRef ||--|| O.FDO-AllowedProfileInProfileRef : ref 
O.FDO-AttributeDefProfileRef ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDefProfileRef ||--|| O.FDO-Extends : ref 
O.FDO-AttributeDefAttrRef ||--|| O.FDO-Type : ref 
O.FDO-AttributeDefAttrRef ||--|| O.FDO-DataAsAttrRef : ref 
O.FDO-AttributeDefAttrRef ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDefAttrRef ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDefComb ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDefComb ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDefComb ||--|| O.FDO-RefinedAttribute : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-Data : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-AllowedAttributeInCombination : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-AllowedAttributeInUnion : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDefUnion ||--|| O.FDO-Attribute : ref 
O.FDO-AttributeDef ||--|| O.FDO-AllowedAttributeInAttrRef : ref 
O.FDO-AttributeDef ||--|| O.FDO-BasicAttribute : ref 
O.FDO-AttributeDef ||--|| O.FDO-AttributeDefSyntax : ref 
O.FDO-AttributeDef ||--|| O.FDO-AttributeDefProfileRef : ref 
O.FDO-AttributeDef ||--|| O.FDO-AttributeDefAttrRef : ref 
O.FDO-AttributeDef ||--|| O.FDO-AttributeDefComb : ref 
O.FDO-AttributeDef ||--|| O.FDO-AttributeDefUnion : ref 
O.FDO-ValidationStrategyForCombination ||--|| O.FDO-AttributeDef : ref 
```