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

from expatriate.model.Model import Model
from expatriate.model.decorators import *
from expatriate.model.xs.BooleanType import BooleanType

from .ReferenceType import ReferenceType
from .TextType import TextType

logger = logging.getLogger(__name__)

@attribute(local_name='is_done', type=BooleanType, default=False)
@attribute(local_name='is_required', type=BooleanType, default=True)
@element(local_name='description', cls=TextType, min=0, max=1)
@element(local_name='reference', list='references', cls=ReferenceType, min=0, max=None)
@element(local_name='step', list='steps', cls=('scap.model.ocil_2_0.StepType', 'StepType'), min=0, max=None)
class StepType(Model):
    pass
