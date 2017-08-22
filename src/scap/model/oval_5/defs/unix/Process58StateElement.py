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

from .StateType import StateType
from .EntityStateCapabilityType import EntityStateCapabilityType
from ..EntityStateType import EntityStateType

logger = logging.getLogger(__name__)

@element(local_name='command_line', cls=EntityStateType, min=0, max=1)
@element(local_name='exec_time', cls=EntityStateType, min=0, max=1)
@element(local_name='pid', cls=EntityStateType, min=0, max=1)
@element(local_name='ppid', cls=EntityStateType, min=0, max=1)
@element(local_name='priority', cls=EntityStateType, min=0, max=1)
@element(local_name='ruid', cls=EntityStateType, min=0, max=1)
@element(local_name='scheduling_class', cls=EntityStateType, min=0, max=1)
@element(local_name='start_time', cls=EntityStateType, min=0, max=1)
@element(local_name='tty', cls=EntityStateType, min=0, max=1)
@element(local_name='user_id', cls=EntityStateType, min=0, max=1)
@element(local_name='exec_shield', cls=EntityStateType, min=0, max=1)
@element(local_name='loginuid', cls=EntityStateType, min=0, max=1)
@element(local_name='posix_capability', cls=EntityStateCapabilityType, min=0, max=1)
@element(local_name='selinux_domain_label', cls=EntityStateType, min=0, max=1)
@element(local_name='session_id', cls=EntityStateType, min=0, max=1)
class Process58StateElement(StateType):
    pass
