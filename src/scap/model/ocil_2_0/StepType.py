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
from scap.model.xs.BooleanType import BooleanType
from scap.Model import Model

from .TextType import TextType
from .ReferenceType import ReferenceType

logger = logging.getLogger(__name__)

@attribute(local_name='is_done', type=BooleanType, default=False)
@attribute(local_name='is_required', type=BooleanType, default=True)
@element(local_name='description', cls=TextType, min=0, max=1)
@element(local_name='reference', list='references', cls=ReferenceType, min=0, max=None)
class StepType(Model):
    pass

# have to unwrap the decorator to prevent circular reference
element(local_name='step', list='steps', cls=StepType, min=0, max=None).__call__(StepType)
