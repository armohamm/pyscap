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

from scap.Model import Model
from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class SeLinuxSecurityContextItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'path', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'filename', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1, 'nillable': True},
            {'tag_name': 'pid', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1, 'nillable': True},
            {'tag_name': 'user', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'role', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'type', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'low_sensitivity', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'low_category', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'high_sensitivity', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'high_category', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'rawlow_sensitivity', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'rawlow_category', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'rawhigh_sensitivity', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'rawhigh_category', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
        ],
    }
