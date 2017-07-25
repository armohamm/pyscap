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

from .Step import Step
from ..xpath import SyntaxException

logger = logging.getLogger(__name__)
class RootStep(Step):
    def __init__(self, root_element):
        self.children = []
        self._root_element = root_element

    def evaluate(self, context_node, context_position, context_size, variables):
        if len(self.children) == 0:
            logger.debug('Root step with no children: using ' + str(self._root_element) + ' as the result set')
            return [self._root_element]
        elif len(self.children) == 1:
            logger.debug('Root step with 1 child: ' + str(self.children[0]) + '; evaluating with root element ' + str(self._root_element) + ' as context node')
            ns = self.children[0].evaluate(self._root_element, 1, 1, variables)
            logger.debug(str(self) + ' resulting nodeset: ' + str(ns))
            return ns
        else:
            return super(RootStep, self).evaluate(context_node, context_position, context_size, variables)

    def __str__(self):
        return 'RootStep ' + hex(id(self)) + ': ' + str([str(x) for x in self.children])
