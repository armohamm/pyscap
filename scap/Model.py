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

    maps = {}
    index = {}
    __xmlns_to_namespace = {
        'http://www.w3.org/XML/1998/namespace': 'xml',
        'http://www.w3.org/2001/XMLSchema': 'xs',
        'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
    }
    __namespace_to_xmlns = {
        'xml': 'http://www.w3.org/XML/1998/namespace',
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    }

    @staticmethod
    def register_namespace(namespace, xmlns):
        Model.__xmlns_to_namespace[xmlns] = namespace
        Model.__namespace_to_xmlns[namespace] = xmlns
        ET.register_namespace(namespace, xmlns)

    @staticmethod
    def unregister_namespace(namespace):
        try:
            xmlns = Model.__namespace_to_xmlns[namespace]
        except KeyError:
            raise UnregisteredNamespaceException('Unregistered namespace: ' + namespace)

        del Model.__namespace_to_xmlns[namespace]
        del Model.__xmlns_to_namespace[xmlns]

    @staticmethod
    def parse_tag(tag):
        # parse tag
        if tag.startswith('{'):
            xml_namespace, tag_name = tag[1:].split('}')
        else:
            return None, tag

        if xml_namespace not in Model.__xmlns_to_namespace:
            raise UnregisteredNamespaceException('Unregistered namespace: ' + xml_namespace + ', tag name: ' + tag_name)

        return xml_namespace, tag_name

    @staticmethod
    def namespace_to_xmlns(namespace):
        logger.debug('Looking for xml namespace for model namespace ' + namespace)
        if namespace not in Model.__namespace_to_xmlns:
            raise UnregisteredNamespaceException('Namespace ' + namespace + ' is not in supported namespaces')

        return Model.__namespace_to_xmlns[namespace]

    @staticmethod
    def xmlns_to_namespace(xmlns):
        logger.debug('Looking for model namespace for xml namespace ' + xmlns)
        if xmlns not in Model.__xmlns_to_namespace:
            raise UnregisteredNamespaceException('XML namespace ' + xmlns + ' is not in supported namespaces')

        return Model.__xmlns_to_namespace[xmlns]

    @staticmethod
    def map_tag_to_module_name(model_namespace, tag):
        pkg_mod = importlib.import_module('scap.model.' + model_namespace)
        try:
            module_name = pkg_mod.TAG_MAP[tag]
        except AttributeError:
            logger.critical(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + tag)
            raise TagMappingException(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + tag)
        except KeyError:
            logger.critical(pkg_mod.__name__ + ' does not define mapping for ' + tag + ' tag')
            raise TagMappingException(pkg_mod.__name__ + ' does not define mapping for ' + tag + ' tag')

        return module_name

    @staticmethod
    def load(parent, child_el):
        xml_namespace, tag_name = Model.parse_tag(child_el.tag)

        # try to load the tag's module
        if parent is None:
            if xml_namespace is None:
                raise UnregisteredNamespaceException('Unable to determine namespace without fully qualified tag (' + child_el.tag + ') and parent model')

            if xml_namespace not in Model.__xmlns_to_namespace:
                raise UnregisteredNamespaceException('Unregistered namespace: ' + xml_namespace + ', tag name: ' + child_el.tag)

            model_namespace = Model.__xmlns_to_namespace[xml_namespace]
            module_name = Model.map_tag_to_module_name(model_namespace, child_el.tag)
        else:
            if xml_namespace is None:
                model_namespace = parent.get_namespace()
            else:
                model_namespace = Model.__xmlns_to_namespace[xml_namespace]

            mmap = Model._get_model_map(parent.__class__)

            logger.debug('Checking ' + parent.__class__.__name__ + ' for tag ' + child_el.tag)
            ns_any = '{' + xml_namespace + '}*'
            module_name = None
            for name in [child_el.tag, tag_name, ns_any, '*']:
                if name not in mmap['element_lookup']:
                    continue

                logger.debug(child_el.tag + ' matched ' + name + ' mapping in ' + parent.__class__.__name__)
                if name.endswith('*'):
                    module_name = Model.map_tag_to_module_name(model_namespace, child_el.tag)
                    break
                elif 'class' in mmap['element_lookup'][name]:
                    module_name = mmap['element_lookup'][name]['class']
                    break

            if module_name is None:
                logger.debug('Did not match any of ' + str([child_el.tag, tag_name, ns_any, '*']))
                logger.critical(parent.__class__.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
                raise TagMappingException(parent.__class__.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')

        # qualify module name if needed
        if '.' not in module_name:
            model_module = 'scap.model.' + model_namespace + '.' + module_name
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
        if fq_model_class_name not in Model.maps:
            at_map = {}
            el_map = {}
            el_order = []
            xml_namespace = None
            tag_name = None
            for class_ in model_class.__mro__:
                if class_ == object:
                    break

                if class_.__module__.startswith('collections.'):
                    # skip collection classes
                    continue

                fq_class_name = class_.__module__ + '.' + class_.__name__

                try:
                    class_.MODEL_MAP
                except AttributeError:
                    logger.critical('Class ' + fq_class_name + ' does not define MODEL_MAP')
                    sys.exit()

                # overwrite the super class' ns & tag with what we've already loaded
                try:
                    if xml_namespace is None:
                        xml_namespace = class_.MODEL_MAP['xml_namespace']
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[xml_namespace] defined')
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

            if xml_namespace is None:
                # try to auto detect from module name
                module_parts = model_class.__module__.split('.')
                if module_parts[0] == 'scap' and module_parts[1] == 'model':
                    xml_namespace = Model.namespace_to_xmlns(module_parts[2])

            el_lookup = {}
            for element_def in el_map:
                if 'xml_namespace' in element_def:
                    el_lookup['{' + element_def['xml_namespace'] + '}' + element_def['tag_name']] = element_def
                else:
                    # try using element's xml_namespace
                    el_lookup['{' + xml_namespace + '}' + element_def['tag_name']] = element_def

            Model.maps[fq_model_class_name] = {
                'xml_namespace': xml_namespace,
                'tag_name': tag_name,
                'attributes': at_map,
                'elements': el_map,
                'element_lookup': el_lookup,
            }
        return Model.maps[fq_model_class_name]

    @staticmethod
    def find_content(uri):
        # locate content & load it, returning the root Model
        if os.path.isfile(uri):
            try:
                return Model.load(None, ET.parse(uri).getroot())
            except:
                return None
        return None

    @staticmethod
    def find_reference(ref, _class = None):
        if _class is None:
            for _class in Model.index:
                if ref in Model.index[_class]:
                    return Model.index[_class][ref]
        else:
            if ref in Model.index[_class]:
                return Model.index[_class][ref]

        return None

    def __init__(self, value=None, tag_name=None):
        self.parent = None
        self.sub_references = {}
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
        if 'xml_namespace' not in self.model_map or self.model_map['xml_namespace'] is None:
            raise ValueError('No xml_namespace defined for ' + self.__class__.__name__ + ' & could not detect')

        if self.model_map['xml_namespace'] not in Model.__xmlns_to_namespace:
            raise ValueError('Unknown namespace: ' + self.model_map['xml_namespace'])

        # initialize attribute values
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xml_namespace, attr_name = Model.parse_tag(name)
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

            elif 'append' in element_def:
                # initialze the array if it doesn't exist
                if element_def['append'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + element_def['append'] + ' to []')
                    setattr(self, element_def['append'], [])

            elif 'map' in element_def:
                # initialze the dict if it doesn't exist
                if element_def['map'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + element_def['map'] + ' to {}')
                    setattr(self, element_def['map'], {})

            else:
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = element_def['tag_name'].replace('-', '_')

                if name not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + name + ' to None')
                    setattr(self, name, None)

    def __str__(self):
        s = self.__class__.__name__
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
            if self.__class__.__name__ not in Model.index:
                Model.index[self.__class__.__name__] = {}
            Model.index[self.__class__.__name__][value] = self

    def get_namespace(self):
        model_namespace = self.__module__.split('.')
        model_namespace = model_namespace[2]
        return model_namespace

    def get_tag_name(self):
        if hasattr(self, 'tag_name'):
            return self.tag_name
        if 'tag_name' not in self.model_map or self.model_map['tag_name'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag_name')
        return self.model_map['tag_name']

    def get_xml_namespace(self):
        if 'xml_namespace' not in self.model_map or self.model_map['xml_namespace'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define namespace')
        return self.model_map['xml_namespace']

    def from_xml(self, parent, el):
        self.parent = parent

        logger.debug('Parsing ' + el.tag + ' element into ' + self.__class__.__module__ + '.' + self.__class__.__name__ + ' class')

        # save the tag_name
        xml_namespace, tag_name = Model.parse_tag(el.tag)

        # check that required attributes are defined
        for attrib in self.model_map['attributes']:
            if 'required' in self.model_map['attributes'][attrib] \
            and self.model_map['attributes'][attrib]['required'] \
            and attrib not in el.keys() \
            and 'default' not in self.model_map['attributes'][attrib]:
                logger.critical(el.tag + ' must define ' + attrib + ' attribute')
                sys.exit()

        for name, value in list(el.items()):
            if not self._parse_attribute(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                sys.exit()

        sub_el_counts = {}
        for sub_el in el:
            if not self._parse_element(sub_el):
                logger.debug('Elements: ' + str(self.model_map['elements']))
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                sys.exit()

        # check the element restrictions
        for element_def in self.model_map['elements']:
            min_ = 1
            if 'map' in element_def or 'append' in element_def:
                # maps and appends default to no max
                max_ = None
            else:
                max_ = 1

            if 'min' in element_def:
                min_ = element_def['min']
            if 'max' in element_def:
                max_ = element_def['max']

            if min_ == 0:
                pass
            elif element_def['tag_name'] not in self.tag_counts or self.tag_counts[element_def['tag_name']] < min_:
                logger.critical(self.__class__.__name__ + ' must have at least ' + str(min_) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            if max_ is None:
                pass
            elif element_def['tag_name'] in self.tag_counts and self.tag_counts[element_def['tag_name']] > max_:
                logger.critical(self.__class__.__name__ + ' must have at most ' + str(max_) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

        self.text = el.text

    def _load_type_class(self, type_):
        if '.' in type_:
            try:
                mod = importlib.import_module('scap.model.' + type_)
                type_ = type_.partition('.')[2]
            except ImportError:
                raise NotImplementedError('Type value scap.model.' + type_ + ' was not found')
        else:
            try:
                mod = importlib.import_module('scap.model.xs.' + type_)
            except ImportError:
                model_namespace = self.get_namespace()
                try:
                    mod = importlib.import_module('scap.model.' + model_namespace + '.' + type_)
                except ImportError:
                    raise NotImplementedError('Type value ' + type_ + ' not defined in scap.model.xs or local namespace (scap.model.' + model_namespace + ')')
        return getattr(mod, type_)

    def _parse_value_as_type(self, value, type_):
        class_ = self._load_type_class(type_)
        return class_().parse_value(value)

    def _produce_value_as_type(self, value, type_):
        class_ = self._load_type_class(type_)
        return class_().produce_value(value)

    def _parse_attribute(self, name, value):
        xml_namespace, attr_name = Model.parse_tag(name)

        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'

        for name in [name, attr_name, ns_any, '*']:
            if name not in self.model_map['attributes']:
                continue

            attr_map = self.model_map['attributes'][name]

            if 'notImplemented' in attr_map and attr_map['notImplemented']:
                raise NotImplementedError(name + ' attribute support is not implemented')

            if 'enum' in attr_map and value not in attr_map['enum']:
                raise ValueError(name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))

            # convert value
            if 'type' in attr_map:
                logger.debug('Parsing ' + str(value) + ' as ' + attr_map['type'] + ' type')
                value = self._parse_value_as_type(value, attr_map['type'])

            if 'in' in attr_map:
                setattr(self, attr_map['in'], value)
                logger.debug('Set attribute ' + attr_map['in'] + ' = ' + str(value))
            else:
                name = attr_name.replace('-', '_')
                setattr(self, name, value)
                logger.debug('Set attribute ' + name + ' = ' + str(value))
            return True
        return False

    def _parse_element(self, el):
        xml_namespace, tag_name = Model.parse_tag(el.tag)

        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'

        for tag in [el.tag, tag_name, ns_any, '*']:
            # check both namespace + tag_name and just tag_name
            if tag not in self.model_map['element_lookup']:
                continue

            logger.debug('Tag ' + el.tag + ' matched ' + tag)
            element_def = self.model_map['element_lookup'][tag]

            if 'notImplemented' in element_def and element_def['notImplemented']:
                raise NotImplementedError(tag + ' element support is not implemented')

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

            elif 'append' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements into ' + element_def['append'])
                lst = getattr(self, element_def['append'])

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
                logger.debug('Appended ' + str(value) + ' to ' + element_def['append'])

            elif 'map' in element_def:
                logger.debug(str(self) + ' parsing ' + tag + ' elements into ' + element_def['map'])
                dic = getattr(self, element_def['map'])

                if 'key' in element_def:
                    try:
                        key = el.get(element_def['key'])
                    except KeyError:
                        key = None
                # TODO: implement keyElement as well
                else:
                    key = el.get('id')
                    if key is None:
                        raise ValueError('Unable to determine key name for map ' + element_def['map'] + ' in ' + self.__class__.__name__)

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
                and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in element_def and element_def['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'value' in element_def:
                    try:
                        if 'type' in element_def:
                            value = self._parse_value_as_type(value, element_def['type'])
                        else:
                            value = el.get(element_def['value'])
                    except KeyError:
                        value = None
                # TODO: implement valueElement? as well
                else:
                    if 'type' in element_def:
                        value = self._parse_value_as_type(el.text, element_def['type'])
                    else:
                        value = Model.load(self, el)
                        value.tag_name = tag_name

                dic[key] = value
                logger.debug('Mapped ' + str(key) + ' to ' + str(value) + ' in ' + element_def['map'])

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
                logger.debug(str(self) + ' parsing ' + tag + ' elements from enum ' + element_def['enum'])
                if el.text not in element_def['enum']:
                    raise ValueError(tag + ' value must be one of ' + str(element_def['enum']))

                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = tag_name.replace('-', '_')

                value = el.text

                setattr(self, name, value)
                logger.debug('Set enum attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            else:
                logger.debug(str(self) + ' could not parse ' + tag + ' element')
                return False

            if element_def['tag_name'] not in self.tag_counts:
                self.tag_counts[element_def['tag_name']] = 1
            else:
                self.tag_counts[element_def['tag_name']] += 1

            return True

        return False

    def to_xml(self):
        logger.debug(str(self) + ' to xml')
        el = ET.Element('{' + self.get_xml_namespace() + '}' + self.get_tag_name())
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

        if 'notImplemented' in attr_map and attr_map['notImplemented']:
            raise NotImplementedError(str(self) + '.' + name + ' attribute support is not implemented')

        if 'in' in attr_map:
            attr_name = attr_map['in']
        else:
            attr_name = attr_name.replace('-', '_')

        try:
            value = getattr(self, attr_name)
        except AttributeError:
            if 'required' in attr_map and attr_map['required']:
                logger.critical(str(self) + ' must assign required attribute ' + attr_name)
                sys.exit()
            else:
                logger.debug('Skipping attribute ' + attr_name)
                return

        if value is None:
            if 'required' in attr_map and attr_map['required']:
                logger.critical(str(self) + ' must assign required attribute ' + attr_name)
                sys.exit()
            else:
                logger.debug(str(self) + ' Skipping attribute ' + attr_name)
                return

        # if model's xml_namespace doesn't match attribute's, then we need to include it
        if attr_namespace is not None and self.get_xml_namespace() != attr_namespace:
            attr_name = name

        if 'class' in attr_map:
            if not isinstance(value, Model):
                raise ValueError(str(self) + ' Need a subclass of Model to set attribute ' + attr_name + ' on {' + self.get_xml_namespace() + '}' + self.get_tag_name() + '; got ' + str(value))

            logger.debug(str(self) + 'Setting attribute ' + attr_name + ' on {' + self.get_xml_namespace() + '}' + self.get_tag_name() + ' to ' + value.__class__.__name__ + ' value ' + value.to_string())
            el.set(attr_name, value.to_string())

        elif 'type' in attr_map:
            # TODO nillable
            # if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() \
            # and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
            #     # check if we can accept nil
            #     if 'nillable' in element_def and element_def['nillable']:
            #         value = None
            #     else:
            #         raise ValueError(el.tag + ' is nil, but not expecting nil value')
            logger.debug(str(self) + ' Producing ' + str(value) + ' as ' + attr_map['type'] + ' type')
            v = self._produce_value_as_type(value, attr_map['type'])

            el.set(attr_name, v)

        elif 'enum' in attr_map:
            if value not in attr_map['enum']:
                raise ValueError(str(self) + '.' + name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))
            el.set(attr_name, value)

        else:
            raise ValueError(str(self) + ' Unable to produce attribute ' + attr_name + '; no class, type or enum definition')

    def _produce_elements(self, element_def):
        sub_els = []

        if element_def['tag_name'].endswith('*'):
            if 'in' in element_def:
                name = element_def['in']
            else:
                name = '_elements'

            lst = getattr(self, name)
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from wildcard ' + name)

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(lst):
                logger.critical(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] <= len(lst):
                logger.critical(str(self) + ' must have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            for i in lst:
                if isinstance(i, Model):
                    sub_els.append(i.to_xml())
                elif isinstance(i, ET.Element):
                    sub_els.append(i)
                else:
                    el = ET.Element(tag)
                    el.text = i
                    sub_els.append(el)
        elif 'append' in element_def:
            name = element_def['append']

            lst = getattr(self, name)
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from append ' + name)

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(lst):
                logger.critical(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] <= len(lst):
                logger.critical(str(self) + ' must have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            for i in lst:
                if 'class' in element_def or 'type' in element_def:
                    if isinstance(i, Model):
                        sub_els.append(i.to_xml())
                    elif isinstance(i, ET.Element):
                        sub_els.append(i)
                    else:
                        raise ValueError(str(self) + ' Unknown class of ' + element_def['tag_name'] + ' to add to sub elements: ' + i.__class__.__name__)
                else:
                    el = ET.Element(tag)
                    el.text = i
                    sub_els.append(el)
        elif 'map' in element_def:
            dict_ = getattr(self, element_def['map'])
            logger.debug(str(self) + ' Appending ' + element_def['tag_name'] + ' elements from map ' + element_def['map'])

            # check minimum tag count
            if 'min' in element_def and element_def['min'] > len(dict_):
                logger.critical(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            # check maximum tag count
            if 'max' in element_def and element_def['max'] is not None and element_def['max'] <= len(dict_):
                logger.critical(str(self) + ' must have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements')
                sys.exit()

            if 'key' in element_def:
                key_name = element_def['key']
            else:
                key_name = 'id'

            dict_keys = list(dict_.keys())
            dict_keys.sort()
            for k in dict_keys:
                v = dict_[k]
                if 'class' in element_def:
                    sub_els.append(v.to_xml())
                elif 'type' in element_def:
                    class_ = self._load_type_class(element_def['type'])
                    inst = class_(value=v, tag_name=element_def['tag_name'])
                    inst.id = k
                    sub_els.append(inst.to_xml())
                else:
                    if 'xml_namespace' in element_def:
                        xml_namespace = element_def['xml_namespace']
                    else:
                        xml_namespace = self.model_map['xml_namespace']

                    el = ET.Element('{' + xml_namespace + '}' + element_def['tag_name'])
                    el.set(key_name, k)

                    if 'value' in element_def:
                        value_name = element_def['value']
                        el.set(value_name, v)
                    else:
                        el.text = v
                    sub_els.append(el)

        elif 'class' in element_def \
        or 'type' in element_def \
        or 'enum' in element_def:
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
                raise ValueError(str(self) + ' Unknown class to add to sub elements: ' + value.__class__.__name__)

        return sub_els
