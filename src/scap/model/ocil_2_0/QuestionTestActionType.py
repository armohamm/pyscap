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

from .ItemBaseType import ItemBaseType
from .QuestionIDPattern import QuestionIDPattern
from .QuestionTestActionIDPattern import QuestionTestActionIDPattern
from .TestActionConditionType import TestActionConditionType
from .TextType import TextType

logger = logging.getLogger(__name__)

@attribute(local_name='question_ref', type=QuestionIDPattern, required=True)
@attribute(local_name='id', type=QuestionTestActionIDPattern, required=True)
@element(local_name='title', cls=TextType, min=0, max=1)
@element(local_name='when_unknown', cls=TestActionConditionType, min=0)
@element(local_name='when_not_tested', cls=TestActionConditionType, min=0)
@element(local_name='when_not_applicable', cls=TestActionConditionType, min=0)
@element(local_name='when_error', cls=TestActionConditionType, min=0)
class QuestionTestActionType(ItemBaseType):
    pass
