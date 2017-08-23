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

logger = logging.getLogger(__name__)
class AccessTokenItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'security_principle', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seassignprimarytokenprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seauditprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sebackupprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sechangenotifyprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'secreateglobalprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'secreatepagefileprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'secreatepermanentprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'secreatesymboliclinkprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'secreatetokenprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedebugprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seenabledelegationprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seimpersonateprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seincreasebasepriorityprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seincreasequotaprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seincreaseworkingsetprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seloaddriverprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'selockmemoryprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'semachineaccountprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'semanagevolumeprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seprofilesingleprocessprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'serelabelprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seremoteshutdownprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'serestoreprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sesecurityprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seshutdownprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sesyncagentprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sesystemenvironmentprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sesystemprofileprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sesystemtimeprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'setakeownershipprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'setcbprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'setimezoneprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seundockprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seunsolicitedinputprivilege', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sebatchlogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seinteractivelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'senetworklogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seremoteinteractivelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'seservicelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedenybatchLogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedenyinteractivelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedenynetworklogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedenyremoteInteractivelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'sedenyservicelogonright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'setrustedcredmanaccessnameright', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
        ],
        'attributes': {
        },
    }
