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
from scap.model.oval_defs_5_linux import *
from scap.model.oval_defs_5_linux.StateType import StateType

logger = logging.getLogger(__name__)
class RpmVerifyStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'rpmverify_state',
        'elements': [
            {'tag_name': 'name', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'filepath', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'size_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'mode_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'md5_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'device_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'link_mismatch', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'ownership_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'group_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'mtime_differs', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'capabilities_differ', 'class': 'EntityStateRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'configuration_file', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'documentation_file', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'ghost_file', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'license_file', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'readme_file', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0, 'max': 1},
        ],
    }
