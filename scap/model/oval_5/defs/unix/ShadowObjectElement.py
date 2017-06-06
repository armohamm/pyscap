# Copyright 2016 Casey Jaymes

# Who knows what evil lurks in the hearts of men? The Shadow knows!

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
from scap.model.oval_5.defs import *
from scap.model.oval_5.defs.unix import *
from scap.model.oval_5.defs.unix.ObjectType import ObjectType

logger = logging.getLogger(__name__)
class ShadowObjectElement(ObjectType):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'set', 'min': 0},
            {'tag_name': 'username', 'class': 'scap.model.oval_5.defs.EntityObjectStringType', 'min': 0},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'filter', 'min': 0, 'max': None},
        ],
        'attributes': {
        },
    }

# The weed of crime bears bitter fruit. Crime does not pay...The Shadow knows!
