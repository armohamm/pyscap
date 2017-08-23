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
from scap.model.xs.BooleanType import BooleanType

from ..NonEmptyString import NonEmptyString
from ..TestIdPattern import TestIdPattern
from ..res.CriterionType import CriterionType as res_CriterionType

logger = logging.getLogger(__name__)

@attribute(local_name='applicability_check', type=BooleanType)
@attribute(local_name='test_ref', type=TestIdPattern, required=True)
@attribute(local_name='negate', type=BooleanType, default=False)
@attribute(local_name='comment', type=NonEmptyString)
class CriterionType(Model):
    def check(self, content, host, imports, export_names):
        # set up result
        res = res_CriterionType()
        res.applicability_check = self.applicability_check
        res.test_ref = self.test_ref
        res.negate = self.negate
        res.result = 'not evaluated'

        try:
            test = content.find_reference(self.test_ref)
            test_res = test.check(content, host, imports, export_names)

            res.version = test_res.version
            res.variable_instance = test_res.variable_instance
            res.result = test_res.result

            if self.negate:
                if res.result == 'true':
                    res.result = 'false'
                elif res.result == 'false':
                    res.result = 'true'
        except:
            res.version = 0

        return res
