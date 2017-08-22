# Copyright 2016 Casey Jaymes

# Who knows what evil lurks in the hearts of men? The Shadow knows!

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

logger = logging.getLogger(__name__)

@element(local_name='username', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='password', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='chg_lst', cls=EntityStateType, min=0, max=1)
@element(local_name='chg_allow', cls=EntityStateType, min=0, max=1)
@element(local_name='chg_req', cls=EntityStateType, min=0, max=1)
@element(local_name='exp_warn', cls=EntityStateType, min=0, max=1)
@element(local_name='exp_inact', cls=EntityStateType, min=0, max=1)
@element(local_name='exp_date', cls=EntityStateType, min=0, max=1)
@element(local_name='flag', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='encrypt_method', cls=EntityStateEncryptMethodType, min=0, max=1)
class ShadowStateElement(StateType):
    pass

# The weed of crime bears bitter fruit. Crime does not pay...The Shadow knows!
