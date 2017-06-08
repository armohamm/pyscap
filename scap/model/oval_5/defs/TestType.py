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
from scap.model.oval_5 import *
from scap.model.oval_5.defs import *
from scap.model.oval_5.res.TestType import TestType as res_TestType

logger = logging.getLogger(__name__)

class TestType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-common-5', 'tag_name': 'notes', 'class': 'NotesType', 'min': 0, 'max': 1},
            #{'tag_name': 'object', 'class': 'ObjectRefType'},
            #{'tag_name': 'state', 'list': 'states', 'class': 'StateRefType', 'min': 0, 'max': None},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.TestIdPattern', 'required': True},
            'version': {'type': 'NonNegativeInteger', 'required': True},
            'check_existence': {'enum': EXISTENCE_ENUMERATION, 'default': 'at_least_one_exists'},
            'check': {'enum': CHECK_ENUMERATION, 'required': True},
            'state_operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString'}, # required in the spec
            'deprecated': {'type': 'Boolean', 'default': False},
        },
    }

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

        items = self.object.resolve(content, host, imports, export_names)

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
