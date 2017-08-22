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
class RegKeyAuditedPermissions53StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'regkeyauditedpermissions53_state',
        'elements': [
@element(local_name='hive', cls=EntityStateRegistryHiveType, min=0)
@element(local_name='key', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='trustee_sid', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='standard_delete', cls=EntityStateAuditType, min=0)
@element(local_name='standard_read_control', cls=EntityStateAuditType, min=0)
@element(local_name='standard_write_dac', cls=EntityStateAuditType, min=0)
@element(local_name='standard_write_owner', cls=EntityStateAuditType, min=0)
@element(local_name='standard_synchronize', cls=EntityStateAuditType, min=0)
@element(local_name='access_system_security', cls=EntityStateAuditType, min=0)
@element(local_name='generic_read', cls=EntityStateAuditType, min=0)
@element(local_name='generic_write', cls=EntityStateAuditType, min=0)
@element(local_name='generic_execute', cls=EntityStateAuditType, min=0)
@element(local_name='generic_all', cls=EntityStateAuditType, min=0)
@element(local_name='key_query_value', cls=EntityStateAuditType, min=0)
@element(local_name='key_set_value', cls=EntityStateAuditType, min=0)
@element(local_name='key_create_sub_key', cls=EntityStateAuditType, min=0)
@element(local_name='key_enumerate_sub_keys', cls=EntityStateAuditType, min=0)
@element(local_name='key_notify', cls=EntityStateAuditType, min=0)
@element(local_name='key_create_link', cls=EntityStateAuditType, min=0)
@element(local_name='key_wow64_64key', cls=EntityStateAuditType, min=0)
@element(local_name='key_wow64_32key', cls=EntityStateAuditType, min=0)
@element(local_name='key_wow64_res', cls=EntityStateAuditType, min=0)
@element(local_name='windows_view', cls=scap.model.oval_5.defs.EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
        ],
    }
