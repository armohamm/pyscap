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

logger = logging.getLogger(__name__)
class RootStep(Step):
    def __init__(self, root_element):
        self.children = []
        self._root_element = root_element

    def evaluate(self, context_node, context_position, context_size, variables):
        if len(self.children) != 1:
            raise SyntaxException('Root step should have 1 child')

        logger.debug('Initial nodeset: ' + str(nodeset))

        raise NotImplementedError('')

        logger.debug('Final nodeset: ' + str(nodeset))
        return nodeset

    def __str__(self):
        return 'Step ' + hex(id(self)) + ': ' + str(self.children)
