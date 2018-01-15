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

from expatriate.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

from .EntityItemEndpointType import EntityItemEndpointType
from .EntityItemWaitStatusType import EntityItemWaitStatusType

logger = logging.getLogger(__name__)

@element(local_name='protocol', min=0, cls=EntityItemType, max=1)
@element(local_name='service_name', min=0, cls=EntityItemType, max=1)
@element(local_name='server_program', min=0, cls=EntityItemType, max=1)
@element(local_name='server_arguments', min=0, cls=EntityItemType, max=1)
@element(local_name='endpoint_type', min=0, cls=EntityItemEndpointType, max=1)
@element(local_name='exec_as_user', min=0, cls=EntityItemType, max=1)
@element(local_name='wait_status', min=0, cls=EntityItemWaitStatusType, max=1)
class InetdItemElement(ItemType):
    pass
