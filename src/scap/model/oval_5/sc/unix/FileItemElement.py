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

from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class FileItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'filepath', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'path', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'filename', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'nillable': True, 'max': 1},
            {'tag_name': 'type', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'group_id', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'user_id', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'a_time', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'c_time', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'm_time', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'size', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'suid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'sgid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'sticky', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'uread', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'uwrite', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'uexec', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'gread', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'gwrite', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'gexec', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'oread', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'owrite', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'oexec', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
            {'tag_name': 'has_extended_acl', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType', 'max': 1},
        ],
        'attributes': {
        },
    }
