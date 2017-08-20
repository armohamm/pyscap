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

@element(None, 'generator', cls='GeneratorType', min=1, max=1)
@element(None, 'document', cls='DocumentType', min=0, max=1)
@element(None, 'questionnaires', cls='QuestionnairesType', min=1, max=1)
@element(None, 'test_actions', cls='TestActionsType', min=1, max=1)
@element(None, 'questions', cls='QuestionsType', min=1, max=1)
@element(None, 'artifacts', cls='ArtifactsType', min=0, max=1)
@element(None, 'variables', cls='VariablesType', min=0, max=1)
@element(None, 'results', cls='ResultsElement', min=0, max=1)
class OCILType(Model):
    pass
