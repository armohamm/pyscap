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

from ..EntityStateType import EntityStateType

from .EntityStateDriveTypeType import EntityStateDriveTypeType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='rootpath', cls=EntityStateType, min=0)
@element(local_name='file_system', cls=EntityStateType, min=0)
@element(local_name='name', cls=EntityStateType, min=0)
@element(local_name='drive_type', cls=EntityStateDriveTypeType, min=0)
@element(local_name='volume_max_component_length', cls=EntityStateType, min=0)
@element(local_name='serial_number', cls=EntityStateType, min=0)
@element(local_name='file_case_sensitive_search', cls=EntityStateType, min=0)
@element(local_name='file_case_preserved_names', cls=EntityStateType, min=0)
@element(local_name='file_unicode_on_disk', cls=EntityStateType, min=0)
@element(local_name='file_persistent_acls', cls=EntityStateType, min=0)
@element(local_name='file_file_compression', cls=EntityStateType, min=0)
@element(local_name='file_volume_quotas', cls=EntityStateType, min=0)
@element(local_name='file_supports_sparse_files', cls=EntityStateType, min=0)
@element(local_name='file_supports_reparse_points', cls=EntityStateType, min=0)
@element(local_name='file_supports_remote_storage', cls=EntityStateType, min=0)
@element(local_name='file_volume_is_compressed', cls=EntityStateType, min=0)
@element(local_name='file_supports_object_ids', cls=EntityStateType, min=0)
@element(local_name='file_supports_encryption', cls=EntityStateType, min=0)
@element(local_name='file_named_streams', cls=EntityStateType, min=0)
@element(local_name='file_read_only_volume', cls=EntityStateType, min=0)
@element(local_name='file_sequential_write_once', cls=EntityStateType, min=0)
@element(local_name='file_supports_transactions', cls=EntityStateType, min=0)
@element(local_name='file_supports_hard_links', cls=EntityStateType, min=0)
@element(local_name='file_supports_extended_attributes', cls=EntityStateType, min=0)
@element(local_name='file_supports_open_by_file_id', cls=EntityStateType, min=0)
@element(local_name='file_supports_usn_journal', cls=EntityStateType, min=0)
class VolumeStateElement(StateType):
    pass
