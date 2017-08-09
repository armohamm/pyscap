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
            {'tag_name': 'group', 'list': 'tags', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'all', 'list': 'tags', 'class': 'AllType', 'min': 0},
            {'tag_name': 'choice', 'list': 'tags', 'class': 'ChoiceElement', 'min': 0},
            {'tag_name': 'sequence', 'list': 'tags', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'simpleType', 'list': 'tags', 'class': 'SimpleTypeType', 'min': 0},
            {'tag_name': 'minExclusive', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'minInclusive', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxExclusive', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxInclusive', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'totalDigits', 'list': 'tags', 'class': 'TotalDigitsElement', 'min': 0, 'max': None},
            {'tag_name': 'fractionDigits', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'length', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'minLength', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'maxLength', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'enumeration', 'list': 'tags', 'class': 'FacetType', 'min': 0, 'max': None},
            {'tag_name': 'whiteSpace', 'list': 'tags', 'class': 'WhitespaceElement', 'min': 0, 'max': None},
            {'tag_name': 'pattern', 'list': 'tags', 'class': 'PatternElement', 'min': 0, 'max': None},
            {'tag_name': 'attribute', 'list': 'tags', 'class': 'AttributeType', 'min': 0, 'max': None},
            {'tag_name': 'attributeGroup', 'list': 'tags', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
            {'tag_name': 'anyAttribute', 'list': 'tags', 'class': 'WildcardType', 'min': 0},
        ],
        'attributes': {
            'base': {'type': 'QNameType'},
        }
    }

    def get_defs(self, schema, top_level):
        logger.debug('Base: ' + self.base)
        # TODO unable to map xmlns because ET doesn't retain it
        base_ns, base_name = [self.base.partition(':')[i] for i in [0,2]]
        top_level.set_super_module(base_ns)
        top_level.set_super_class(base_name)

        return super(RestrictionType, self).get_defs(schema, top_level)
