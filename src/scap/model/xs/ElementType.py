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
import os.path

from scap.model.xs import *
from scap.model.xs.AnnotatedType import AnnotatedType

logger = logging.getLogger(__name__)
class ElementType(AnnotatedType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'simpleType', 'list': 'tags', 'class': 'SimpleTypeType', 'min': 0},
            {'tag_name': 'complexType', 'list': 'tags', 'class': 'ComplexTypeType', 'min': 0},
            {'tag_name': 'unique', 'list': 'tags', 'class': 'KeybaseType', 'min': 0, 'max': None},
            {'tag_name': 'key', 'list': 'tags', 'class': 'KeybaseType', 'min': 0, 'max': None},
            {'tag_name': 'keyref', 'list': 'tags', 'class': 'KeyRefElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'name': {'type': 'NCNameType'},
            'ref': {'type': 'QNameType'},
            'type': {'type': 'QNameType'},
            'substitutionGroup': {'type': 'QNameType'},
            'default': {'type': 'StringType'},
            'fixed': {'type': 'StringType'},
            'nillable': {'type': 'BooleanType', 'default': False},
            'abstract': {'type': 'BooleanType', 'default': False},
            'final': {'enum': ['#all', 'extension', 'restriction']},
            'block': {'enum': ['#all', 'extension', 'restriction', 'substitution']},
            'form': {'enum': FORM_CHOICE_ENUMERATION},
            'minOccurs': {'type': 'NonNegativeIntegerType', 'default': 1},
            'maxOccurs': {'type': 'AllNniType', 'default': 1},
            '*': {},
        }
    }

    def stub(self, path, schema):
        class_name = ''.join(cap_first(w) for w in self.name.split('_'))
        if not class_name.endswith('Element'):
            class_name = class_name + 'Element'
        schema.add_tag_mapping(self.name, class_name)

        super(ElementType, self).stub(path, schema, class_name)

    def get_defs(self, schema, top_level):
        if self.ref is not None:
            return schema.find_reference(self.ref).get_defs(schema, top_level)

        model_map = {'elements': [], 'attributes': {}}

        e = {}

        e['min'] = self.minOccurs

        if self.maxOccurs == 'unbounded':
            e['max'] = None
        else:
            e['max'] = self.maxOccurs

        if self.default is not None:
            e['default'] = self.default

        if self.nillable:
            e['nillable'] = True

        # TODO type vs. class detection
        e['class'] = self.type

        if self.maxOccurs == 'unbounded':
            e['list'] = self.name + 's'

        e['tag_name'] = self.name

        model_map['elements'].append(e)
        logger.debug('Adding element ' + str(e))

        for t in self.tags:
            defs = t.get_defs(schema, top_level)
            model_map['elements'].extend(defs['elements'])
            model_map['attributes'].update(defs['attributes'])
        return model_map
