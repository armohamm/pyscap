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

@element(None, 'boolean_question_test_action', list='test_actions', cls='BooleanQuestionTestActionElement', min=0, max=None)
@element(None, 'choice_question_test_action', list='test_actions', cls='ChoiceQuestionTestActionElement', min=0, max=None)
@element(None, 'numeric_question_test_action', list='test_actions', cls='NumericQuestionTestActionElement', min=0, max=None)
@element(None, 'string_question_test_action', list='test_actions', cls='StringQuestionTestActionElement', min=0, max=None)
class TestActionsType(Model):
    # TODO: min 1 of test_actions
    pass
