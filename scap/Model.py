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
import importlib
import sys
import os.path
import xml.etree.ElementTree as ET

XML_SPACE_ENUMERATION = [
    'default',
    # The value "default" signals that applications' default white-space
    # processing modes are acceptable for this element
    'preserve',
    # the value "preserve" indicates the intent that applications preserve all
    # the white space
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class UnregisteredNamespaceException(Exception):
    pass

class TagMappingException(Exception):
    pass

class MinimumElementException(Exception):
    pass

class MaximumElementException(Exception):
    pass

class RequiredAttributeException(Exception):
    pass

class UnknownAttributeException(Exception):
    pass

class UnknownElementException(Exception):
    pass

class EnumerationException(Exception):
    pass

class ReferenceException(Exception):
    pass

class Model(object):
    MODEL_MAP = {
        'attributes': {
            '{http://www.w3.org/XML/1998/namespace}lang': {'type': 'String', 'in': '_xml_lang'},
            '{http://www.w3.org/XML/1998/namespace}space': {'enum': XML_SPACE_ENUMERATION, 'in': '_xml_space'},
            '{http://www.w3.org/XML/1998/namespace}base': {'type': 'AnyURI', 'in': '_xml_base'},
            '{http://www.w3.org/XML/1998/namespace}id': {'type': 'ID', 'in': '_xml_id'},
            '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': {'type': 'AnyURI', 'in': '_xsi_schemaLocation'},
        },
    }

    __model_mappings = {}

    __xmlns_to_package = {
        'http://www.w3.org/XML/1998/namespace': 'scap.model.xml',
        'http://www.w3.org/2001/XMLSchema': 'scap.model.xs',
        'http://www.w3.org/2001/XMLSchema-instance': 'scap.model.xsi',
    }
    __package_to_xmlns = {
        'scap.model.xml': 'http://www.w3.org/XML/1998/namespace',
        'scap.model.xs': 'http://www.w3.org/2001/XMLSchema',
        'scap.model.xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    }

    @staticmethod
    def register_namespace(model_package, xmlns):
        Model.__xmlns_to_package[xmlns] = model_package
        Model.__package_to_xmlns[model_package] = xmlns
        # TODO need to make sure model_package.split('.')[-1] is unique
        ET.register_namespace(model_package.split('.')[-1], xmlns)

    @staticmethod
    def unregister_namespace(model_package):
        try:
            xmlns = Model.__package_to_xmlns[model_package]
        except KeyError:
            raise UnregisteredNamespaceException('Unregistered namespace: ' + model_package)

        del Model.__package_to_xmlns[model_package]
        del Model.__xmlns_to_package[xmlns]

    @staticmethod
    def parse_tag(tag):
        # parse tag
        if tag.startswith('{'):
            xmlns, tag_name = tag[1:].split('}')
        else:
            return None, tag

        if xmlns not in Model.__xmlns_to_package:
            raise UnregisteredNamespaceException('Unregistered namespace: ' + xmlns + ', tag name: ' + tag_name)

        return xmlns, tag_name

    @staticmethod
    def package_to_xmlns(model_package):
        logger.debug('Looking for xml namespace for model package ' + model_package)
        if model_package not in Model.__package_to_xmlns:
            raise UnregisteredNamespaceException('Namespace ' + model_package + ' is not in registered namespaces')

        return Model.__package_to_xmlns[model_package]

    @staticmethod
    def xmlns_to_package(xmlns):
        logger.debug('Looking for model package for xml namespace ' + xmlns)
        if xmlns not in Model.__xmlns_to_package:
            raise UnregisteredNamespaceException('XML namespace ' + xmlns + ' is not in registered namespaces')

        return Model.__xmlns_to_package[xmlns]

    @staticmethod
    def map_tag_to_module_name(model_package, tag):
        pkg_mod = importlib.import_module(model_package)

        if not hasattr(pkg_mod, 'TAG_MAP'):
            raise TagMappingException(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + tag)
        if tag not in pkg_mod.TAG_MAP:
            raise TagMappingException(pkg_mod.__name__ + ' does not define mapping for ' + tag + ' tag')

        return pkg_mod.TAG_MAP[tag]

    @staticmethod
    def load(parent, child_el):
        xmlns, tag_name = Model.parse_tag(child_el.tag)

        # try to load the tag's module
        if parent is None:
            if xmlns is None:
                raise UnregisteredNamespaceException('Unable to determine namespace without fully qualified tag (' + child_el.tag + ') and parent model')

            model_package = Model.xmlns_to_package(xmlns)
            module_name = Model.map_tag_to_module_name(model_package, child_el.tag)
        else:
            if xmlns is None:
                model_package = parent.get_package()
                ns_any = '{' + parent.get_xmlns() + '}*'
                fq_tag = '{' + parent.get_xmlns() + '}' + tag_name
            else:
                model_package = Model.xmlns_to_package(xmlns)
                ns_any = '{' + xmlns + '}*'
                fq_tag = child_el.tag

            mmap = Model._get_model_map(parent.__class__)

            logger.debug('Checking ' + parent.__class__.__name__ + ' for tag ' + child_el.tag)
            module_name = None
            for name in [fq_tag, tag_name, ns_any, '*']:
                if name not in mmap['element_lookup']:
                    continue

                logger.debug(child_el.tag + ' matched ' + name + ' mapping in ' + parent.__class__.__name__)
                if name.endswith('*'):
                    module_name = Model.map_tag_to_module_name(model_package, child_el.tag)
                    break
                elif 'class' in mmap['element_lookup'][name]:
                    module_name = mmap['element_lookup'][name]['class']
                    break

            if module_name is None:
                raise TagMappingException(parent.__class__.__name__ + ' does not define mapping for ' + child_el.tag + ' tag; does not match any of ' + str([fq_tag, tag_name, ns_any, '*']))

        # qualify module name if needed
        if '.' not in module_name:
            model_module = model_package + '.' + module_name
        else:
            model_module = module_name

        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)
            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, module_name)
        inst = class_()
        inst.from_xml(parent, child_el)

        return inst

    @staticmethod
    def _get_model_map(model_class):
        fq_model_class_name = model_class.__module__ + '.' + model_class.__name__
        if fq_model_class_name not in Model.__model_mappings:
            at_map = {}
            el_map = {}
            el_order = []
            xmlns = None
            tag_name = None
            for class_ in model_class.__mro__:
                if class_ == object:
                    break

                if class_.__module__.startswith('collections.'):
                    # skip collection classes
                    continue

                fq_class_name = class_.__module__ + '.' + class_.__name__

                if not hasattr(class_, 'MODEL_MAP'):
                    raise TagMappingException('Class ' + fq_class_name + ' does not define MODEL_MAP')

                # overwrite the super class' ns & tag with what we've already loaded
                try:
                    if xmlns is None:
                        xmlns = class_.MODEL_MAP['xmlns']
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[xmlns] defined')
                    pass
                try:
                    if tag_name is None:
                        tag_name = class_.MODEL_MAP['tag_name']
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[tag_name] defined')
                    pass

                # update the super class' attribute map with subclass
                try:
                    super_atmap = class_.MODEL_MAP['attributes'].copy()
                    super_atmap.update(at_map)
                    at_map = super_atmap
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[attributes] defined')
                    pass

                # update the super class' element map with subclass
                try:
                    super_elmap = class_.MODEL_MAP['elements'].copy()
                    super_elmap.extend(el_map)
                    el_map = super_elmap
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[elements] defined')
                    pass

            if xmlns is None:
                # try to auto detect from module name
                xmlns = Model.package_to_xmlns(model_class.__module__.rpartition('.')[0])

            el_lookup = {}
            for element_def in el_map:
                if 'xmlns' not in element_def and element_def['tag_name'] == '*':
                    el_lookup['*'] = element_def
                elif 'xmlns' in element_def:
                    el_lookup['{' + element_def['xmlns'] + '}' + element_def['tag_name']] = element_def
                else:
                    # try using element's xmlns
                    el_lookup['{' + xmlns + '}' + element_def['tag_name']] = element_def

            Model.__model_mappings[fq_model_class_name] = {
                'xmlns': xmlns,
                'tag_name': tag_name,
                'attributes': at_map,
                'elements': el_map,
                'element_lookup': el_lookup,
            }

        return Model.__model_mappings[fq_model_class_name]

    @staticmethod
    def find_content(uri):
        # locate content & load it, returning the root Model
        if os.path.isfile(uri):
            try:
                return Model.load(None, ET.parse(uri).getroot())
            except:
                raise ReferenceException('Could not find content for: ' + uri)
        else:
            raise NotImplementedError('URI loading is not yet implemented')

        raise ReferenceException('Could not find content for: ' + uri)

    def __init__(self, value=None, tag_name=None):
        self.parent = None

        self._children = []

        self._references = {}

        if value is None:
            self.text = None
        else:
            self.text = value

        self.tail = None

        self.model_map = Model._get_model_map(self.__class__)

        if tag_name is not None:
            self.tag_name = tag_name

        self.tag_counts = {}

        # must have namespace for concrete classes
        if 'xmlns' not in self.model_map or self.model_map['xmlns'] is None:
            raise ValueError('No xmlns defined for ' + self.__class__.__name__ + ' & could not detect')

        # initialize attribute values
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xmlns, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')

            if 'default' in attr_map:
                value = attr_map['default']
                setattr(self, attr_name, value)
                logger.debug('Default of attribute ' + attr_name + ' = ' + str(value))
            else:
                setattr(self, attr_name, None)

        # initialize elements
        for element_def in self.model_map['elements']:
            if element_def['tag_name'].endswith('*'):
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = '_elements'

                if name not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + name + ' to []')
                    setattr(self, name, [])

            elif 'list' in element_def:
                # initialze the array if it doesn't exist
                if element_def['list'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + element_def['list'] + ' to []')
                    setattr(self, element_def['list'], [])

            elif 'dict' in element_def:
                # initialze the dict if it doesn't exist
                if element_def['dict'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + element_def['dict'] + ' to {}')
                    setattr(self, element_def['dict'], {})

            else:
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = element_def['tag_name'].replace('-', '_')

                if name not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + name + ' to None')
                    setattr(self, name, None)

    def get_package(self):
        return self.__module__.rpartition('.')[0]

    def __str__(self):
        s = self.__class__.__module__ + '.' + self.__class__.__name__
        if hasattr(self, 'id') and self.id is not None:
            s += ' id: ' + self.id
        elif hasattr(self, 'Id') and self.Id is not None:
            s += ' Id: ' + self.Id
        elif hasattr(self, 'name') and self.name is not None:
            s += ' name: ' + self.name
        else:
            s += ' # ' + str(id(self))

        return s

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

        if name == 'id':
            if self.parent is not None:
                self.parent._references[value] = self
        elif name == 'parent':
            if value is not None:
                value._children.append(self)

    def find_reference(self, ref):
        if ref in self._references:
            return self._references[ref]
        else:
            for c in self._children:
                try:
                    return c.find_reference(ref)
                except:
                    pass

        raise ReferenceException('Could not find reference ' + ref + ' within ' + str(self))

    def get_tag_name(self):
        if hasattr(self, 'tag_name'):
            return self.tag_name
        if 'tag_name' not in self.model_map or self.model_map['tag_name'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag_name')
        return self.model_map['tag_name']

    def get_xmlns(self):
        if 'xmlns' not in self.model_map or self.model_map['xmlns'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define namespace')
        return self.model_map['xmlns']

    def from_xml(self, parent, el):
        self.parent = parent

        logger.debug('Parsing ' + el.tag + ' element into ' + self.__class__.__module__ + '.' + self.__class__.__name__ + ' class')

        # save the tag_name
        xmlns, tag_name = Model.parse_tag(el.tag)

        # check that required attributes are defined
        for attrib in self.model_map['attributes']:
            if 'required' in self.model_map['attributes'][attrib] \
            and self.model_map['attributes'][attrib]['required'] \
            and attrib not in el.keys() \
            and 'default' not in self.model_map['attributes'][attrib]:
                raise RequiredAttributeException(el.tag + ' must define ' + attrib + ' attribute')

        for name, value in list(el.items()):
            self._parse_attribute(name, value)

        for sub_el in el:
            self._parse_element(sub_el)

        # check the element restrictions
        for element_def in self.model_map['elements']:
            if 'xmlns' not in element_def and element_def['tag_name'] == '*':
                tag = '*'
            elif 'xmlns' in element_def:
                tag = '{' + element_def['xmlns'] + '}' + element_def['tag_name']
            else:
                tag = '{' + self.get_xmlns() + '}' + element_def['tag_name']

            min_ = 1
            if 'dict' in element_def or 'list' in element_def or element_def['tag_name'] == '*':
                # dicts and lists default to no max
                max_ = None
            else:
                max_ = 1

            # if there's an explicit min/max definition, use that
            if 'min' in element_def:
                min_ = element_def['min']
            if 'max' in element_def:
                max_ = element_def['max']

            # check that we have the min & max of those elements
            if min_ != 0 and (tag not in self.tag_counts or self.tag_counts[tag] < min_):
                raise MinimumElementException(self.__class__.__name__ + ' must have at least ' + str(min_) + ' ' + tag + ' elements')

            if max_ is not None and tag in self.tag_counts and self.tag_counts[tag] > max_:
                raise MaximumElementException(self.__class__.__name__ + ' may have at most ' + str(max_) + ' ' + tag + ' elements')

        self.text = el.text

    def _load_type_class(self, type_):
        if '.' in type_:
            try:
                mod = importlib.import_module(type_)
            except ImportError:
                raise NotImplementedError('Type class ' + type_ + ' was not found')
        else:
            try:
                mod = importlib.import_module('scap.model.xs.' + type_)
            except ImportError:
                try:
                    mod = importlib.import_module(self.get_package() + '.' + type_)
                except ImportError:
                    raise NotImplementedError('Type class ' + type_ + ' not defined in scap.model.xs or local package (' + self.get_package() + ')')
        return getattr(mod, type_)

    def _parse_value_as_type(self, value, type_):
        class_ = self._load_type_class(type_)
        return class_().parse_value(value)

    def _produce_value_as_type(self, value, type_):
        class_ = self._load_type_class(type_)
        return class_().produce_value(value)

    def _parse_attribute(self, fq_attr_name, value):
        xmlns, attr_name = Model.parse_tag(fq_attr_name)

        if xmlns is None:
            ns_any = '{' + self.model_map['xmlns'] + '}*'
        else:
            ns_any = '{' + xmlns + '}*'

        for name in [fq_attr_name, attr_name, ns_any, '*']:
            if name not in self.model_map['attributes']:
                continue

            attr_map = self.model_map['attributes'][name]

            if 'enum' in attr_map and value not in attr_map['enum']:
                raise EnumerationException(name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))

            # convert value
            if 'type' in attr_map:
                logger.debug('Parsing ' + str(value) + ' as ' + attr_map['type'] + ' type')
                value = self._parse_value_as_type(value, attr_map['type'])

            if 'in' in attr_map:
                logger.debug('Setting attribute ' + attr_map['in'] + ' = ' + str(value))
                setattr(self, attr_map['in'], value)
            else:
                name = attr_name.replace('-', '_')
                logger.debug('Setting attribute ' + name + ' = ' + str(value))
                setattr(self, name, value)
            return

        # if we didn't find a match for the attribute, raise
        raise UnknownAttributeException('Unknown ' + str(self) + ' attribute ' + fq_attr_name + ' = ' + value)

    def _parse_element(self, el):
        xmlns, tag_name = Model.parse_tag(el.tag)

        if xmlns is None:
            ns_any = '{' + self.get_xmlns() + '}*'
            fq_tag = '{' + self.get_xmlns() + '}' + tag_name
        else:
            ns_any = '{' + xmlns + '}*'
            fq_tag = el.tag

        for tag in [fq_tag, tag_name, ns_any, '*']:
            # check both namespace + tag_name and just tag_name
            if tag not in self.model_map['element_lookup']:
                continue

            logger.debug('Tag ' + el.tag + ' matched ' + tag)
            element_def = self.model_map['element_lookup'][tag]

            if tag.endswith('*'):
                logger.debug(str(self) + ' parsing ' + tag + ' elements matching *')
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = '_elements'

                lst = getattr(self, name)

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'type' in element_def:
                    value = self._parse_value_as_type(el.text, element_def['type'])
                else:
                    value = Model.load(self, el)
                    value.tag_name = tag_name

                lst.append(value)
                logger.debug('Appended ' + str(value) + ' to ' + name)

            elif 'list' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements into ' + element_def['list'])
                lst = getattr(self, element_def['list'])

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'type' in element_def:
                    value = self._parse_value_as_type(el.text, element_def['type'])
                else:
                    value = Model.load(self, el)
                    value.tag_name = tag_name

                lst.append(value)
                logger.debug('Appended ' + str(value) + ' to ' + element_def['list'])

            elif 'dict' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements into ' + element_def['dict'])
                dic = getattr(self, element_def['dict'])

                # TODO: implement key_element as well
                if 'key' in element_def:
                    if element_def['key'] not in el.keys():
                        key = None
                    else:
                        key = el.get(element_def['key'])
                else:
                    if 'id' not in el.keys():
                        key = None
                    else:
                        key = el.get('id')

                # TODO: implement value_element? as well
                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not allowing nil value')
                elif 'value_attr' in element_def:
                    # try parsing from an attribute
                    if element_def['value_attr'] not in el.keys():
                        raise ValueError('Could not parse value from ' + el.tag + ' attribute ' + element_def['value_attr'])

                    if 'type' not in element_def:
                        raise ValueError('Could not parse value from ' + el.tag + ' attribute ' + element_def['value_attr'] + ' without explicit type')

                    value = self._parse_value_as_type(el.get(element_def['value_attr']), element_def['type'])
                else:
                    # try parsing from the tag itself, just mapping with the key
                    if 'type' in element_def:
                        value = self._parse_value_as_type(el.text, element_def['type'])
                    else:
                        # needs 'class' in element_def
                        value = Model.load(self, el)
                        value.tag_name = tag_name

                dic[key] = value
                logger.debug('Mapped ' + str(key) + ' to ' + str(value) + ' in ' + element_def['dict'])

            elif 'class' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements as ' + element_def['class'])
                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                else:
                    value = Model.load(self, el)
                    value.tag_name = tag_name

                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = tag_name.replace('-', '_')

                setattr(self, name, value)
                logger.debug('Set attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            elif 'type' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements as ' + element_def['type'])
                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                else:
                    value = self._parse_value_as_type(el.text, element_def['type'])

                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = tag_name.replace('-', '_')

                setattr(self, name, value)
                logger.debug('Set attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            elif 'enum' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements from enum ' + str(element_def['enum']))
                if el.text not in element_def['enum']:
                    raise EnumerationException(tag + ' value must be one of ' + str(element_def['enum']))

                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = tag_name.replace('-', '_')

                value = el.text

                setattr(self, name, value)
                logger.debug('Set enum attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            else:
                raise UnknownElementException(str(self) + ' could not parse ' + tag + ' element')

            if tag not in self.tag_counts:
                self.tag_counts[tag] = 1
            else:
                self.tag_counts[tag] += 1

            return

        raise UnknownElementException('Unknown ' + str(self) + ' sub-element ' + el.tag + ' does not match ' + str([fq_tag, tag_name, ns_any, '*']))

    def to_xml(self):
        logger.debug(str(self) + ' to xml')
        el = ET.Element('{' + self.get_xmlns() + '}' + self.get_tag_name())
        if self.text is not None:
            el.text = str(self.text)

        for name in self.model_map['attributes']:
            value = self._produce_attribute(name, el)

        for element_def in self.model_map['elements']:
            el.extend(self._produce_elements(element_def))

        if self.tail is not None:
            el.tail = str(self.tail)
        return el

    def _produce_attribute(self, name, el):
        if name.endswith('*'):
            return

        attr_namespace, attr_name = Model.parse_tag(name)
        attr_map = self.model_map['attributes'][name]

        if 'in' in attr_map:
            value_name = attr_map['in']
        else:
            value_name = attr_name.replace('-', '_')

        if not hasattr(self, value_name):
            if 'required' in attr_map and attr_map['required']:
                raise RequiredAttributeException(str(self) + ' must assign required attribute ' + attr_name)
            else:
                logger.debug('Skipping undefined attribute ' + attr_name)
                return
        else:
            value = getattr(self, value_name)

        # TODO nillable for attrs?
        if value is None:
            if 'required' in attr_map and attr_map['required']:
                raise RequiredAttributeException(str(self) + ' must assign required attribute ' + attr_name)
            else:
                logger.debug(str(self) + ' Skipping unassigned attribute ' + attr_name)
                return

        if 'default' in attr_map and value == attr_map['default']:
            logger.debug('Skipping attribute ' + attr_name + '; remains at default ' + str(attr_map['default']))
            return

        # if model's xmlns doesn't match attribute's, then we need to include it
        if attr_namespace is not None and self.get_xmlns() != attr_namespace:
            attr_name = name

        if 'type' in attr_map:
            logger.debug(str(self) + ' Producing ' + str(value) + ' as ' + attr_map['type'] + ' type')
            v = self._produce_value_as_type(value, attr_map['type'])

            el.set(attr_name, v)

        elif 'enum' in attr_map:
            if value not in attr_map['enum']:
                raise EnumerationException(str(self) + '.' + name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))
            el.set(attr_name, value)

        else:
            # otherwise, we default to producing as string
            logger.debug(str(self) + ' Producing ' + str(value) + ' as String type')
            v = self._produce_value_as_type(value, 'String')
            el.set(attr_name, v)

    def _produce_elements(self, element_def):
        sub_els = []
        if 'xmlns' in element_def:
            xmlns = element_def['xmlns']
        else:
            xmlns = self.get_xmlns()

        if element_def['tag_name'].endswith('*'):
            if 'in' in element_def:
                name = element_def['in']
            else:
                name = '_elements'

            lst = getattr(self, name)
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from wildcard ' + name)

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(lst):
                raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(lst):
                raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            for i in lst:
                if isinstance(i, Model):
                    sub_els.append(i.to_xml())
                elif isinstance(i, ET.Element):
                    sub_els.append(i)
                else:
                    el = ET.Element(tag)
                    el.text = i
                    sub_els.append(el)
        elif 'list' in element_def:
            name = element_def['list']

            lst = getattr(self, name)
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from list ' + name)

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(lst):
                raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(lst):
                raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            for i in lst:
                if i is None:
                    el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
                    el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    sub_els.append(el)
                elif 'type' in element_def:
                    el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
                    el.text = self._produce_value_as_type(i, element_def['type'])
                    sub_els.append(el)
                elif 'class' in element_def:
                    if not isinstance(i, Model):
                        raise ValueError(str(self) + ' Unknown class of ' + element_def['tag_name'] + ' to add to sub elements: ' + i.__class__.__name__)
                    sub_els.append(i.to_xml())
                elif isinstance(i, ET.Element):
                    sub_els.append(i)
                else:
                    el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
                    el.text = i
                    sub_els.append(el)
        elif 'dict' in element_def:
            dict_ = getattr(self, element_def['dict'])
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from dict ' + element_def['dict'])

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(dict_):
                raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(dict_)) + ' found')

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(dict_):
                raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(dict_)) + ' found')

            if 'key' in element_def:
                key_name = element_def['key']
            else:
                key_name = 'id'

            dict_keys = list(dict_.keys())
            if None in dict_keys:
                dict_keys.remove(None)
                dict_keys.sort()
                dict_keys.insert(0, None)
            else:
                dict_keys.sort()

            for k in dict_keys:
                v = dict_[k]
                if v is None:
                    if 'value_attr' in element_def:
                        raise ValueError('Cannot use None as a value for value attribute maps')

                    el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
                    el.set(key_name, k)
                    el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    sub_els.append(el)
                elif 'class' in element_def:
                    setattr(v, key_name, k)
                    sub_els.append(v.to_xml())
                else:
                    el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
                    el.set(key_name, k)

                    if 'value_attr' in element_def:
                        value_name = element_def['value_attr']
                        el.set(value_name, self._produce_value_as_type(v, element_def['type']))
                    else:
                        el.text = v
                    sub_els.append(el)

        elif 'class' in element_def:
            if 'in' in element_def:
                name = element_def['in']
            else:
                name = element_def['tag_name'].replace('-', '_')

            value = getattr(self, name)
            if value is None:
                return []

            logger.debug(str(self) + ' Setting .' + name + ' to ' + value.__class__.__name__ + '(' + str(value) + ')')
            if isinstance(value, Model):
                sub_els.append(value.to_xml())
            elif isinstance(value, ET.Element):
                sub_els.append(value)
            else:
                raise UnknownElementException(str(self) + ' Unknown class to add to sub elements: ' + value.__class__.__name__)
        elif 'type' in element_def:
            if 'in' in element_def:
                name = element_def['in']
            else:
                name = element_def['tag_name'].replace('-', '_')

            value = getattr(self, name)
            if value is None:
                return []

            # create an element
            el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
            el.text = self._produce_value_as_type(value, element_def['type'])
            return [el]
        elif 'enum' in element_def:
            if 'in' in element_def:
                name = element_def['in']
            else:
                name = element_def['tag_name'].replace('-', '_')

            value = getattr(self, name)
            if value is None:
                return []

            if value not in element_def['enum']:
                raise EnumerationException(str(self) + ' ' + element_def['tag_name'] + ' is not in enumeration : ' + str(element_def['enum']))

            el = ET.Element('{' + xmlns + '}' + element_def['tag_name'])
            el.text = value
            return [el]
        else:
            raise UnknownElementException(str(self) + ' Unable to produce element definition: ' + str(element_def))
        return sub_els
