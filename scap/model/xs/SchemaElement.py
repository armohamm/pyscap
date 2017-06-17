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
from scap.model.xs.AnyTypeType import AnyTypeType

logger = logging.getLogger(__name__)
class SchemaElement(AnyTypeType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'include', 'list': 'tags', 'class': 'IncludeElement', 'min': 0, 'max': None},
            {'tag_name': 'import', 'list': 'tags', 'class': 'ImportElement', 'min': 0, 'max': None},
            {'tag_name': 'redefine', 'list': 'tags', 'class': 'RedefineElement', 'min': 0, 'max': None},
            {'tag_name': 'annotation', 'list': 'tags', 'class': 'AnnotationElement', 'min': 0, 'max': None},
            {'tag_name': 'simpleType', 'list': 'tags', 'class': 'SimpleTypeType', 'min': 0, 'max': None},
            {'tag_name': 'complexType', 'list': 'tags', 'class': 'ComplexTypeType', 'min': 0, 'max': None},
            {'tag_name': 'group', 'list': 'tags', 'class': 'GroupType', 'min': 0, 'max': None},
            {'tag_name': 'attributeGroup', 'list': 'tags', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
            {'tag_name': 'element', 'list': 'tags', 'class': 'ElementType', 'min': 0, 'max': None},
            {'tag_name': 'attribute', 'list': 'tags', 'class': 'AttributeType', 'min': 0, 'max': None},
            {'tag_name': 'notation', 'list': 'tags', 'class': 'NotationElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'targetNamespace': {'type': 'AnyUriType'},
            'version': {'type': 'TokenType'},
            'finalDefault': {'enum': ['#all', 'extension', 'restriction', 'list', 'union']},
            'blockDefault': {'enum': ['#all', 'extension', 'restriction', 'substitution']},
            'attributeFormDefault': {'enum': FORM_CHOICE_ENUMERATION, 'default': 'unqualified'},
            'elementFormDefault': {'enum': FORM_CHOICE_ENUMERATION, 'default': 'unqualified'},
            'id': {'type': 'IdType'},
            # xml:lang
        },
    }

    def add_enumeration(self, name, enum):
        self._enumerations[name] = enum

    def add_tag_mapping(self, name, class_name):
        self._tag_mapping[name] = class_name

    def stub(self, path):
        self._enumerations = {}
        self._tag_mapping = {}

        for c in self.tags:
            if c.tag_name in ['simpleType', 'complexType', 'element']:
                c.stub(path, self)

        with open(os.path.join(path, '__init__.py'), 'w') as f:
            f.write(STUB_HEADER)
            f.write('TAG_MAP = {\n')
            for name in sorted(self._tag_mapping.keys()):
                f.write("    '{" + self.targetNamespace + '}' + name + "': '" + self._tag_mapping[name] + "',\n")
            f.write('}\n\n')

        logger.debug('Wrote __init__.py')
