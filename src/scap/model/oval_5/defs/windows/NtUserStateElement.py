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
class NtUserStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'ntuser_state',
        'elements': [
@element(local_name='key', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sid', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='username', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='account_type', cls=EntityStateNTUserAccountTypeType, min=0)
@element(local_name='logged_on', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='enabled', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='date_modified', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='days_since_modified', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='filepath', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='last_write_time', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='type', cls=scap.model.oval_5.defs.EntityStateRegistryTypeType, min=0)
@element(local_name='value', cls=scap.model.oval_5.defs.EntityStateType, min=0)
        ],
    }
