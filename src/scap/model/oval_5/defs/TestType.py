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
from expatriate.model.xs.NonNegativeIntegerType import NonNegativeIntegerType

from .. import CHECK_ENUMERATION
from .. import EXISTENCE_ENUMERATION
from .. import EXISTENCE_RESULT_ENUMERATION
from .. import OPERATOR_ENUMERATION
from ..NonEmptyString import NonEmptyString
from ..TestIdPattern import TestIdPattern
from ..res.TestType import TestType as res_TestType

from .NotesType import NotesType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=TestIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='check_existence', enum=EXISTENCE_ENUMERATION, default='at_least_one_exists')
@attribute(local_name='check', enum=CHECK_ENUMERATION, required=True)
@attribute(local_name='state_operator', enum=OPERATOR_ENUMERATION, default='AND')
@attribute(local_name='comment', type=NonEmptyString) # required in the spec
@attribute(local_name='deprecated', type=BooleanType, default=False)
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', min=0, max=1)
@element(namespace='http://oval.mitre.org/XMLSchema/oval-common-5', local_name='notes', cls=NotesType, min=0, max=1)
class TestType(Model):
    def check(self, content, host, imports, export_names):
        # set up result
        res = res_TestType()
        res.test_id = self.id
        res.version = self.version
        res.check_existence = self.check_existence
        res.check = self.check
        res.state_operator = self.state_operator
        res.result = 'not evaluated'

        # TODO save to host for result generation

        if self.deprecated:
            logger.warning('Test ' + self.id + ' is deprecated, but being used')

        if self.object is None:
            return res

        items = host.collect_oval_items(self.object, content, imports, export_names)

        # Existence Check Evaluation
        counts = {x: 0 for x in EXISTENCE_RESULT_ENUMERATION}
        for item in items:
            # TODO add to res as TestedItemType
            # TODO save object & item link and item to host for sc generation

            counts[item.status] += 1

        ex, dne, e, nc = [counts[x] for x in EXISTENCE_RESULT_ENUMERATION]
        if self.check_existence == 'all_exist':
            res.result = existence_all_exist(ex, dne, e, nc)
        elif self.check_existence == 'any_exist':
            res.result = existence_any_exist(ex, dne, e, nc)
        elif self.check_existence == 'at_least_one_exists':
            res.result = existence_at_least_one_exists(ex, dne, e, nc)
        elif self.check_existence == 'none_exist':
            res.result = existence_none_exist(ex, dne, e, nc)
        elif self.check_existence == 'only_one_exists':
            res.result = existence_only_one_exists(ex, dne, e, nc)
        else:
            raise ValueError('Unknown check_existence value: ' + self.check_existence)

        if res.result != 'true':
            return res

        # Check Evaluation
        for item in items:
            # TODO compare to state(s)
            pass

        # TODO State Operator Evaluation

        return res
