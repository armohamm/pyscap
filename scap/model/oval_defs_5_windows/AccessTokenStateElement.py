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

class AccessTokenStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'accesstoken_state',
        'elements': [
            {'tag_name': 'security_principle', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'seassignprimarytokenprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seauditprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sebackupprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sechangenotifyprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreateglobalprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatepagefileprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatepermanentprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatesymboliclinkprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secreatetokenprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedebugprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seenabledelegationprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seimpersonateprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreasebasepriorityprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreasequotaprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seincreaseworkingsetprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seloaddriverprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'selockmemoryprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'semachineaccountprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'semanagevolumeprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seprofilesingleprocessprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'serelabelprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seremoteshutdownprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'serestoreprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesecurityprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seshutdownprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesyncagentprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemenvironmentprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesyncagentprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemprofileprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sesystemtimeprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setakeownershipprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setcbprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setimezoneprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seundockprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seunsolicitedinputprivilege', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sebatchlogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seinteractivelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'senetworklogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seremoteinteractivelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'seservicelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenybatchLogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyinteractivelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenynetworklogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyremoteInteractivelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'sedenyservicelogonright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'setrustedcredmanaccessnameright', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
        ],
    }
