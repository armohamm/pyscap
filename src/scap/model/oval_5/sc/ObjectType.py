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
from scap.model.xs.NonNegativeIntegerType import NonNegativeIntegerType
from scap.model.xs.StringType import StringType

from ..MessageType import MessageType
from ..ObjectIdPattern import ObjectIdPattern

from .ReferenceType import ReferenceType
from .VariableValueType import VariableValueType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=ObjectIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='variable_instance', type=NonNegativeIntegerType, default=1)
@attribute(local_name='comment', type=StringType)
@attribute(local_name='flag', enum=[ 'error', 'complete', 'incomplete', 'does not exist', 'not collected', 'not applicable', ], required=True)
@element(local_name='message', list='messages', cls=MessageType, min=0, max=None)
@element(local_name='variable_value', list='variable_values', cls=VariableValueType, min=0, max=None)
@element(local_name='reference', list='references', cls=ReferenceType, min=0, max=None)
class ObjectType(Model):
    pass
