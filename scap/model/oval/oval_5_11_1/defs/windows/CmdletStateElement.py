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
from scap.model.oval.oval_5_11_1.defs.windows import *
from scap.model.oval.oval_5_11_1.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)

class CmdletStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'cmdlet_state',
        'elements': [
            {'tag_name': 'module_name', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'module_id', 'class': 'EntityStateGUIDType', 'min': 0, 'max': 1},
            {'tag_name': 'module_version', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateVersionType', 'min': 0, 'max': 1},
            {'tag_name': 'verb', 'class': 'EntityStateCmdletVerbType', 'min': 0, 'max': 1},
            {'tag_name': 'noun', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'parameters', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateRecordType', 'min': 0, 'max': 1},
            {'tag_name': 'select', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateRecordType', 'min': 0, 'max': 1},
            {'tag_name': 'value', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateRecordType', 'min': 0, 'max': 1},
        ],
    }
