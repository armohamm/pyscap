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
from scap.model.oval_5 import WINDOWS_VIEW_ENUMERATION

from .StateType import StateType
from ..EntityStateType import EntityStateType

logger = logging.getLogger(__name__)

@element(local_name='filepath', cls=EntityStateType, min=0)
@element(local_name='path', cls=EntityStateType, min=0)
@element(local_name='filename', cls=EntityStateType, min=0)
@element(local_name='owner', cls=EntityStateType, min=0)
@element(local_name='size', cls=EntityStateType, min=0)
@element(local_name='a_time', cls=EntityStateType, min=0)
@element(local_name='c_time', cls=EntityStateType, min=0)
@element(local_name='m_time', cls=EntityStateType, min=0)
@element(local_name='ms_checksum', cls=EntityStateType, min=0)
@element(local_name='version', cls=EntityStateType, min=0)
@element(local_name='type', cls=EntityStateFileTypeType, min=0)
@element(local_name='development_class', cls=EntityStateType, min=0)
@element(local_name='company', cls=EntityStateType, min=0)
@element(local_name='internal_name', cls=EntityStateType, min=0)
@element(local_name='language', cls=EntityStateType, min=0)
@element(local_name='original_filename', cls=EntityStateType, min=0)
@element(local_name='product_name', cls=EntityStateType, min=0)
@element(local_name='product_version', cls=EntityStateType, min=0)
@element(local_name='windows_view', cls=EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
class FileStateElement(StateType):
    pass
