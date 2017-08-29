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

from ..EntityStateType import EntityStateType

from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='filepath', cls=EntityStateType, min=0)
@element(local_name='path', cls=EntityStateType, min=0, max=1)
@element(local_name='filename', cls=EntityStateType, min=0, max=1)
@element(local_name='type', cls=EntityStateType, min=0, max=1)
@element(local_name='group_id', cls=EntityStateType, min=0, max=1)
@element(local_name='user_id', cls=EntityStateType, min=0, max=1)
@element(local_name='a_time', cls=EntityStateType, min=0, max=1)
@element(local_name='c_time', cls=EntityStateType, min=0, max=1)
@element(local_name='m_time', cls=EntityStateType, min=0, max=1)
@element(local_name='size', cls=EntityStateType, min=0, max=1)
@element(local_name='suid', cls=EntityStateType, min=0, max=1)
@element(local_name='sgid', cls=EntityStateType, min=0, max=1)
@element(local_name='sticky', cls=EntityStateType, min=0, max=1)
@element(local_name='uread', cls=EntityStateType, min=0, max=1)
@element(local_name='uwrite', cls=EntityStateType, min=0, max=1)
@element(local_name='uexec', cls=EntityStateType, min=0, max=1)
@element(local_name='gread', cls=EntityStateType, min=0, max=1)
@element(local_name='gwrite', cls=EntityStateType, min=0, max=1)
@element(local_name='gexec', cls=EntityStateType, min=0, max=1)
@element(local_name='oread', cls=EntityStateType, min=0, max=1)
@element(local_name='owrite', cls=EntityStateType, min=0, max=1)
@element(local_name='oexec', cls=EntityStateType, min=0, max=1)
@element(local_name='has_extended_acl', cls=EntityStateType, min=0, max=1)
class FileStateElement(StateType):
    pass
