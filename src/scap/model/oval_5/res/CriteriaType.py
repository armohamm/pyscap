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

from .. import OPERATOR_ENUMERATION
from .. import RESULT_ENUMERATION

logger = logging.getLogger(__name__)

@attribute(local_name='applicability_check', type=BooleanType)
@attribute(local_name='operator', enum=OPERATOR_ENUMERATION, required=True)
@attribute(local_name='negate', type=BooleanType, default=False)
@attribute(local_name='result', enum=RESULT_ENUMERATION, required=True)
@element(local_name='criteria', list='criteria', cls=('scap.model.oval_5.defs.CriteriaType', 'CriteriaType'), min=0, max=None)
@element(local_name='criterion', list='criteria', cls=('scap.model.oval_5.defs.CriterionType', 'CriterionType'), min=0, max=None)
@element(local_name='extend_definition', list='criteria', cls=('scap.model.oval_5.defs.ExtendDefinitionType', 'ExtendDefinitionType'), min=0, max=None)
class CriteriaType(Model):
    pass
