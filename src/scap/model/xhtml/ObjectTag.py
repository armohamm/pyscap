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

from scap.model.xhtml import *
from scap.Model import Model

logger = logging.getLogger(__name__)
class ObjectTag(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'param', 'list': '_elements', 'class': 'ParamType', 'min': 0, 'max': None},
        ],
        'attributes': {
            'declare': {'enum': ['declare']},
            'classid': {'type:' 'UriType'},
            'codebase': {'type:' 'UriType'},
            'data': {'type:' 'UriType'},
            'type': {'type:' 'ContentTypeType'},
            'codetype': {'type:' 'ContentTypeType'},
            'archive': {'type:' 'UriListType'},
            'standby': {'type:' 'TextType'},
            'height': {'type:' 'LengthType'},
            'width': {'type:' 'LengthType'},
            'usemap': {'type:' 'UriType'},
            'name': {'type:' 'NMTokenType'},
            'tabindex': {'type:' 'TabIndexNumberType'},
        },
    }
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_block)
    MODEL_MAP['elements'].append({'tag_name': 'form', 'list': '_elements', 'class': 'FormType', 'min': 0, 'max': None})
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_inline)
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_misc)
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_attrs)
