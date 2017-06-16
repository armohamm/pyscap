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
from scap.model.xs.AnyTypeType import AnyTypeType

logger = logging.getLogger(__name__)
class SchemaElement(AnyTypeType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'include', 'class': 'IncludeElement', 'min': 0, 'max': None},
            {'tag_name': 'import', 'class': 'ImportElement', 'min': 0, 'max': None},
            {'tag_name': 'redefine', 'class': 'RedefineElement', 'min': 0, 'max': None},
            {'tag_name': 'annotation', 'class': 'AnnotationElement', 'min': 0, 'max': None},
            {'tag_name': 'simpleType', 'class': 'SimpleTypeType', 'min': 0, 'max': None},
            {'tag_name': 'complexType', 'class': 'ComplexTypeType', 'min': 0, 'max': None},
            {'tag_name': 'group', 'class': 'GroupType', 'min': 0, 'max': None},
            {'tag_name': 'attributeGroup', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
            {'tag_name': 'element', 'class': 'ElementType', 'min': 0, 'max': None},
            {'tag_name': 'attribute', 'class': 'AttributeType', 'min': 0, 'max': None},
            {'tag_name': 'notation', 'class': 'NotationElement', 'min': 0, 'max': None},
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

    def stub(self, path):
