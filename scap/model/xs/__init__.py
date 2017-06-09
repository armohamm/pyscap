# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

TAG_MAP = {
    '{http://www.w3.org/2001/XMLSchema}schema': 'SchemaElement',
}

i_ = r'[A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD]'
c_ = r'[-.0-9A-Z_a-z\u00B7\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u037D\u037F-\u1FFF\u200C-\u200D\u203F\u2040\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD]'

ELEMENT_GROUP_REDEFINABLE = []
ELEMENT_GROUP_REDEFINABLE.append({'tag_name': 'simpleType', 'class': 'SimpleTypeElement', 'min': 0, 'max': None})
ELEMENT_GROUP_REDEFINABLE.append({'tag_name': 'complexType', 'class': 'ComplexTypeElement', 'min': 0, 'max': None})
ELEMENT_GROUP_REDEFINABLE.append({'tag_name': 'group', 'class': 'GroupElement', 'min': 0, 'max': None})
ELEMENT_GROUP_REDEFINABLE.append({'tag_name': 'attributeGroup', 'class': 'AttributeGroupElement', 'min': 0, 'max': None})

ELEMENT_GROUP_SCHEMA_TOP = []
ELEMENT_GROUP_SCHEMA_TOP.extend(ELEMENT_GROUP_REDEFINABLE)
ELEMENT_GROUP_SCHEMA_TOP.append({'tag_name': 'element', 'class': 'ElementElement', 'min': 0, 'max': None})
ELEMENT_GROUP_SCHEMA_TOP.append({'tag_name': 'attribute', 'class': 'AttributeElement', 'min': 0, 'max': None})
ELEMENT_GROUP_SCHEMA_TOP.append({'tag_name': 'notation', 'class': 'NotationElement', 'min': 0, 'max': None})

ATTRIBUTE_GROUP_OCCURS = {
    'minOccurs': {'type': 'NonNegativeIntegerType', 'default': 1},
    'maxOccurs': {'type': 'AllNniType', 'default': 1},
}

ATTRIBUTE_GROUP_DEF_REF = {
    'name': {'type': 'NCNameType'},
    'ref': {'type': 'QNameType'},
}

ELEMENT_GROUP_TYPE_DEF_PARTICLE = [
    {'tag_name': 'group', 'class': 'GroupRefType', 'min': 0},
    {'tag_name': 'all', 'class': 'AllElement', 'min': 0},
    {'tag_name': 'choice', 'class': 'ChoiceElement', 'min': 0},
    {'tag_name': 'sequence', 'class': 'SequenceElement', 'min': 0},
]

ELEMENT_GROUP_NESTED_PARTICLE = [
    {'tag_name': 'element', 'class': 'LocalElementType', 'min': 0},
    {'tag_name': 'group', 'class': 'GroupRefType', 'min': 0},
    {'tag_name': 'choice', 'class': 'ChoiceElement', 'min': 0},
    {'tag_name': 'sequence', 'class': 'SequenceElement', 'min': 0},
    {'tag_name': 'any', 'class': 'AnyElement', 'min': 0},
]

ELEMENT_GROUP_PARTICLE = [
    {'tag_name': 'element', 'class': 'LocalElementType', 'min': 0},
    {'tag_name': 'group', 'class': 'GroupRefType', 'min': 0},
    {'tag_name': 'all', 'class': 'AllElement', 'min': 0},
    {'tag_name': 'choice', 'class': 'ChoiceElement', 'min': 0},
    {'tag_name': 'sequence', 'class': 'SequenceElement', 'min': 0},
]

ELEMENT_GROUP_ATTR_DECLS = [
    {'tag_name': 'attribute', 'class': 'AttributeType', 'min': 0, 'max': None},
    {'tag_name': 'attributeGroup', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
    {'tag_name': 'anyAttribute', 'class': 'AnyAttributeElement', 'min': 0},
]

ELEMENT_GROUP_COMPLEX_TYPE_MODEL = [
    {'tag_name': 'simpleContent', 'class': 'SimpleContentElement', 'min': 0, 'max': None},
    {'tag_name': 'complexContent', 'class': 'ComplexContentElement', 'min': 0, 'max': None},
]
ELEMENT_GROUP_COMPLEX_TYPE_MODEL.extend(ELEMENT_GROUP_TYPE_DEF_PARTICLE)
ELEMENT_GROUP_COMPLEX_TYPE_MODEL.extend(ELEMENT_GROUP_ATTR_DECLS)

ELEMENT_GROUP_ALL_MODEL = [
    {'tag_name': 'annotation', 'class': 'AnnotationElement', 'min': 0},
    {'tag_name': 'element', 'class': 'NarrowMaxMinType', 'min': 0, 'max': None},
]

ELEMENT_GROUP_IDENTITY_CONSTRAINT = [
    {'tag_name': 'unique', 'class': 'UniqueElement', 'min': 0},
    {'tag_name': 'key', 'class': 'KeyElement', 'min': 0},
    {'tag_name': 'keyref', 'class': 'KeyRefElement', 'min': 0},
]

ELEMENT_GROUP_SIMPLE_DERIVATION = [
    {'tag_name': 'restriction', 'class': 'RestrictionElement', 'min': 0},
    {'tag_name': 'list', 'class': 'ListElement', 'min': 0},
    {'tag_name': 'union', 'class': 'UnionElement', 'min': 0},
]

ELEMENT_GROUP_FACETS = [
    {'tag_name': 'minExclusive', 'class': 'MinExclusiveElement', 'min': 0, 'max': None},
    {'tag_name': 'minInclusive', 'class': 'MinInclusiveElement', 'min': 0, 'max': None},
    {'tag_name': 'maxExclusive', 'class': 'MaxExclusiveElement', 'min': 0, 'max': None},
    {'tag_name': 'maxInclusive', 'class': 'MaxInclusiveElement', 'min': 0, 'max': None},
    {'tag_name': 'totalDigits', 'class': 'TotalDigitsElement', 'min': 0, 'max': None},
    {'tag_name': 'fractionDigits', 'class': 'FractionDigitsElement', 'min': 0, 'max': None},
    {'tag_name': 'length', 'class': 'LengthElement', 'min': 0, 'max': None},
    {'tag_name': 'minLength', 'class': 'MinLengthElement', 'min': 0, 'max': None},
    {'tag_name': 'maxLength', 'class': 'MaxLengthElement', 'min': 0, 'max': None},
    {'tag_name': 'enumeration', 'class': 'EnumerationElement', 'min': 0, 'max': None},
    {'tag_name': 'whiteSpace', 'class': 'WhitespaceElement', 'min': 0, 'max': None},
    {'tag_name': 'pattern', 'class': 'PatternElement', 'min': 0, 'max': None},
]

ELEMENT_GROUP_SIMPLE_RESTRICTION_MODEL = [
    {'tag_name': 'simpleType', 'class': 'LocalSimpleTypeType', 'min': 0},
]
ELEMENT_GROUP_SIMPLE_RESTRICTION_MODEL.extend(ELEMENT_GROUP_FACETS)
