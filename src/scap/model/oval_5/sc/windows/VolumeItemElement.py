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
from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class VolumeItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'rootpath', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_system', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'name', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'drive_type', 'max': 1, 'min': 0, 'class': 'EntityItemDriveTypeType'},
            {'tag_name': 'volume_max_component_length', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'serial_number', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_case_sensitive_search', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_case_preserved_names', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_unicode_on_disk', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_persistent_acls', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_file_compression', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_volume_quotas', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_sparse_files', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_reparse_points', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_remote_storage', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_volume_is_compressed', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_object_ids', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_encryption', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_named_streams', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_read_only_volume', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_sequential_write_once', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_transactions', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_hard_links', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_extended_attributes', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_open_by_file_id', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'file_supports_usn_journal', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
        ],
        'attributes': {
        },
    }
