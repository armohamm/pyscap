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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions': 'OVALDefinitionsElement',
}

ELEMENT_GROUP_FUNCTION = [
    {'tag_name': 'arithmetic', 'list': 'components', 'class': 'ArithmeticFunctionType'},
    {'tag_name': 'begin', 'list': 'components', 'class': 'BeginFunctionType'},
    {'tag_name': 'concat', 'list': 'components', 'class': 'ConcatFunctionType'},
    {'tag_name': 'count', 'list': 'components', 'class': 'CountFunctionType'},
    {'tag_name': 'end', 'list': 'components', 'class': 'EndFunctionType'},
    {'tag_name': 'escape_regex', 'list': 'components', 'class': 'EscapeRegexFunctionType'},
    {'tag_name': 'split', 'list': 'components', 'class': 'SplitFunctionType'},
    {'tag_name': 'substring', 'list': 'components', 'class': 'SubstringFunctionType'},
    {'tag_name': 'time_difference', 'list': 'components', 'class': 'TimeDifferenceFunctionType'},
    {'tag_name': 'unique', 'list': 'components', 'class': 'UniqueFunctionType'},
    {'tag_name': 'regex_capture', 'list': 'components', 'class': 'RegexCaptureFunctionType'},
    {'tag_name': 'glob_to_regex', 'list': 'components', 'class': 'GlobToRegexFunctionType'},
]

ELEMENT_GROUP_COMPONENT = [
    {'tag_name': 'object_component', 'list': 'components', 'class': 'ObjectComponentType'},
    {'tag_name': 'variable_component', 'list': 'components', 'class': 'VariableComponentType'},
    {'tag_name': 'literal_component', 'list': 'components', 'class': 'LiteralComponentType'},
]
ELEMENT_GROUP_COMPONENT.extend(ELEMENT_GROUP_FUNCTION)

ARITHMETIC_ENUMERATION = [
    'add',
    'multiply',
]

DATE_TIME_FORMAT_ENUMERATION = [
    'year_month_day',
    'month_day_year',
    'day_month_year',
    'win_filetime',
    'seconds_since_epoch',
    'cim_datetime',
]

FILTER_ACTION_ENUMERATION = [
    'exclude',
    'include',
]

SET_OPERATOR_ENUMERATION = [
    'COMPLEMENT',
    'INTERSECTION',
    'UNION',
]

#                  ||                                   ||
#  set_operator is ||            obj 1 flag             ||
#       union      ||                                   ||
#                  ||  E  |  C  |  I  | DNE | NC  | NA  ||
# -----------------||-----------------------------------||
#                E ||  E  |  E  |  E  |  E  |  E  |  E  ||
#   obj          C ||  E  |  C  |  I  |  C  |  I  |  C  ||
#    2           I ||  E  |  I  |  I  |  I  |  I  |  I  ||
#   flag       DNE ||  E  |  C  |  I  | DNE |  I  | DNE ||
#               NC ||  E  |  I  |  I  |  I  |  NC |  NC ||
#               NA ||  E  |  C  |  I  | DNE |  NC |  NA ||
# -----------------||-----------------------------------||

# TODO set_operator_union(set)

#                  ||                                   ||
#  set_operator is ||             obj 1 flag            ||
#   intersection   ||                                   ||
#                  ||  E  |  C  |  I  | DNE | NC  | NA  ||
# -----------------||-----------------------------------||
#                E ||  E  |  E  |  E  | DNE |  E  |  E  ||
#    obj         C ||  E  |  C  |  I  | DNE |  NC |  C  ||
#     2          I ||  E  |  I  |  I  | DNE |  NC |  I  ||
#    flag      DNE || DNE | DNE | DNE | DNE | DNE | DNE ||
#               NC ||  E  |  NC |  NC | DNE |  NC |  NC ||
#               NA ||  E  |  C  |  I  | DNE |  NC |  NA ||
# -----------------||-----------------------------------||

# TODO set_operator_intersection(set)

#                  ||                                   ||
#  set_operator is ||             obj 1 flag            ||
#     complement   ||                                   ||
#                  ||  E  |  C  |  I  | DNE | NC  | NA  ||
# -----------------||-----------------------------------||
#                E ||  E  |  E  |  E  | DNE |  E  |  E  ||
#    obj         C ||  E  |  C  |  I  | DNE |  NC |  E  ||
#     2          I ||  E  |  E  |  E  | DNE |  NC |  E  ||
#    flag      DNE ||  E  |  C  |  I  | DNE |  NC |  E  ||
#               NC ||  E  |  NC |  NC | DNE |  NC |  E  ||
#               NA ||  E  |  E  |  E  |  E  |  E  |  E  ||
# -----------------||-----------------------------------||

# TODO set_operator_complement(set)
