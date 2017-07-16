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

logger = logging.getLogger(__name__)
class Function(object):
    FUNCTIONS {
        # Node Set Functions
        'last': None,
        'position': : None,
        'count': None,
        'id': None,
        'local-name': None,
        'namespace-uri': None,
        'name': None,
        # String Functions
        'string': None,
        'concat': None,
        'starts-with': None,
        'contains': None,
        'substring-before': None,
        'substring-after': None,
        'substring': None,
        'string-length': None,
        'normalize-space': None,
        'translate': None,
        # Boolean Functions
        'boolean': None,
        'not': None,
        'true': None,
        'false': None,
        'lang': None,
        # Number Functions
        'number': None,
        'sum': None,
        'floor': None,
        'ceiling': None,
        'round': None,
    }
    def __init__(self, name):
        self.name = name
        self.children = []

    def evaluate(self):
        children = []
        for c in self.children:
            children.append(c.evaluate())
        return Function.FUNCTIONS[self.name](*children)

    def __str__(self):
        return 'Function ' + self.name + ': ' + str(self.children)
