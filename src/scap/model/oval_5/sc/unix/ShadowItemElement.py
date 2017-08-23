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

@element(local_name='username', min=0, cls=EntityItemType, max=1)
@element(local_name='password', min=0, cls=EntityItemType, max=1)
@element(local_name='chg_lst', min=0, cls=EntityItemType, max=1)
@element(local_name='chg_allow', min=0, cls=EntityItemType, max=1)
@element(local_name='chg_req', min=0, cls=EntityItemType, max=1)
@element(local_name='exp_warn', min=0, cls=EntityItemType, max=1)
@element(local_name='exp_inact', min=0, cls=EntityItemType, max=1)
@element(local_name='exp_date', min=0, cls=EntityItemType, max=1)
@element(local_name='flag', min=0, cls=EntityItemType, max=1)
@element(local_name='encrypt_method', min=0, cls=EntityItemEncryptMethodType, max=1)
class ShadowItemElement(ItemType):
    pass
