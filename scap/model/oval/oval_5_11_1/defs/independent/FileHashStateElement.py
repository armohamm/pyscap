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

from scap.model.oval.oval_5_11_1 import *
from scap.model.oval.oval_5_11_1.defs import *
from scap.model.oval.oval_5_11_1.defs_independent import *
from scap.model.oval.oval_5_11_1.defs_independent.StateType import StateType

logger = logging.getLogger(__name__)
class FileHashStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'filehash_state',
        'elements': [
            {'tag_name': 'filepath', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'filename', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'md5', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'sha1', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
