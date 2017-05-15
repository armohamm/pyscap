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
class TableTag(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'caption', 'type': 'CaptionTag', 'min': 0},
            {'tag_name': 'col', 'type': 'ColTag', 'min': 0, 'max': None},
            {'tag_name': 'colgroup', 'type': 'ColGroupTag', 'min': 0, 'max': None},
            {'tag_name': 'thead', 'type': 'THeadTag', 'min': 0},
            {'tag_name': 'tfoot', 'type': 'TFootTag', 'min': 0},
            # choice
            {'tag_name': 'tbody', 'type': 'TBodyTag', 'min': 0, 'max': None},
            {'tag_name': 'tr', 'type': 'TRTag', 'min': 0, 'max': None},
        ],
        'attributes': {
            'summary': {'type': 'TextType'},
            'width': {'type': 'LengthType'},
            'border': {'type': 'PixelsType'},
            'frame': {'enum': T_FRAME_ENUMERATION},
            'rules': {'enum': T_RULES_ENUMERATION},
            'cellspacing': {'type': 'LengthType'},
            'cellpadding': {'type': 'LengthType'},
        },
    }
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_attrs)
