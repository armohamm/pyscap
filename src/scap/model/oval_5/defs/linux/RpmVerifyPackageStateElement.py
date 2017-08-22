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
from .EpochElement import EpochElement
from .VersionElement import VersionElement
from .ReleaseElement import ReleaseElement
from ..EntityStateType import EntityStateType

logger = logging.getLogger(__name__)

@element(local_name='name', cls=EntityStateType, min=0, max=1)
@element(local_name='epoch', cls=EpochElement, min=0, max=1)
@element(local_name='version', cls=VersionElement, min=0, max=1)
@element(local_name='release', cls=ReleaseElement, min=0, max=1)
@element(local_name='arch', cls=EntityStateType, min=0, max=1)
@element(local_name='extended_name', cls=EntityStateType, min=0, max=1)
@element(local_name='dependency_check_passed', cls=EntityStateType, min=0, max=1)
@element(local_name='digest_check_passed', cls=EntityStateType, min=0, max=1)
@element(local_name='verification_script_successful', cls=EntityStateType, min=0, max=1)
@element(local_name='signature_check_passed', cls=EntityStateType, min=0, max=1)
class RpmVerifyPackageStateElement(StateType):
    pass
