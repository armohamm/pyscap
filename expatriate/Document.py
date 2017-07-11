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
import xml.parsers.expat

from .CharacterData import CharacterData
from .Comment import Comment
from .Element import Element
from .ProcessingInstruction import ProcessingInstruction

logger = logging.getLogger(__name__)

class Document(object):
    def __init__(self, encoding=None, skip_whitespace=True):
        self.version = None
        self.encoding = encoding
        self.standalone = None
        self.skip_whitespace = skip_whitespace

        self.children = []

        self._parser = xml.parsers.expat.ParserCreate(encoding=encoding)
        self._in_cdata = False
        self._stack = [self]
        self._namespaces = {}

        self._parser.XmlDeclHandler = lambda version, encoding, standalone: self._xml_decl_handler(version, encoding, standalone)

        self._parser.StartDoctypeDeclHandler = lambda doctypeName, systemId, publicId, has_internal_subset: self._start_doctype_decl_handler(doctypeName, systemId, publicId, has_internal_subset)
        self._parser.EndDoctypeDeclHandler = lambda : self._end_doctype_decl_handler()
        self._parser.ElementDeclHandler = lambda name, model: self._element_decl_handler(name, model)
        self._parser.AttlistDeclHandler = lambda elname, attname, type_, default, required: self._attlist_decl_handler(elname, attname, type_, default, required)

        self._parser.StartElementHandler = lambda name, attributes: self._start_element_handler(name, attributes)
        self._parser.EndElementHandler = lambda name: self._end_element_handler(name)

        self._parser.ProcessingInstructionHandler = lambda target, data: self._processing_instruction_handler(target, data)

        self._parser.CharacterDataHandler = lambda data: self._character_data_handler(data)

        self._parser.EntityDeclHandler = lambda entityName, is_parameter_entity, value, base, systemId, publicId, notationName: self._entity_decl_handler(entityName, is_parameter_entity, value, base, systemId, publicId, notationName)

        self._parser.NotationDeclHandler = lambda notationName, base, systemId, publicId: self._notation_decl_handler(notationName, base, systemId, publicId)

        self._parser.StartNamespaceDeclHandler = lambda prefix, uri: self._start_namespace_handler(prefix, uri)
        self._parser.EndNamespaceDeclHandler = lambda prefix: self._end_namespace_handler(prefix)

        self._parser.CommentHandler = lambda data: self._comment_handler(data)

        self._parser.StartCdataSectionHandler = lambda: self._start_cdata_section_handler()
        self._parser.EndCdataSectionHandler = lambda: self._end_cdata_section_handler()

        self._parser.DefaultHandlerExpand = lambda data: self._default_handler_expand(data)

        self._parser.NotStandaloneHandler = lambda data: self._not_standalone_handler(data)

        self._parser.ExternalEntityRefHandler = lambda context, base, systemId, publicId: self._external_entity_ref_handler(context, base, systemId, publicId)

    def parse(self, data, isfinal=True):
        self._parser.Parse(data, isfinal)

        # TODO check that we're the only thing left on the stack when isfinal

    def parse_file(self, file_):
        self._parser.ParseFile(file_)

        # TODO check that we're the only thing left on the stack when isfinal

    def _add_to_current_element(self, item):
        if len(self._stack) > 0:
            self._stack[-1].children.append(item)
            item.parent = self._stack[-1]

    def _xml_decl_handler(self, version, encoding, standalone):
        self.version = version
        self.encoding = encoding
        self.standalone = standalone

    def _start_doctype_decl_handler(self, doctypeName, systemId, publicId, has_internal_subset):
        pass

    def _end_doctype_decl_handler(self):
        pass

    def _element_decl_handler(self, name, model):
        pass

    def _attlist_decl_handler(self, elname, attname, type_, default, required):
        pass

    def _start_element_handler(self, name, attributes):
        el = Element(name, attributes)

        self._add_to_current_element(el)

        self._stack.append(el)

    def _end_element_handler(self, name):
        el = self._stack.pop()

    def _processing_instruction_handler(self, target, data):
        pi = ProcessingInstruction(target, data)
        self._add_to_current_element(pi)

    def _character_data_handler(self, data):
        if self.skip_whitespace and data.strip() == '':
            return
            
        char_data = CharacterData(data)
        self._add_to_current_element(char_data)

    def _entity_decl_handler(self, entityName, is_parameter_entity, value, base, systemId, publicId, notationName):
        pass

    def _notation_decl_handler(self, notationName, base, systemId, publicId):
        pass

    def _start_namespace_handler(self, prefix, uri):
        self._namespaces[prefix] = url

    def _end_namespace_handler(self, prefix):
        self._stack[-1].namespaces[prefix] = self._namespaces[prefix]

    def _comment_handler(self, data):
        c = Comment(data)
        self._add_to_current_element(c)

    def _start_cdata_section_handler(self):
        self._in_cdata = True

    def _end_cdata_section_handler(self):
        self._in_cdata = False

    def _default_handler_expand(self, data):
        pass

    def _not_standalone_handler(self, data):
        pass

    def _external_entity_ref_handler(self, context, base, systemId, publicId):
        pass
