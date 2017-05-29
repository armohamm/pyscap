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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class VolumeStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'volume_state',
        'elements': [
            {'tag_name': 'rootpath', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'file_system', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'name', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'drive_type', 'class': 'EntityStateDriveTypeType', 'min': 0},
            {'tag_name': 'volume_max_component_length', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'serial_number', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'file_case_sensitive_search', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_case_preserved_names', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_unicode_on_disk', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_persistent_acls', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_file_compression', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_volume_quotas', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_sparse_files', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_reparse_points', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_remote_storage', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_volume_is_compressed', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_object_ids', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_encryption', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_named_streams', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_read_only_volume', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_sequential_write_once', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_transactions', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_hard_links', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_extended_attributes', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_open_by_file_id', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_supports_usn_journal', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
        ],
    }
