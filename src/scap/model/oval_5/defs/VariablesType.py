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

from scap.Model import Model
from scap.model.decorators import *

from .ConstantVariableElement import ConstantVariableElement
from .ExternalVariableElement import ExternalVariableElement
from .LocalVariableElement import LocalVariableElement

logger = logging.getLogger(__name__)

@element(local_name='external_variable', dict='variables', cls=ExternalVariableElement, min=0, max=None)
@element(local_name='constant_variable', dict='variables', cls=ConstantVariableElement, min=0, max=None)
@element(local_name='local_variable', dict='variables', cls=LocalVariableElement, min=0, max=None)
class VariablesType(Model):
    # TODO min 1 variables
    pass
