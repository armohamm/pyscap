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

class SeLinuxSecurityContextItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='filepath', cls=EntityItemType, min=0, max=1)
@element(local_name='path', cls=EntityItemType, min=0, max=1)
@element(local_name='filename', cls=EntityItemType, min=0, max=1, 'nillable': True)
@element(local_name='pid', cls=EntityItemType, min=0, max=1, 'nillable': True)
@element(local_name='user', cls=EntityItemType, min=0, max=1)
@element(local_name='role', cls=EntityItemType, min=0, max=1)
@element(local_name='type', cls=EntityItemType, min=0, max=1)
@element(local_name='low_sensitivity', cls=EntityItemType, min=0, max=1)
@element(local_name='low_category', cls=EntityItemType, min=0, max=1)
@element(local_name='high_sensitivity', cls=EntityItemType, min=0, max=1)
@element(local_name='high_category', cls=EntityItemType, min=0, max=1)
@element(local_name='rawlow_sensitivity', cls=EntityItemType, min=0, max=1)
@element(local_name='rawlow_category', cls=EntityItemType, min=0, max=1)
@element(local_name='rawhigh_sensitivity', cls=EntityItemType, min=0, max=1)
@element(local_name='rawhigh_category', cls=EntityItemType, min=0, max=1)
        ],
    }
