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

from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class CmdletItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'module_name', 'max': 1, 'nillable': True, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'module_id', 'max': 1, 'nillable': True, 'min': 0, 'class': 'EntityItemGUIDType'},
            {'tag_name': 'module_version', 'max': 1, 'nillable': True, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemVersionType'},
            {'tag_name': 'verb', 'max': 1, 'min': 0, 'class': 'EntityItemCmdletVerbType'},
            {'tag_name': 'noun', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'parameters', 'max': 1, 'nillable': True, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemRecordType'},
            {'tag_name': 'select', 'max': 1, 'nillable': True, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemRecordType'},
            {'tag_name': 'value', 'max': None, 'list': 'values', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemRecordType'},
        ],
        'attributes': {
        },
    }

