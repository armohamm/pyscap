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

from scap.model.oval_5.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)
class SharedResourceStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'sharedresource_state',
        'elements': [
@element(local_name='netname', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='shared_type', cls=EntityStateSharedResourceTypeType, min=0)
@element(local_name='max_uses', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='current_uses', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='local_path', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_read_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_write_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_create_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_exec_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_delete_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_atrib_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_perm_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='access_all_permission', cls=scap.model.oval_5.defs.EntityStateType, min=0)
        ],
    }
