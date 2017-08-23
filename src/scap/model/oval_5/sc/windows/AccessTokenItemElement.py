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

from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

class AccessTokenItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='security_principle', max=1, min=0, cls=EntityItemType)
@element(local_name='seassignprimarytokenprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seauditprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sebackupprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sechangenotifyprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='secreateglobalprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='secreatepagefileprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='secreatepermanentprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='secreatesymboliclinkprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='secreatetokenprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sedebugprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seenabledelegationprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seimpersonateprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seincreasebasepriorityprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seincreasequotaprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seincreaseworkingsetprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seloaddriverprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='selockmemoryprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='semachineaccountprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='semanagevolumeprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seprofilesingleprocessprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='serelabelprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seremoteshutdownprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='serestoreprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sesecurityprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seshutdownprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sesyncagentprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sesystemenvironmentprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sesystemprofileprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sesystemtimeprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='setakeownershipprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='setcbprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='setimezoneprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seundockprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='seunsolicitedinputprivilege', max=1, min=0, cls=EntityItemType)
@element(local_name='sebatchlogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='seinteractivelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='senetworklogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='seremoteinteractivelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='seservicelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='sedenybatchLogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='sedenyinteractivelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='sedenynetworklogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='sedenyremoteInteractivelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='sedenyservicelogonright', max=1, min=0, cls=EntityItemType)
@element(local_name='setrustedcredmanaccessnameright', max=1, min=0, cls=EntityItemType)
        ],
        'attributes': {
        },
    }
