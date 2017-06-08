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

from scap.model.xs import *
from scap.model.xs.AllElement import AllElement

logger = logging.getLogger(__name__)
class NamedGroupAllElement(AllElement):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
            'minOccurs': {'prohibited': True},
            'maxOccurs': {'prohibited': True},
            '*': {},
        }
    }
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_ALL_MODEL)
