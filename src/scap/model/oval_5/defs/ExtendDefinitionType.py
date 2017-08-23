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

from ..res.ExtendDefinitionType import ExtendDefinitionType as res_ExtendDefinitionType
from ..DefinitionIdPattern import DefinitionIdPattern
from ..NonEmptyString import NonEmptyString

logger = logging.getLogger(__name__)

@attribute(local_name='applicability_check', type=BooleanType)
@attribute(local_name='definition_ref', type=DefinitionIdPattern, required=True)
@attribute(local_name='negate', type=BooleanType, default=False)
@attribute(local_name='comment', type=NonEmptyString)
class ExtendDefinitionType(Model):
    def check(self, content, host, imports, export_names):
        # set up result
        res = res_ExtendDefinitionType()
        res.applicability_check = self.applicability_check
        res.definition_ref = self.definition_ref
        res.negate = self.negate
        res.result = 'not evaluated'

        try:
            defn = content.find_reference(self.definition_ref)
            def_res = defn.check(content, host, imports, export_names)

            res.version = def_res.version
            res.variable_instance = def_res.variable_instance
            res.result = def_res.result

            if self.negate:
                if res.result == 'true':
                    res.result = 'false'
                elif res.result == 'false':
                    res.result = 'true'
        except:
            res.version = 0

        return res
