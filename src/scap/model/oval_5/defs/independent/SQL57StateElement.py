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
from scap.model.oval_5 import DATABASE_ENGINE_ENUMERATION

from ..EntityObjectType import EntityObjectType
from ..EntityStateType import EntityStateType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='engine', cls=EntityObjectType, min=0, value_enum=DATABASE_ENGINE_ENUMERATION)
@element(local_name='version', cls=EntityObjectType, min=0)
@element(local_name='connection_string', cls=EntityObjectType, min=0)
@element(local_name='sql', cls=EntityObjectType, min=0)
@element(local_name='result', cls=EntityStateType, min=0)
class SQL57StateElement(StateType):
    pass
