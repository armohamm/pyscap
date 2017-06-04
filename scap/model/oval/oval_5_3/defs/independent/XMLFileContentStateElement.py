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
from scap.model.oval.oval_5_3.defs.independent import *
from scap.model.oval.oval_5_3.defs.independent.StateType import StateType

logger = logging.getLogger(__name__)
class XMLFileContentStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'xmlfilecontent_state',
        'elements': [
            {'tag_name': 'path', 'class': 'scap.model.oval.oval_5_3.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'filename', 'class': 'scap.model.oval.oval_5_3.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'xpath', 'class': 'scap.model.oval.oval_5_3.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'value_of', 'class': 'scap.model.oval.oval_5_3.defs.EntityStateStringType', 'min': 0, 'max': 1},
        ],
    }
