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
from . import SEVERITY_ENUMERATION, ROLE_ENUMERATION
from scap.model.decorators import *

logger = logging.getLogger(__name__)

@attribute(local_name='idref', type=NCNameType, required=True)
@attribute(local_name='weight', type=Weight)
@attribute(local_name='selector', type=StringType)
@attribute(local_name='severity', enum=SEVERITY_ENUMERATION)
@attribute(local_name='role', enum=ROLE_ENUMERATION)
@element(local_name='remark', type=TextType, list='remarks', min=0, max=None)
class ProfileRefineRuleType(Model):
    def apply(self, item):
        from scap.model.xccdf_1_1.RuleType import RuleType
        if not isinstance(item, RuleType):
            raise ValueError('Trying to refine rule (' + self.idref + ') on an item of the wrong type: ' + item.__class__.__name__)

        if self.weight is not None:
            logger.debug('Refining rule ' + item.id + ' weight to ' + self.weight)
            item.weight = float(self.weight)

        if self.selector is not None:
            logger.debug('Refining rule ' + item.id + ' check to ' + self.selector)
            item.check_selector = self.selector

        if self.severity is not None:
            logger.debug('Refining rule ' + item.id + ' severity to ' + self.severity)
            item.severity = self.severity

        if self.role is not None:
            logger.debug('Refining rule ' + item.id + ' role to ' + self.role)
            item.role = self.role
