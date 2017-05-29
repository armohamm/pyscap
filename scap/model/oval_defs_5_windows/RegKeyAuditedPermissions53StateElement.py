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

from scap.model.oval_common_5 import *
from scap.model.oval_defs_5 import *
from scap.model.oval_defs_5_windows import *
from scap.model.oval_defs_5_windows.StateType import StateType

logger = logging.getLogger(__name__)
class RegKeyAuditedPermissions53StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'regkeyauditedpermissions53_state',
        'elements': [
            {'tag_name': 'hive', 'class': 'EntityStateRegistryHiveType', 'min': 0},
            {'tag_name': 'key', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'trustee_sid', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'standard_delete', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'standard_read_control', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'standard_write_dac', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'standard_write_owner', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'standard_synchronize', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'access_system_security', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'generic_read', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'generic_write', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'generic_execute', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'generic_all', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_query_value', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_set_value', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_create_sub_key', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_enumerate_sub_keys', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_notify', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_create_link', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_wow64_64key', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_wow64_32key', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'key_wow64_res', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
