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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions': 'OvalDefinitionsElement',
}

ELEMENT_GROUP_FUNCTION = [
    {'tag_name': 'begin', 'list': 'components', 'class': 'BeginFunctionType', 'min': 0, 'max': None},
    {'tag_name': 'concat', 'list': 'components', 'class': 'ConcatFunctionType', 'min': 0, 'max': None},
    {'tag_name': 'end', 'list': 'components', 'class': 'EndFunctionType', 'min': 0, 'max': None},
    {'tag_name': 'escape_regex', 'list': 'components', 'class': 'EscapeRegexFunctionType', 'min': 0, 'max': None},
    {'tag_name': 'split', 'list': 'components', 'class': 'SplitFunctionType', 'min': 0, 'max': None},
    {'tag_name': 'substring', 'list': 'components', 'class': 'SubstringFunctionType', 'min': 0, 'max': None},
]

ELEMENT_GROUP_COMPONENT = [
    {'tag_name': 'object_component', 'list': 'components', 'class': 'ObjectComponentType', 'min': 0, 'max': None},
    {'tag_name': 'variable_component', 'list': 'components', 'class': 'VariableComponentType', 'min': 0, 'max': None},
    {'tag_name': 'literal_component', 'list': 'components', 'class': 'AnySimpleType', 'min': 0, 'max': None},
]
ELEMENT_GROUP_COMPONENT.extend(ELEMENT_GROUP_FUNCTION)

CLASS_ENUMERATION = [
    'compliance',
    'inventory',
    'miscellaneous',
    'patch',
    'vulnerability',
]

SET_OPERATOR_ENUMERATION = [
    'COMPLEMENT',
    'INTERSECTION',
    'UNION',
]
