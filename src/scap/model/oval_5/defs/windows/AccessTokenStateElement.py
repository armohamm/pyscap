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

from expatriate.model.decorators import *

from ..EntityStateType import EntityStateType

from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='security_principle', cls=EntityStateType, min=0)
@element(local_name='seassignprimarytokenprivilege', cls=EntityStateType, min=0)
@element(local_name='seauditprivilege', cls=EntityStateType, min=0)
@element(local_name='sebackupprivilege', cls=EntityStateType, min=0)
@element(local_name='sechangenotifyprivilege', cls=EntityStateType, min=0)
@element(local_name='secreateglobalprivilege', cls=EntityStateType, min=0)
@element(local_name='secreatepagefileprivilege', cls=EntityStateType, min=0)
@element(local_name='secreatepermanentprivilege', cls=EntityStateType, min=0)
@element(local_name='secreatesymboliclinkprivilege', cls=EntityStateType, min=0)
@element(local_name='secreatetokenprivilege', cls=EntityStateType, min=0)
@element(local_name='sedebugprivilege', cls=EntityStateType, min=0)
@element(local_name='seenabledelegationprivilege', cls=EntityStateType, min=0)
@element(local_name='seimpersonateprivilege', cls=EntityStateType, min=0)
@element(local_name='seincreasebasepriorityprivilege', cls=EntityStateType, min=0)
@element(local_name='seincreasequotaprivilege', cls=EntityStateType, min=0)
@element(local_name='seincreaseworkingsetprivilege', cls=EntityStateType, min=0)
@element(local_name='seloaddriverprivilege', cls=EntityStateType, min=0)
@element(local_name='selockmemoryprivilege', cls=EntityStateType, min=0)
@element(local_name='semachineaccountprivilege', cls=EntityStateType, min=0)
@element(local_name='semanagevolumeprivilege', cls=EntityStateType, min=0)
@element(local_name='seprofilesingleprocessprivilege', cls=EntityStateType, min=0)
@element(local_name='serelabelprivilege', cls=EntityStateType, min=0)
@element(local_name='seremoteshutdownprivilege', cls=EntityStateType, min=0)
@element(local_name='serestoreprivilege', cls=EntityStateType, min=0)
@element(local_name='sesecurityprivilege', cls=EntityStateType, min=0)
@element(local_name='seshutdownprivilege', cls=EntityStateType, min=0)
@element(local_name='sesyncagentprivilege', cls=EntityStateType, min=0)
@element(local_name='sesystemenvironmentprivilege', cls=EntityStateType, min=0)
@element(local_name='sesyncagentprivilege', cls=EntityStateType, min=0)
@element(local_name='sesystemprofileprivilege', cls=EntityStateType, min=0)
@element(local_name='sesystemtimeprivilege', cls=EntityStateType, min=0)
@element(local_name='setakeownershipprivilege', cls=EntityStateType, min=0)
@element(local_name='setcbprivilege', cls=EntityStateType, min=0)
@element(local_name='setimezoneprivilege', cls=EntityStateType, min=0)
@element(local_name='seundockprivilege', cls=EntityStateType, min=0)
@element(local_name='seunsolicitedinputprivilege', cls=EntityStateType, min=0)
@element(local_name='sebatchlogonright', cls=EntityStateType, min=0)
@element(local_name='seinteractivelogonright', cls=EntityStateType, min=0)
@element(local_name='senetworklogonright', cls=EntityStateType, min=0)
@element(local_name='seremoteinteractivelogonright', cls=EntityStateType, min=0)
@element(local_name='seservicelogonright', cls=EntityStateType, min=0)
@element(local_name='sedenybatchLogonright', cls=EntityStateType, min=0)
@element(local_name='sedenyinteractivelogonright', cls=EntityStateType, min=0)
@element(local_name='sedenynetworklogonright', cls=EntityStateType, min=0)
@element(local_name='sedenyremoteInteractivelogonright', cls=EntityStateType, min=0)
@element(local_name='sedenyservicelogonright', cls=EntityStateType, min=0)
@element(local_name='setrustedcredmanaccessnameright', cls=EntityStateType, min=0)
class AccessTokenStateElement(StateType):
    pass
