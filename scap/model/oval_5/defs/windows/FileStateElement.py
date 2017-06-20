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
class FileStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'file_state',
        'elements': [
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'filename', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'owner', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'size', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'a_time', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'c_time', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'm_time', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'ms_checksum', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'version', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'type', 'class': 'EntityStateFileTypeType', 'min': 0},
            {'tag_name': 'development_class', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'company', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'internal_name', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'language', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'original_filename', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'product_name', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'product_version', 'class': 'EntityStateType', 'min': 0},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
