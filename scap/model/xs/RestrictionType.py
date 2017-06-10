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
        ],
        'attributes': {
            'base': {'type': 'QNameType'},
        }
    }
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_TYPE_DEF_PARTICLE)
    MODEL_MAP['elements'].append({'tag_name': 'simpleType', 'class': 'SimpleTypeType', 'min': 0})
    MODEL_MAP['elements'].extend([
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
    ])
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_ATTR_DECLS)
