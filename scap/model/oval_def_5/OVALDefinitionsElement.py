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
from scap.model.oval_5 import *
from scap.model.oval_def_5 import *

logger = logging.getLogger(__name__)
class OVALDefinitionsElement(Model):
    MODEL_MAP = {
        'tag_name' : 'oval_definitions',
        'elements': [
            # TODO one of the following exists
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-common-5', 'tag_name': 'generator', 'class': 'GeneratorType', 'min': 0},
            {'tag_name': 'generator', 'class': 'GeneratorType', 'min': 0},
            {'tag_name': 'definitions', 'class': 'DefinitionsType', 'min': 0, 'max': 1},
            {'tag_name': 'tests', 'class': 'TestsType', 'min': 0, 'max': 1},
            {'tag_name': 'objects', 'class': 'ObjectsType', 'min': 0, 'max': 1},
            {'tag_name': 'states', 'class': 'StatesType', 'min': 0, 'max': 1},
            {'tag_name': 'variables', 'class': 'VariablesType', 'min': 0, 'max': 1},
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
        ],
    }
