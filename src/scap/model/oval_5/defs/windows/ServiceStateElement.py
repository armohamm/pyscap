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

from .EntityStateServiceControlsAcceptedType import EntityStateServiceControlsAcceptedType
from .EntityStateServiceCurrentStateType import EntityStateServiceCurrentStateType
from .EntityStateServiceStartTypeType import EntityStateServiceStartTypeType
from .EntityStateServiceTypeType import EntityStateServiceTypeType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='service_name', cls=EntityStateType, min=0)
@element(local_name='display_name', cls=EntityStateType, min=0)
@element(local_name='description', cls=EntityStateType, min=0)
@element(local_name='service_type', cls=EntityStateServiceTypeType, min=0)
@element(local_name='start_type', cls=EntityStateServiceStartTypeType, min=0)
@element(local_name='current_state', cls=EntityStateServiceCurrentStateType, min=0)
@element(local_name='controls_accepted', cls=EntityStateServiceControlsAcceptedType, min=0)
@element(local_name='start_name', cls=EntityStateType, min=0)
@element(local_name='path', cls=EntityStateType, min=0)
@element(local_name='pid', cls=EntityStateType, min=0)
@element(local_name='service_flag', cls=EntityStateType, min=0)
@element(local_name='dependencies', cls=EntityStateType, min=0)
class ServiceStateElement(StateType):
    pass
