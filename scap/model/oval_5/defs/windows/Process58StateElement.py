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
class Process58StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'process58_state',
        'elements': [
            {'tag_name': 'command_line', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'pid', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'ppid', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'priority', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'image_path', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'current_dir', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'creation_time', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'dep_enabled', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'primary_window_text', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'name', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
        ],
    }
