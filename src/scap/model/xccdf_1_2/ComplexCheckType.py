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
from scap.model.xccdf_1_2 import CHECK_OPERATOR_ENUMERATION

logger = logging.getLogger(__name__)

@attribute(local_name='operator', enum=CHECK_OPERATOR_ENUMERATION, required=True)
@attribute(local_name='negate', type=BooleanType, default=False)
@element(local_name='check', cls=CheckType, min=0, max=None, list='checks')
@element(local_name='complex-check', cls=ComplexCheckType, min=0, max=None, list='checks')
class ComplexCheckType(Model):
    def check(self, benchmark, host):
        if len(self.checks) < 1:
            raise ValueError('No sub-checks with complex-check')

        check_results = []
        for check in self.checks:
            check_results += check.check(benchmark, host)

        # apply the operator
        if self.operator == 'AND':
            result = AND([x['result'] for x in check_results])
        elif self.operator == 'OR':
            result = OR([x['result'] for x in check_results])
        else:
            raise ValueError('Unknown check operator: ' + self.operator)

        if self.negate:
            result = negate(result)

        return {
            'result': result,
            'messages': [
                MessageType(
                    tag_name='message',
                    value='Complex check result',
                    severity='info'
                ),
            ],
            'imports': {}
        }
