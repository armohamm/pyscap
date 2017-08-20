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

@attribute(None, 'start_time', type='DateTimeType')
@attribute(None, 'end_time', type='DateTimeType')
@element(None, 'title', cls='TextType', min=0, max=1)
@element(None, 'questionnaire_results', cls='QuestionnaireResultsType', min=0, max=1)
@element(None, 'test_action_results', cls='TestActionResultsType', min=0, max=1)
@element(None, 'question_results', cls='QuestionResultsType', min=0, max=1)
@element(None, 'artifact_results', cls='ArtifactResultsType', min=0, max=1)
@element(None, 'targets', cls='TargetsType', min=0, max=1)
class ResultsType(Model):
    pass
