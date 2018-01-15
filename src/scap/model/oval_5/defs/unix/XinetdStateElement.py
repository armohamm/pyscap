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

from .EntityStateXinetdTypeStatusType import EntityStateXinetdTypeStatusType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='protocol', cls=EntityStateType, min=0, max=1)
@element(local_name='service_name', cls=EntityStateType, min=0, max=1)
@element(local_name='flags', cls=EntityStateType, min=0, max=1)
@element(local_name='no_access', cls=EntityStateType, min=0, max=1)
@element(local_name='only_from', cls=EntityStateType, min=0, max=1)
@element(local_name='port', cls=EntityStateType, min=0, max=1)
@element(local_name='server', cls=EntityStateType, min=0, max=1)
@element(local_name='server_arguments', cls=EntityStateType, min=0, max=1)
@element(local_name='socket_type', cls=EntityStateType, min=0, max=1)
@element(local_name='type', cls=EntityStateXinetdTypeStatusType, min=0, max=1)
@element(local_name='user', cls=EntityStateType, min=0, max=1)
@element(local_name='wait', cls=EntityStateType, min=0, max=1)
@element(local_name='disabled', cls=EntityStateType, min=0, max=1)
class XinetdStateElement(StateType):
    pass
