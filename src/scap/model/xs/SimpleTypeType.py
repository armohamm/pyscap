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
class SimpleTypeType(AnnotatedType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'restriction', 'list': 'tags', 'class': 'RestrictionType', 'min': 0},
            {'tag_name': 'list', 'list': 'tags', 'class': 'ListElement', 'min': 0},
            {'tag_name': 'union', 'list': 'tags', 'class': 'UnionElement', 'min': 0},
        ],
        'attributes': {
            'final': {'enum': ['#all', 'list', 'union', 'restriction']},
            'name': {'type': 'NCNameType'},
            '*': {},
        }
    }

    def stub(self, path, schema):
        class_name = ''.join(cap_first(w) for w in self.name.split('_'))
        if not class_name.endswith('Type'):
            class_name = class_name + 'Type'
        super(SimpleTypeType, self).stub(path, schema, class_name)
