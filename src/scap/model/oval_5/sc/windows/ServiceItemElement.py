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

from .EntityItemServiceControlsAcceptedType import EntityItemServiceControlsAcceptedType
from .EntityItemServiceCurrentStateType import EntityItemServiceCurrentStateType
from .EntityItemServiceStartTypeType import EntityItemServiceStartTypeType
from .EntityItemServiceTypeType import EntityItemServiceTypeType

logger = logging.getLogger(__name__)

@element(local_name='service_name', max=1, min=0, cls=EntityItemType)
@element(local_name='display_name', max=1, min=0, cls=EntityItemType)
@element(local_name='description', max=1, min=0, cls=EntityItemType)
@element(local_name='service_type', max=None, list='service_types', min=0, cls=EntityItemServiceTypeType)
@element(local_name='start_type', max=1, min=0, cls=EntityItemServiceStartTypeType)
@element(local_name='current_state', max=1, min=0, cls=EntityItemServiceCurrentStateType)
@element(local_name='controls_accepted', max=None, list='controls_accepteds', min=0, cls=EntityItemServiceControlsAcceptedType)
@element(local_name='start_name', max=1, min=0, cls=EntityItemType)
@element(local_name='path', max=1, min=0, cls=EntityItemType)
@element(local_name='pid', max=1, min=0, cls=EntityItemType)
@element(local_name='service_flag', max=1, min=0, cls=EntityItemType)
@element(local_name='dependencies', max=None, list='dependenciess', min=0, cls=EntityItemType)
class ServiceItemElement(ItemType):
    pass
