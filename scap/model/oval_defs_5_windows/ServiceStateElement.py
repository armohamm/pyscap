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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class ServiceStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'service_state',
        'elements': [
            {'tag_name': 'service_name', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'display_name', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'description', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'service_type', 'class': 'EntityStateServiceTypeType', 'min': 0},
            {'tag_name': 'start_type', 'class': 'EntityStateServiceStartTypeType', 'min': 0},
            {'tag_name': 'current_state', 'class': 'EntityStateServiceCurrentStateType', 'min': 0},
            {'tag_name': 'controls_accepted', 'class': 'EntityStateServiceControlsAcceptedType', 'min': 0},
            {'tag_name': 'start_name', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'pid', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'service_flag', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'dependencies', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
        ],
    }
