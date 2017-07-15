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

logger = logging.getLogger(__name__)

class DuplicateNamespaceException(Exception):
    pass

class UnknownNamespaceException(Exception):
    pass

class Element(Node):
    def __init__(self, parent, name, attributes):
        super(Element, self).__init__(parent)

        self.name = name
        # TODO parse out namespace

        self.attributes = attributes
        # TODO parse out namespace

        self.children = []

        if isinstance(self.parent, Element):
            self.namespaces = self.parent.namespaces.copy()
        else:
            # Document
            self.namespaces = {'xml': 'http://www.w3.org/XML/1998/namespace'}

        # check for a default namespace
        if 'xmlns' in self.attributes:
            self.namespaces[None] = self.attributes['xmlns']

        # check for prefix namespaces
        for k in self.attributes:
            if k.startswith('xmlns:'):
                prefix = k.partition(':')[2]
                if prefix in self.namespaces:
                    raise DuplicateNamespaceException('Prefix ' + prefix + ' has already been used but is being redefined')
                self.namespaces[prefix] = self.attributes[k]
                logger.debug('Added prefix ' + prefix + ' for ' + self.attributes[k])

        # check name for prefix
        if ':' in name:
            prefix = name.partition(':')[0]
            if prefix not in self.namespaces:
                raise UnknownNamespaceException('Unable to map element name prefix ' + prefix + ' to namespace')

        # check attributes for prefix
        for k in self.attributes:
            if not k.startswith('xmlns:') and ':' in k:
                prefix = k.partition(':')[0]
                if prefix not in self.namespaces:
                    raise UnknownNamespaceException('Unable to map attribute prefix ' + prefix + ' to namespace')

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
