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
from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

class PartitionItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='mount_point', cls=EntityItemType, min=0, max=1)
@element(local_name='device', cls=EntityItemType, min=0, max=1)
@element(local_name='uuid', cls=EntityItemType, min=0, max=1)
@element(local_name='fs_type', cls=EntityItemType, min=0, max=1)
@element(local_name='mount_options', cls=EntityItemType, min=0, max=1)
@element(local_name='total_space', cls=EntityItemType, min=0, max=1)
@element(local_name='space_used', cls=EntityItemType, min=0, max=1)
@element(local_name='space_left', cls=EntityItemType, min=0, max=1)
        ],
    }
