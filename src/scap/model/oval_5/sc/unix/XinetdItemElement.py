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

from ..EntityItemIPAddressStringType import EntityItemIPAddressStringType
from ..EntityItemType import EntityItemType

from .EntityItemXinetdTypeStatusType import EntityItemXinetdTypeStatusType

logger = logging.getLogger(__name__)

@element(local_name='protocol', min=0, cls=EntityItemType, max=1)
@element(local_name='service_name', min=0, cls=EntityItemType, max=1)
@element(local_name='flags', list='flagss', min=0, cls=EntityItemType, max=None)
@element(local_name='no_access', list='no_accesss', min=0, cls=EntityItemType, max=None)
@element(local_name='only_from', list='only_froms', min=0, cls=EntityItemIPAddressStringType, max=None)
@element(local_name='port', min=0, cls=EntityItemType, max=1)
@element(local_name='server', min=0, cls=EntityItemType, max=1)
@element(local_name='server_arguments', min=0, cls=EntityItemType, max=1)
@element(local_name='socket_type', min=0, cls=EntityItemType, max=1)
@element(local_name='type', min=0, cls=EntityItemXinetdTypeStatusType, max=1)
@element(local_name='user', min=0, cls=EntityItemType, max=1)
@element(local_name='wait', min=0, cls=EntityItemType, max=1)
@element(local_name='disabled', min=0, cls=EntityItemType, max=1)
class XinetdItemElement(ItemType):
    pass
