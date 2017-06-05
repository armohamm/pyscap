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
from scap.model.oval_5.defs import *

logger = logging.getLogger(__name__)
class OvalDefinitionsElement(Model):
    MODEL_MAP = {
        'tag_name' : 'oval_definitions',
        'elements': [
            # TODO one of the following exists
            {'tag_name': 'generator', 'class': 'scap.model.oval_5.GeneratorType', 'min': 1, 'max': 1},
            {'tag_name': 'definitions', 'class': 'DefinitionsType', 'in': '_definitions', 'min': 0, 'max': 1},
            {'tag_name': 'tests', 'class': 'TestsType', 'in': '_tests', 'min': 0, 'max': 1},
            {'tag_name': 'objects', 'class': 'ObjectsType', 'in': '_objects', 'min': 0, 'max': 1},
            {'tag_name': 'states', 'class': 'StatesType', 'in': '_states', 'min': 0, 'max': 1},
            {'tag_name': 'variables', 'class': 'VariablesType', 'in': '_variables', 'min': 0, 'max': 1},
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
        ],
    }

    def from_xml(self, parent, el):
        super(OvalDefinitionsElement, self).from_xml(parent, el)

        if self._definitions is not None:
            self.definitions = self._definitions.definitions
        if self._tests is not None:
            self.tests = self._tests.tests
        if self._objects is not None:
            self.objects = self._objects.objects
        if self._states is not None:
            self.states = self._states.states
        if self._variables is not None:
            self.variables = self._variables.variables
