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
from ..NonEmptyString import NonEmptyString
from ..res.CriteriaType import CriteriaType as res_CriteriaType

from .CriterionType import CriterionType
from .ExtendDefinitionType import ExtendDefinitionType

logger = logging.getLogger(__name__)

@attribute(local_name='applicability_check', type=BooleanType)
@attribute(local_name='operator', enum=OPERATOR_ENUMERATION, default='AND')
@attribute(local_name='negate', type=BooleanType, default=False)
@attribute(local_name='comment', type=NonEmptyString)
@element(local_name='criteria', list='criteria', cls=('scap.model.oval_5.defs.CriteriaType', 'CriteriaType'), min=0, max=None)
@element(local_name='criterion', list='criteria', cls=CriterionType, min=0, max=None)
@element(local_name='extend_definition', list='criteria', cls=ExtendDefinitionType, min=0, max=None)
class CriteriaType(Model):
    # TODO len(criteria) >= 1

    def check(self, content, host, imports, export_names):
        # set up result
        res = res_CriteriaType()
        res.applicability_check = self.applicability_check
        res.operator = self.operator
        res.negate = self.negate
        res.result = 'not evaluated'

        if len(self.criteria) <= 0:
            raise ValueError('Criteria missing criteria/criterion/extend_definition')

        if len(self.criteria) == 1:
            res.criteria.append(self.criteria[0].check(content, host, imports, export_names))
            res.result = res.criteria[0].result
            return res

        counts = {x: 0 for x in RESULT_ENUMERATION}

        for crit in self.criteria:
            crit_res = crit.check(content, host, imports, export_names)
            res.criteria.append(crit_res)
            counts[crit_res.result] += 1

        t, f, e, u, ne, na = [counts[x] for x in RESULT_ENUMERATION]

        if self.operator == 'AND':
            res.result = operator_AND(t, f, e, u, ne, na)
        elif self.operator == 'ONE':
            res.result = operator_ONE(t, f, e, u, ne, na)
        elif self.operator == 'OR':
            res.result = operator_OR(t, f, e, u, ne, na)
        elif self.operator == 'XOR':
            res.result = operator_XOR(t, f, e, u, ne, na)
        else:
            raise ValueError('Unknown operator: ' + self.operator)

        if self.negate:
            if res.result == 'true':
                res.result = 'false'
            elif res.result == 'false':
                res.result = 'true'

        return res
