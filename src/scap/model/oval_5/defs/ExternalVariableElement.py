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

from .VariableType import VariableType
from .PossibleRestrictionType import PossibleRestrictionType
from .PossibleValueType import PossibleValueType

logger = logging.getLogger(__name__)

@element(local_name='possible_restriction', list='possible_restrictions', cls=PossibleRestrictionType, min=0, max=None)
@element(local_name='possible_value', list='possible_values', cls=PossibleValueType, min=0, max=None)
class ExternalVariableElement(VariableType):
    pass
