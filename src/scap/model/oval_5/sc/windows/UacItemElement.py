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

@element(local_name='admin_approval_mode', max=1, min=0, cls=EntityItemType)
@element(local_name='elevation_prompt_admin', max=1, min=0, cls=EntityItemType)
@element(local_name='elevation_prompt_standard', max=1, min=0, cls=EntityItemType)
@element(local_name='detect_installations', max=1, min=0, cls=EntityItemType)
@element(local_name='elevate_signed_executables', max=1, min=0, cls=EntityItemType)
@element(local_name='elevate_uiaccess', max=1, min=0, cls=EntityItemType)
@element(local_name='run_admins_aam', max=1, min=0, cls=EntityItemType)
@element(local_name='secure_desktop', max=1, min=0, cls=EntityItemType)
@element(local_name='virtualize_write_failures', max=1, min=0, cls=EntityItemType)
class UacItemElement(ItemType):
    pass
