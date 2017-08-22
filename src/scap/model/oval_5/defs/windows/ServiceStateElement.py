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

from scap.model.oval_5.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)
class ServiceStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'service_state',
        'elements': [
@element(local_name='service_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='display_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='description', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='service_type', cls=EntityStateServiceTypeType, min=0)
@element(local_name='start_type', cls=EntityStateServiceStartTypeType, min=0)
@element(local_name='current_state', cls=EntityStateServiceCurrentStateType, min=0)
@element(local_name='controls_accepted', cls=EntityStateServiceControlsAcceptedType, min=0)
@element(local_name='start_name', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='path', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='pid', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='service_flag', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='dependencies', cls=scap.model.oval_5.defs.EntityStateType, min=0)
        ],
    }
