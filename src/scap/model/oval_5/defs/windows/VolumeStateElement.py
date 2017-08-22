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
class VolumeStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'volume_state',
        'elements': [
@element(local_name='rootpath', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_system', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='drive_type', cls=EntityStateDriveTypeType, min=0)
@element(local_name='volume_max_component_length', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='serial_number', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_case_sensitive_search', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_case_preserved_names', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_unicode_on_disk', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_persistent_acls', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_file_compression', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_volume_quotas', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_sparse_files', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_reparse_points', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_remote_storage', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_volume_is_compressed', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_object_ids', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_encryption', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_named_streams', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_read_only_volume', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_sequential_write_once', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_transactions', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_hard_links', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_extended_attributes', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_open_by_file_id', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='file_supports_usn_journal', cls=scap.model.oval_5.defs.EntityStateType, min=0)
        ],
    }
