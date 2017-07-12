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

class DuplicateNamespaceException(Exception):
    pass

class UnknownNamespaceException(Exception):
    pass

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

        # self._parser.StartNamespaceDeclHandler = lambda prefix, uri: self._start_namespace_handler(prefix, uri)
        # self._parser.EndNamespaceDeclHandler = lambda prefix: self._end_namespace_handler(prefix)

        self._parser.CommentHandler = lambda data: self._comment_handler(data)

        self._parser.StartCdataSectionHandler = lambda: self._start_cdata_section_handler()
        self._parser.EndCdataSectionHandler = lambda: self._end_cdata_section_handler()

        self._parser.DefaultHandlerExpand = lambda data: self._default_handler_expand(data)

        self._parser.NotStandaloneHandler = lambda data: self._not_standalone_handler(data)

        self._parser.ExternalEntityRefHandler = lambda context, base, systemId, publicId: self._external_entity_ref_handler(context, base, systemId, publicId)

    def parse(self, data, isfinal=True):
        logger.debug('Parsing data: ' + str(data))
        self._parser.Parse(data, isfinal)

        # TODO check that we're the only thing left on the stack when isfinal

    def parse_file(self, file_):
        logger.debug('Parsing file: ' + str(file_))
        self._parser.ParseFile(file_)

        # TODO check that we're the only thing left on the stack when isfinal

    def _add_to_current_element(self, item):
        logger.debug('_add_to_current_element: ' + str(item) + ' to children of ' + str(self._stack[-1]))

        self._stack[-1].children.append(item)
        item.parent = self._stack[-1]

    def _xml_decl_handler(self, version, encoding, standalone):
        logger.debug('_xml_decl_handler version: ' + str(version) + ' encoding: ' + str(encoding) + ' standalone: ' + str(standalone))
        self.version = version
        self.encoding = encoding
        self.standalone = standalone

    def _start_doctype_decl_handler(self, doctypeName, systemId, publicId, has_internal_subset):
        logger.debug('_start_doctype_decl_handler doctypeName: ' + str(doctypeName) + ' systemId: ' + str(systemId) + ' publicId: ' + str(publicId) + ' has_internal_subset: ' + str(has_internal_subset))

    def _end_doctype_decl_handler(self):
        logger.debug('_end_doctype_decl_handler')

    def _element_decl_handler(self, name, model):
        logger.debug('_element_decl_handler doctypeName: ' + str(name) + ' model: ' + str(model))

    def _attlist_decl_handler(self, elname, attname, type_, default, required):
        logger.debug('_attlist_decl_handler elname: ' + str(elname) + ' attname: ' + str(attname) + ' type_: ' + str(type_) + ' default: ' + str(default) + ' required: ' + str(required))

    def _start_element_handler(self, name, attributes):
        logger.debug('_start_element_handler elname: ' + str(name) + ' attname: ' + str(name) + ' attributes: ' + str(attributes))
        el = Element(name, attributes)

        # check for a default namespace
        if 'xmlns' in el.attributes:
            el.namespaces[None] = el.attributes['xmlns']
        # check for prefix namespaces
        for k in el.attributes:
            if k.startswith('xmlns:'):
                prefix = k.partition(':')[2]
                el.namespaces[prefix] = el.attributes[k]
                if prefix in self._namespaces:
                    raise DuplicateNamespaceException('Prefix ' + prefix + ' has already been used but is being redefined')
                self._namespaces[prefix] = el.attributes[k]
                logger.debug('Added prefix ' + prefix + ' for ' + el.attributes[k])

        # check name for prefix
        if ':' in name:
            prefix = name.partition(':')[0]
            if prefix not in self._namespaces:
                raise UnknownNamespaceException('Unable to map element name prefix ' + prefix + ' to namespace')
        # check attributes for prefix
        for k in el.attributes:
            if not k.startswith('xmlns:') and ':' in k:
                prefix = k.partition(':')[0]
                if prefix not in self._namespaces:
                    raise UnknownNamespaceException('Unable to map attribute prefix ' + prefix + ' to namespace')

        self._add_to_current_element(el)
        self._stack.append(el)

    def _end_element_handler(self, name):
        logger.debug('_end_element_handler name: ' + str(name))
        el = self._stack.pop()
        for k in el.attributes:
            if k.startswith('xmlns:'):
                prefix = k.partition(':')[2]
                del self._namespaces[prefix]
                logger.debug('Removed prefix ' + prefix)

    def _processing_instruction_handler(self, target, data):
        logger.debug('_processing_instruction_handler target: ' + str(target) + ' data: ' + str(data))
        pi = ProcessingInstruction(target, data)
        self._add_to_current_element(pi)

    def _character_data_handler(self, data):
        logger.debug('_character_data_handler data: ' + str(data))
        if self.skip_whitespace and data.strip() == '':
            return

        char_data = CharacterData(data)
        self._add_to_current_element(char_data)

    def _entity_decl_handler(self, entityName, is_parameter_entity, value, base, systemId, publicId, notationName):
        logger.debug('_entity_decl_handler entityName: ' + str(entityName) + ' is_parameter_entity: ' + str(is_parameter_entity) + ' value: ' + str(value) + ' base: ' + str(base) + ' systemId: ' + str(systemId) + ' publicId: ' + str(publicId) + ' notationName: ' + str(notationName))

    def _notation_decl_handler(self, notationName, base, systemId, publicId):
        logger.debug('_notation_decl_handler notationName: ' + str(notationName) + ' base: ' + str(base) + ' systemId: ' + str(systemId) + ' publicId: ' + str(publicId))

    # def _start_namespace_handler(self, prefix, uri):
    #     logger.debug('_start_namespace_handler prefix: ' + str(prefix) + ' uri: ' + str(uri))
    #     self._namespaces[prefix] = url
    #
    # def _end_namespace_handler(self, prefix):
    #     logger.debug('_end_namespace_handler prefix: ' + str(prefix))
    #     self._stack[-1].namespaces[prefix] = self._namespaces[prefix]

    def _comment_handler(self, data):
        logger.debug('_comment_handler data: ' + str(data))
        c = Comment(data)
        self._add_to_current_element(c)

    def _start_cdata_section_handler(self):
        logger.debug('_start_cdata_section_handler')
        self._in_cdata = True

    def _end_cdata_section_handler(self):
        logger.debug('_end_cdata_section_handler')
        self._in_cdata = False

    def _default_handler_expand(self, data):
        logger.debug('_default_handler_expand data: ' + str(data))

    def _not_standalone_handler(self, data):
        logger.debug('_not_standalone_handler data: ' + str(data))

    def _external_entity_ref_handler(self, context, base, systemId, publicId):
        logger.debug('_external_entity_ref_handler context: ' + str(context) + ' base: ' + str(base) + ' systemId: ' + str(systemId) + ' publicId: ' + str(publicId))
