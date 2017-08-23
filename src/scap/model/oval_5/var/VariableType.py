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
from scap.model.decorators import *
from scap.model.oval_5 import SIMPLE_DATATYPE_ENUMERATION

logger = logging.getLogger(__name__)

class VariableType(Model):
    MODEL_MAP = {
        'elements': [
@element(local_name='value', list='values', type=anySimpleType, min=1, max=None)
@element(local_name='notes', cls=scap.model.oval_5.NotesType, min=0, max=1)
        ],
        'attributes': {
@attribute(local_name='id', type=scap.model.oval_5.VariableIdPattern, required=True)
@attribute(local_name='datatype', enum=SIMPLE_DATATYPE_ENUMERATION, required=True)
@attribute(local_name='comment', type=StringType, required=True)
        }
    }
