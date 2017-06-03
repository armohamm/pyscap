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

from scap.model.oval_5 import *
from scap.model.oval_def_5 import *
from scap.model.oval_def_5_independent import *
from scap.model.oval_def_5_independent.ObjectType import ObjectType

logger = logging.getLogger(__name__)
class TextFileContent54ObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'textfilecontent54_object',
        'elements': [
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'set', 'class': 'SetElement'},
            {'tag_name': 'behaviors', 'class': 'Textfilecontent54Behaviors', 'min': 0, 'max': 1},
            {'tag_name': 'filepath', 'class': 'scap.model.oval_def_5.EntityObjectStringType'},
            {'tag_name': 'path', 'class': 'scap.model.oval_def_5.EntityObjectStringType'},
            {'tag_name': 'filename', 'class': 'scap.model.oval_def_5.EntityObjectStringType'},
            {'tag_name': 'pattern', 'class': 'scap.model.oval_def_5.EntityObjectStringType'},
            {'tag_name': 'instance', 'class': 'scap.model.oval_def_5.EntityObjectIntType'},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'filter', 'class': 'FilterElement', 'min': 0, 'max': None},
        ],
    }
