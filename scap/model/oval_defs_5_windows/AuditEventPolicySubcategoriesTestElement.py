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

from scap.model.oval_common_5 import *
from scap.model.oval_defs_5 import *
from scap.model.oval_defs_5_windows import *
from scap.model.oval_defs_5.TestType import TestType

logger = logging.getLogger(__name__)

class AuditEventPolicySubcategoriesTestElement(TestType):
    MODEL_MAP = {
        'tag_name': 'auditeventpolicysubcategories_test',
        'elements': [
            {'tag_name': 'object', 'class': 'scap.model.oval_defs_5.ObjectRefType'},
            {'tag_name': 'state', 'list': 'states', 'class': 'scap.model.oval_defs_5.StateRefType', 'min': 0, 'max': None},
        ],
    }
