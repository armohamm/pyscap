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

class RegistryItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='hive', max=1, min=0, cls=EntityItemRegistryHiveType)
@element(local_name='key', max=1, 'nillable': True, min=0, cls=scap.model.oval_5.sc.EntityItemType)
@element(local_name='name', max=1, 'nillable': True, min=0, cls=scap.model.oval_5.sc.EntityItemType)
@element(local_name='last_write_time', max=1, min=0, cls=scap.model.oval_5.sc.EntityItemType)
@element(local_name='type', max=1, min=0, cls=EntityItemRegistryTypeType)
@element(local_name='value', max=None, list='values', min=0, cls=scap.model.oval_5.sc.EntityItemType)
@element(local_name='windows_view', max=1, min=0, cls=EntityItemWindowsViewType)
        ],
        'attributes': {
        },
    }
