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
class RegKeyEffectiveRights53StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'regkeyeffectiverights53_state',
        'elements': [
            {'tag_name': 'hive', 'class': 'EntityStateRegistryHiveType', 'min': 0},
            {'tag_name': 'key', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'trustee_sid', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'standard_delete', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'standard_read_control', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'standard_write_dac', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'standard_write_owner', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'standard_synchronize', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'access_system_security', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'generic_read', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'generic_write', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'generic_execute', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'generic_all', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_query_value', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_set_value', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_create_sub_key', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_enumerate_sub_keys', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_notify', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_create_link', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_wow64_64key', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_wow64_32key', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'key_wow64_res', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
