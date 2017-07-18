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
import math

logger = logging.getLogger(__name__)
class Operator(object):
    def op_div(x,y):
        if y == 0:
            if x > 0:
                return math.inf
            else:
                return -math.inf
        else:
            return x // y

    OPERATORS = {
        '*': lambda x,y: x * y,
        # /
        # //
        # |
        '+': lambda x,y: x + y,
        '-': lambda x,y: x - y,
        '=': lambda x,y: x == y,
        '!=': lambda x,y: x != y,
        '<': lambda x,y: x < y,
        '<=': lambda x,y: x <= y,
        '>': lambda x,y: x > y,
        '>=': lambda x,y: x >= y,
        'and': lambda x,y: x and y,
        'or': lambda x,y: x or y,
        'mod': lambda x,y: math.fmod(x, y),
        'div': op_div,
        'negate': lambda x: - x,
    }
    def __init__(self, op):
        self.op = op
        self.children = []

    def evaluate(self, context_node, context_position, context_size, variables):
        if self.op == 'negate':
            return Operator.OPERATORS['negate'](self.children[0].evaluate(context_node, context_position, context_size, variables))
        else:
            return Operator.OPERATORS[self.op]( \
                self.children[0].evaluate(context_node, context_position, context_size, variables), \
                self.children[1].evaluate(context_node, context_position, context_size, variables) \
            )

    def __str__(self):
        return 'Operator ' + self.op + ' ' + hex(id(self)) + ': ' + str([str(x) for x in self.children])
