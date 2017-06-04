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
class ServiceEffectiveRightsStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'serviceeffectiverights_state',
        'elements': [
            {'tag_name': 'service_name', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'trustee_sid', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateStringType', 'min': 0},
            {'tag_name': 'standard_delete', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_read_control', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_write_dac', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_write_owner', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_read', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_write', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_execute', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_query_conf', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_change_conf', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_query_stat', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_enum_dependents', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_start', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_stop', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_pause', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_interrogate', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
            {'tag_name': 'service_user_defined', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityStateBoolType', 'min': 0},
        ],
    }
