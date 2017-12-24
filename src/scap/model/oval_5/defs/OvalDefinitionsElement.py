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

from ..GeneratorType import GeneratorType

from .DefinitionsType import DefinitionsType
from .ObjectsType import ObjectsType
from .StatesType import StatesType
from .TestsType import TestsType
from .VariablesType import VariablesType

logger = logging.getLogger(__name__)

@element(local_name='generator', cls=GeneratorType, min=1, max=1)
@element(local_name='definitions', cls=DefinitionsType, into='_definitions', min=0, max=1)
@element(local_name='tests', cls=TestsType, into='_tests', min=0, max=1)
@element(local_name='objects', cls=ObjectsType, into='_objects', min=0, max=1)
@element(local_name='states', cls=StatesType, into='_states', min=0, max=1)
@element(local_name='variables', cls=VariablesType, into='_variables', min=0, max=1)
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', min=0, max=1)
class OvalDefinitionsElement(Model):
    def _from_xml(self, parent, el):
        super(OvalDefinitionsElement, self)._from_xml(parent, el)

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
