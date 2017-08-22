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

class AccessTokenStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'accesstoken_state',
        'elements': [
@element(local_name='security_principle', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seassignprimarytokenprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seauditprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sebackupprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sechangenotifyprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='secreateglobalprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='secreatepagefileprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='secreatepermanentprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='secreatesymboliclinkprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='secreatetokenprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedebugprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seenabledelegationprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seimpersonateprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seincreasebasepriorityprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seincreasequotaprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seincreaseworkingsetprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seloaddriverprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='selockmemoryprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='semachineaccountprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='semanagevolumeprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seprofilesingleprocessprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='serelabelprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seremoteshutdownprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='serestoreprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesecurityprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seshutdownprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesyncagentprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesystemenvironmentprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesyncagentprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesystemprofileprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sesystemtimeprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='setakeownershipprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='setcbprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='setimezoneprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seundockprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seunsolicitedinputprivilege', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sebatchlogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seinteractivelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='senetworklogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seremoteinteractivelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='seservicelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedenybatchLogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedenyinteractivelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedenynetworklogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedenyremoteInteractivelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='sedenyservicelogonright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='setrustedcredmanaccessnameright', cls=scap.model.oval_5.defs.EntityStateType, min=0)
        ],
    }
