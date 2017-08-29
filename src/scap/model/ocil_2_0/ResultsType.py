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
from scap.model.xs.DateTimeType import DateTimeType

from .ArtifactResultsType import ArtifactResultsType
from .QuestionResultsType import QuestionResultsType
from .QuestionnaireResultsType import QuestionnaireResultsType
from .TargetsType import TargetsType
from .TestActionResultsType import TestActionResultsType
from .TextType import TextType

logger = logging.getLogger(__name__)

@attribute(local_name='start_time', type=DateTimeType)
@attribute(local_name='end_time', type=DateTimeType)
@element(local_name='title', cls=TextType, min=0, max=1)
@element(local_name='questionnaire_results', cls=QuestionnaireResultsType, min=0, max=1)
@element(local_name='test_action_results', cls=TestActionResultsType, min=0, max=1)
@element(local_name='question_results', cls=QuestionResultsType, min=0, max=1)
@element(local_name='artifact_results', cls=ArtifactResultsType, min=0, max=1)
@element(local_name='targets', cls=TargetsType, min=0, max=1)
class ResultsType(Model):
    pass
