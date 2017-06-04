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
from scap.model.oval.oval_5_3 import *
from scap.model.oval.oval_5_3.defs import *

logger = logging.getLogger(__name__)
class SetElement(Model):
    MODEL_MAP = {
        'tag_name': 'set',
        'elements': [
            {'tag_name': 'set', 'class': 'SetElement', 'min': 0, 'max': 2},
            {'tag_name': 'object_reference', 'list': 'object_references', 'type': 'scap.model.oval.oval_5_3.ObjectIdPattern', 'min': 0, 'max': 2},
            {'tag_name': 'filter', 'class': 'FilterElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'set_operator': {'enum': SET_OPERATOR_ENUMERATION, 'default': 'UNION'},
        }
    }
    # TODO: either set element or object_reference (+ optional filter)
