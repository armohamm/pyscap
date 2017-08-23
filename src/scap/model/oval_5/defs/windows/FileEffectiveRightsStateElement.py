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

from .StateType import StateType
from ..EntityStateType import EntityStateType

logger = logging.getLogger(__name__)

@element(local_name='path', cls=EntityStateType, min=0)
@element(local_name='filename', cls=EntityStateType, min=0)
@element(local_name='trustee_name', cls=EntityStateType, min=0)
@element(local_name='standard_delete', cls=EntityStateType, min=0)
@element(local_name='standard_read_control', cls=EntityStateType, min=0)
@element(local_name='standard_write_dac', cls=EntityStateType, min=0)
@element(local_name='standard_write_owner', cls=EntityStateType, min=0)
@element(local_name='standard_synchronize', cls=EntityStateType, min=0)
@element(local_name='access_system_security', cls=EntityStateType, min=0)
@element(local_name='generic_read', cls=EntityStateType, min=0)
@element(local_name='generic_write', cls=EntityStateType, min=0)
@element(local_name='generic_execute', cls=EntityStateType, min=0)
@element(local_name='generic_all', cls=EntityStateType, min=0)
@element(local_name='file_read_data', cls=EntityStateType, min=0)
@element(local_name='file_write_data', cls=EntityStateType, min=0)
@element(local_name='file_append_data', cls=EntityStateType, min=0)
@element(local_name='file_read_ea', cls=EntityStateType, min=0)
@element(local_name='file_write_ea', cls=EntityStateType, min=0)
@element(local_name='file_execute', cls=EntityStateType, min=0)
@element(local_name='file_delete_child', cls=EntityStateType, min=0)
@element(local_name='file_read_attributes', cls=EntityStateType, min=0)
@element(local_name='file_write_attributes', cls=EntityStateType, min=0)
@element(local_name='windows_view', cls=EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
class FileEffectiveRightsStateElement(StateType):
    pass
