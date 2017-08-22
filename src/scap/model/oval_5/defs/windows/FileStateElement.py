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

from scap.model.oval_5 import WINDOWS_VIEW_ENUMERATION
from scap.model.oval_5.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)
class FileStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'file_state',
        'elements': [
@element(local_name='filepath', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='path', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='filename', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='owner', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='size', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='a_time', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='c_time', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='m_time', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='ms_checksum', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='version', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='type', cls=EntityStateFileTypeType, min=0)
@element(local_name='development_class', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='company', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='internal_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='language', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='original_filename', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='product_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='product_version', cls=EntityStateType, min=0)
@element(local_name='windows_view', cls=scap.model.oval_5.defs.EntityStateType, min=0, value_enum=WINDOWS_VIEW_ENUMERATION)
        ],
    }
