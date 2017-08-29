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
from scap.model.oval_5 import WINDOWS_VIEW_ENUMERATION

from ..EntityStateType import EntityStateType

from .EntityStateRegistryHiveType import EntityStateRegistryHiveType
from .EntityStateRegistryTypeType import EntityStateRegistryTypeType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='hive', cls=EntityStateRegistryHiveType, min=0)
@element(local_name='key', cls=EntityStateType, min=0)
@element(local_name='name', cls=EntityStateType, min=0)
@element(local_name='last_write_time', cls=EntityStateType, min=0)
@element(local_name='type', cls=EntityStateRegistryTypeType, min=0)
@element(local_name='value', cls=EntityStateType, min=0)
@element(local_name='windows_view', cls=EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
class RegistryStateElement(StateType):
    pass
