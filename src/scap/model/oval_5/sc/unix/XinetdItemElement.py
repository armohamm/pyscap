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

from ..EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

class XinetdItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='protocol', min=0, cls=EntityItemType, max=1)
@element(local_name='service_name', min=0, cls=EntityItemType, max=1)
            {list='flagss', 'tag_name': 'flags', min=0, cls=EntityItemType, max=None},
            {list='no_accesss', 'tag_name': 'no_access', min=0, cls=EntityItemType, max=None},
            {list='only_froms', 'tag_name': 'only_from', min=0, cls=scap.model.oval_5.sc.EntityItemIPAddressStringType, max=None},
@element(local_name='port', min=0, cls=EntityItemType, max=1)
@element(local_name='server', min=0, cls=EntityItemType, max=1)
@element(local_name='server_arguments', min=0, cls=EntityItemType, max=1)
@element(local_name='socket_type', min=0, cls=EntityItemType, max=1)
@element(local_name='type', min=0, cls=EntityItemXinetdTypeStatusType, max=1)
@element(local_name='user', min=0, cls=EntityItemType, max=1)
@element(local_name='wait', min=0, cls=EntityItemType, max=1)
@element(local_name='disabled', min=0, cls=EntityItemType, max=1)
        ],
        'attributes': {
        },
    }
