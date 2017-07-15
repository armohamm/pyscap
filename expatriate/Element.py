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

from .Node import Node
from .Attribute import Attribute
from .Namespace import Namespace

logger = logging.getLogger(__name__)

class DuplicateNamespaceException(Exception):
    pass

class UnknownNamespaceException(Exception):
    pass

class Element(Node):
    def __init__(self, parent, name, attributes):
        super(Element, self).__init__(parent)

        self.name = name

        self.attributes = attributes

        self.children = []

        if isinstance(self.parent, Element):
            self.namespaces = self.parent.namespaces.copy()
        else:
            # Document
            self.namespaces = {'xml': 'http://www.w3.org/XML/1998/namespace'}

        # check for a default namespace
        if 'xmlns' in self.attributes:
            if self.attributes['xmlns'] == '' and None in self.namespaces:
                del self.namespaces[None]
            else:
                self.namespaces[None] = self.attributes['xmlns']

        # check for prefix namespaces
        for k, v in self.attributes.items():
            if k.startswith('xmlns:'):
                prefix = k.partition(':')[2]
                if prefix in self.namespaces:
                    raise DuplicateNamespaceException('Prefix ' + prefix + ' has already been used but is being redefined')
                self.namespaces[prefix] = v
                logger.debug('Added prefix ' + prefix + ' for ' + v)

        # create nodes for each of the namespaces
        self.namespace_nodes = {}
        for prefix, uri in self.namespaces.items():
            self.namespace_nodes[prefix] = Namespace(self, prefix, uri)

        # parse the namespace & local part of the element name
        if ':' in name:
            n = name.partition(':')
            if n[0] not in self.namespaces:
                raise UnknownNamespaceException('Unable to map element name prefix ' + n[0] + ' to namespace')
            self.name_namespace = self.namespaces[n[0]]
            self.name_local = n[2]
        else:
            self.name_namespace = None
            self.name_local = name

        # check attributes for prefix
        self.attribute_locals = {}
        self.attribute_namespaces = {}
        self.attribute_nodes = {}
        for k, v in self.attributes.items():
            if k.startswith('xmlns:'):
                continue

            # parse the namespace & local part from each attribute
            if ':' in k:
                n = k.partition(':')
                if n[0] not in self.namespaces:
                    raise UnknownNamespaceException('Unable to map attribute prefix ' + n[0] + ' to namespace')
                self.attribute_namespaces[k] = self.namespaces[n[0]]
                self.attribute_locals[k] = n[2]
            else:
                self.attribute_namespaces[k] = None
                self.attribute_locals[k] = k

            self.attribute_nodes[k] = Attribute(self, self.attribute_namespaces[k], self.attribute_locals[k], v)


    def escape_attribute(self, text):
        return self.escape(text).replace('"', '&quot;')

    def produce(self):
        s = '<' + self.name
        for k, v in self.attributes.items():
            s += ' ' + k + '="' + self.escape_attribute(v) + '"'
        if len(self.children) == 0:
            s += '/>'
        else:
            s += '>'
            for c in self.children:
                s += c.produce()
            s += '</' + self.name + '>'

        return s

    def get_type(self):
        return 'element'
