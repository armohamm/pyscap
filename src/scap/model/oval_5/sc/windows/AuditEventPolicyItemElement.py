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

from .EntityItemAuditType import EntityItemAuditType

logger = logging.getLogger(__name__)

@element(local_name='account_logon', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='account_management', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='detailed_tracking', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='directory_service_access', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='logon', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='object_access', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='policy_change', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='privilege_use', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='system', max=1, min=0, cls=EntityItemAuditType)
class AuditEventPolicyItemElement(ItemType):
    pass
