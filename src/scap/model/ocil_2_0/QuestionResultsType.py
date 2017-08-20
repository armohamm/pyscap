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

logger = logging.getLogger(__name__)

@element(local_name='boolean_question_result', list='question_results', cls='BooleanQuestionResultType', min=0, max=None)
@element(local_name='choice_question_result', list='question_results', cls='ChoiceQuestionResultType', min=0, max=None)
@element(local_name='numeric_question_result', list='question_results', cls='NumericQuestionResultType', min=0, max=None)
@element(local_name='string_question_result', list='question_results', cls='StringQuestionResultType', min=0, max=None)
class QuestionResultsType(Model):
    # TODO at least one question_results
    pass
