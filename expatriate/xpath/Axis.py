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
    ns = []
    while(node.parent is not None):
        ns.append(node.parent)
        node = node.parent
    return ns

def a_ancestor_or_self(node):
    ns = [node]
    ns.extend(a_ancestor(node))
    return ns

def a_attribute(node):
    if hasattr(node, 'attribute_nodes'):
        return list(node.attribute_nodes.values())
    else:
        return []

def a_child(node):
    if hasattr(node, 'children'):
        return node.children.copy()
    else:
        return []

def a_descendant(node):
    if not hasattr(node, 'children') or len(node.children) == 0:
        logger.debug(str(node) + ' has no children')
        return []
    else:
        ns = []
        for n in node.children:
            ns.append(n)
            ns.extend(a_descendant(n))
        return ns

def a_descendant_or_self(node):
    ns = [node]
    ns.extend(a_descendant(node))
    return ns

def a_namespace(node):
    if hasattr(node, 'namespace_nodes'):
        return list(node.namespace_nodes.values())
    else:
        return []

def a_parent(node):
    if node.parent is not None:
        return [node.parent]
    else:
        return []

def a_following_sibling(node):
    from ..Attribute import Attribute
    from ..Namespace import Namespace
    if isinstance(node, Attribute) \
    or isinstance(node, Namespace) \
    or node.parent is None:
        return []

    ns = []
    # figure out our index then go through children > our index
    node_i = node.parent.children.index(node)
    for i in range(node_i + 1, len(node.parent.children)):
        ns.append(node.parent.children[i])
    return ns

def a_following(node):
    from ..Attribute import Attribute
    from ..Namespace import Namespace
    if isinstance(node, Attribute) \
    or isinstance(node, Namespace):
        return []

    ns = []
    while node is not None:
        ns.extend(a_following_sibling(node))
        node = node.parent
    return ns

def a_preceding_sibling(node):
    from ..Attribute import Attribute
    from ..Namespace import Namespace
    if isinstance(node, Attribute) \
    or isinstance(node, Namespace) \
    or node.parent is None:
        return []

    ns = []
    # figure out our index then go through children < our index
    node_i = node.parent.children.index(node)
    for i in range(node_i - 1, -1, -1):
        logger.debug('Appending sibling ' + str(i) + ' of ' + str(node))
        ns.append(node.parent.children[i])
    return ns

def a_preceding(node):
    from ..Attribute import Attribute
    from ..Namespace import Namespace
    if isinstance(node, Attribute) \
    or isinstance(node, Namespace):
        return []

    ns = []
    while node is not None:
        logger.debug('Extending nodeset with ' + str(node) + ' preceding siblings')
        ns.extend(a_preceding_sibling(node))
        if node.parent is not None:
            logger.debug('Appending parent of ' + str(node) + ': ' + str(node.parent))
            ns.append(node.parent)
        node = node.parent
    return ns

logger = logging.getLogger(__name__)
class Axis(object):
    AXES = {
        'ancestor': a_ancestor,
        'ancestor-or-self': a_ancestor_or_self,
        'attribute': a_attribute,
        'child': a_child,
        'descendant': a_descendant,
        'descendant-or-self': a_descendant_or_self,
        'following': a_following,
        'following-sibling': a_following_sibling,
        'namespace': a_namespace,
        'parent': a_parent,
        'preceding': a_preceding,
        'preceding-sibling': a_preceding_sibling,
        'self': lambda node: [node],
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
                if c.evaluate(node, i+1, len(nodeset), variables):
                    logger.debug(str(node) + ' passed ' + str(c))
                    ns.append(node)
                else:
                    logger.debug(str(node) + ' failed ' + str(c))
            nodeset = ns

        return nodeset

    def __str__(self):
        return 'Axis ' + hex(id(self)) + ' ' + self.name + ': ' + str([str(x) for x in self.children])
