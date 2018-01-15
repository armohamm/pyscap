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

from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='admin_approval_mode', cls=EntityStateType, min=0)
@element(local_name='elevation_prompt_admin', cls=EntityStateType, min=0)
@element(local_name='elevation_prompt_standard', cls=EntityStateType, min=0)
@element(local_name='detect_installations', cls=EntityStateType, min=0)
@element(local_name='elevate_signed_executables', cls=EntityStateType, min=0)
@element(local_name='elevate_uiaccess', cls=EntityStateType, min=0)
@element(local_name='run_admins_aam', cls=EntityStateType, min=0)
@element(local_name='secure_desktop', cls=EntityStateType, min=0)
@element(local_name='virtualize_write_failures', cls=EntityStateType, min=0)
class UacStateElement(StateType):
    pass
