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

from .WhenBooleanElement import WhenBooleanElement
from .WhenChoiceElement import WhenChoiceElement
from .WhenPatternElement import WhenPatternElement
from .WhenRangeElement import WhenRangeElement

logger = logging.getLogger(__name__)

@element(local_name='when_pattern', list='expressions', cls=WhenPatternElement, min=0, max=None)
@element(local_name='when_choice', list='expressions', cls=WhenChoiceElement, min=0, max=None)
@element(local_name='when_range', list='expressions', cls=WhenRangeElement, min=0, max=None)
@element(local_name='when_boolean', list='expressions', cls=WhenBooleanElement, min=0, max=None)
class VariableSetType(Model):
    #TODO: at least one when_*
    pass
