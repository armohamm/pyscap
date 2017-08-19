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

from scap.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)

@attribute(None, 'operator', enum=['AND', 'OR'], required=True)
@attribute(None, 'negate', type='BooleanType', required=True)
@element(None, 'logical-test', list='logical_tests', class='LogicalTestType', min=0, max=None)
@element(None, 'fact-ref', list='fact_refs', class='FactRefType', min=0, max=None)
class LogicalTestType(Model):
    pass
