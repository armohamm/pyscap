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
class DnsCacheStateElement(StateType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'protocol', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'service_name', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'server_program', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'server_arguments', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'endpoint_type', 'class': 'EntityStateEndpointType', 'min': 0, 'max': 1},
            {'tag_name': 'exec_as_user', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'wait_status', 'class': 'EntityStateWaitStatusType', 'min': 0, 'max': 1},
        ],
        'attributes': {
        },
    }
