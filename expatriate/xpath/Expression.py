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
import re

from .Operator import Operator
from .Negate import Negate

logger = logging.getLogger(__name__)
class Expression(object):
    def __init__(self):
        self.children = []

    def evaluate(self):
        logger.debug('Evaluating expression ' + str(self))

        child_eval = []
        for c in self.children:
            child_eval.append(c.evaluate())
            logger.debug('Child ' + str(c) + ' evaluated to ' + str(child_eval[-1]))

        if len(child_eval) == 0:
            return ()
        elif len(child_eval) == 1:
            return child_eval[0]
        else:
            return tuple(child_eval)

    def __str__(self):
        return 'Expression ' + hex(id(self))
