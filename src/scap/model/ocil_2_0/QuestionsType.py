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
from scap.Model import Model

from .BooleanQuestionElement import BooleanQuestionElement
from .ChoiceQuestionElement import ChoiceQuestionElement
from .NumericQuestionElement import NumericQuestionElement
from .StringQuestionElement import StringQuestionElement
from .ChoiceGroupType import ChoiceGroupType

logger = logging.getLogger(__name__)

@element(local_name='boolean_question', list='questions', cls=BooleanQuestionElement, min=0, max=None)
@element(local_name='choice_question', list='questions', cls=ChoiceQuestionElement, min=0, max=None)
@element(local_name='numeric_question', list='questions', cls=NumericQuestionElement, min=0, max=None)
@element(local_name='string_question', list='questions', cls=StringQuestionElement, min=0, max=None)
@element(local_name='choice_group', list='questions', cls=ChoiceGroupType, min=0, max=None)
class QuestionsType(Model):
    #TODO: questions contains at least one
    pass
