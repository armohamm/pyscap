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
from scap.model.oval.oval_5_11_1.defs_windows import *
from scap.model.oval.oval_5_11_1.defs_windows.StateType import StateType

logger = logging.getLogger(__name__)
class NtUserStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'ntuser_state',
        'elements': [
            {'tag_name': 'key', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'name', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'sid', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'username', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'account_type', 'class': 'EntityStateNTUserAccountTypeType', 'min': 0},
            {'tag_name': 'logged_on', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'enabled', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'date_modified', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateIntType', 'min': 0},
            {'tag_name': 'days_since_modified', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateIntType', 'min': 0},
            {'tag_name': 'filepath', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'last_write_time', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateIntType', 'min': 0},
            {'tag_name': 'type', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateRegistryTypeType', 'min': 0},
            {'tag_name': 'value', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateAnySimpleType', 'min': 0},
        ],
    }
