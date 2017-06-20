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

from scap.model.oval_5.defs.unix.StateType import StateType

logger = logging.getLogger(__name__)
class PasswordStateElement(StateType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'username', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'password', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'user_id', 'class': 'EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'group_id', 'class': 'EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'gcos', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'home_dir', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'login_shell', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'last_login', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
        ],
        'attributes': {
        },
    }
