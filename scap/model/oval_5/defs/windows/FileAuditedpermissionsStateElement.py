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
class FileAuditedpermissionsStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'fileauditedpermissions_state',
        'elements': [
            {'tag_name': 'path', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'filename', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'trustee_name', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
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
            {'tag_name': 'file_read_data', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_write_data', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_append_data', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_read_ea', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_write_ea', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_execute', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_delete_child', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_read_attributes', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_write_attributes', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
