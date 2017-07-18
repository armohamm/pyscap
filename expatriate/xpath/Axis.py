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

from .NodeTest import NodeTest

def a_ancestor(node):
    pass

def a_self(node):
    return [node]

logger = logging.getLogger(__name__)
class Axis(object):
    AXES = {
        'ancestor': a_ancestor,
        'ancestor-or-self': None,
        'attribute': None,
        'child': None,
        'descendant': None,
        'descendant-or-self': None,
        'following': None,
        'following-sibling': None,
        'namespace': None,
        'parent': None,
        'preceding': None,
        'preceding-sibling': None,
        'self': a_self,
    }

    def __init__(self, name):
        self.name = name
        self.children = []

    def evaluate(self, context_node, context_position, context_size, variables):
        nodeset = Axis.AXES[self.name](context_node)
        logger.debug('Initial nodeset: ' + str(nodeset))

        if len(self.children) < 1 or not isinstance(self.children[0], NodeTest):
            raise ValueError('Axis missing NodeTest')
            # TODO the rest need to be predicates

        for c in self.children:
            ns = []
            for i in range(len(nodeset)):
                node = nodeset[i]
                logger.debug('Testing ' + str(node) + ' against ' + str(c))
                if c.test(node, context_node, i+1, len(nodeset), variables):
                    logger.debug(str(node) + ' passed ' + str(c))
                    ns.append(node)
            nodeset = ns

        return nodeset

    def __str__(self):
        return 'Axis ' + hex(id(self)) + ' ' + self.name + ': ' + str([str(x) for x in self.children])
