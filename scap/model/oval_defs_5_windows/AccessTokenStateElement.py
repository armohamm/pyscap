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
from scap.model.oval_defs_5_windows import *
from scap.model.oval_defs_5_windows.StateType import StateType

logger = logging.getLogger(__name__)

class AccessTokenStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'accesstoken_state',
        'elements': [
            {'tag_name': 'security_principle', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'seassignprimarytokenprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seauditprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sebackupprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sechangenotifyprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreateglobalprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatepagefileprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatepermanentprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatesymboliclinkprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatetokenprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedebugprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seenabledelegationprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seimpersonateprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreasebasepriorityprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreasequotaprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreaseworkingsetprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seloaddriverprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'selockmemoryprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'semachineaccountprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'semanagevolumeprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seprofilesingleprocessprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'serelabelprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seremoteshutdownprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'serestoreprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesecurityprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seshutdownprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesyncagentprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemenvironmentprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesyncagentprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemprofileprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemtimeprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setakeownershipprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setcbprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setimezoneprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seundockprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seunsolicitedinputprivilege', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sebatchlogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seinteractivelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'senetworklogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seremoteinteractivelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seservicelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenybatchLogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyinteractivelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenynetworklogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyremoteInteractivelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyservicelogonright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setrustedcredmanaccessnameright', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'min': 0},
        ],
    }
