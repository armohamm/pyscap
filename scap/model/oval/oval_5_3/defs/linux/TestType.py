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

from scap.model.oval.oval_5_3 import *
from scap.model.oval.oval_5_3.defs import *
from scap.model.oval.oval_5_3.defs.linux import *
from scap.model.oval.oval_5_3.defs.TestType import TestType as oval_def_5_TestType

logger = logging.getLogger(__name__)
class TestType(oval_def_5_TestType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'object', 'class': 'scap.model.oval.oval_5_3.defs.ObjectRefType'},
            {'tag_name': 'state', 'list': 'states', 'class': 'scap.model.oval.oval_5_3.defs.StateRefType', 'min': 0, 'max': None},
        ],
    }
