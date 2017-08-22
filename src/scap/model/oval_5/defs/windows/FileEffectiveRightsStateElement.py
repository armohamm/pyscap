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

from scap.model.oval_5 import WINDOWS_VIEW_ENUMERATION
from scap.model.oval_5.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)
class FileEffectiveRightsStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'fileeffectiverights_state',
        'elements': [
@element(local_name='path', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='filename', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='trustee_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_delete', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_read_control', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_write_dac', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_write_owner', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_synchronize', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_system_security', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='generic_read', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='generic_write', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='generic_execute', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='generic_all', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_read_data', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_write_data', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_append_data', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_read_ea', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_write_ea', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_execute', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_delete_child', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_read_attributes', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_write_attributes', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='windows_view', cls=scap.model.oval_5.defs.EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
        ],
    }
