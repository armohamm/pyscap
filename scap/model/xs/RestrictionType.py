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

import logging

from scap.model.xs import *
from scap.model.xs.AnnotatedType import AnnotatedType

logger = logging.getLogger(__name__)
class RestrictionType(AnnotatedType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'group', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'all', 'class': 'AllType', 'min': 0},
            {'tag_name': 'choice', 'class': 'ChoiceElement', 'min': 0},
            {'tag_name': 'sequence', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'simpleType', 'class': 'SimpleTypeType', 'min': 0},
            {'tag_name': 'minExclusive', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'minInclusive', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxExclusive', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxInclusive', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'totalDigits', 'class': 'TotalDigitsElement', 'min': 0, 'max': None},
            {'tag_name': 'fractionDigits', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'length', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'minLength', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxLength', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'enumeration', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'whiteSpace', 'class': 'WhitespaceElement', 'min': 0, 'max': None},
            {'tag_name': 'pattern', 'class': 'PatternElement', 'min': 0, 'max': None},
            {'tag_name': 'attribute', 'class': 'AttributeType', 'min': 0, 'max': None},
            {'tag_name': 'attributeGroup', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
            {'tag_name': 'anyAttribute', 'class': 'WildcardType', 'min': 0},
        ],
        'attributes': {
            'base': {'type': 'QNameType'},
        }
    }
