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

from collections import UserList, UserDict
import logging
import importlib
import sys
import os.path
import re
import xml.etree.ElementTree as ET

from scap.model.decorators import *
from scap.model.exceptions import *

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

class ModelList(UserList):
    def __init__(self, model, element_def, *args, **kwargs):
        super(ModelList, self).__init__(*args, **kwargs)
        self._model = model
        self.element_def = element_def

    def __setitem__(self, index, value):
        # remove former value from self._model._children_values
        if index < len(self.data):
            former_value = self.data[index]
            self._model.remove_child(former_value)

        # add new value to self._model._children_values
        self._model.append_child_for(value, self.element_def)

        super(ModelList, self).__setitem__(index, value)

    def __delitem__(self, index):
        # remove former value from self._model._children_values
        if index < len(self.data):
            former_value = self.data[index]
            self._model.remove_child(former_value)

        super(ModelList, self).__delitem__(index)

    def insert(self, index, value):
        # add new value to self._model._children_values
        self._model.append_child_for(value, self.element_def)

        super(ModelList, self).insert(index, value)

    #TODO __contains__, __iter__, __reversed__, index, and count
    #TODO reverse, and __iadd__

    def append(self, value):
        # add new value to self._model._children_values
        self._model.append_child_for(value, self.element_def)

        super(ModelList, self).append(value)

    def extend(self, lst):
        for value in lst:
            # add new value to self._model._children_values
            self._model.append_child_for(value, self.element_def)

        super(ModelList, self).extend(lst)

    def pop(self, i=-1):
        value = super(ModelList, self).pop(i)

        # remove former value from self._model._children_values
        self._model.remove_child(value)
        return value

    def remove(self, value):
        # remove former value from self._model._children_values
        self._model.remove_child(value)

        super(ModelList, self).remove(value)

class ModelDict(UserDict):
    def __init__(self, model, element_def, *args, **kwargs):
        super(ModelDict, self).__init__(*args, **kwargs)
        self._model = model
        self.element_def = element_def

    def __setitem__(self, key, value):
        # remove former value from self._model._children_values
        if key in self.data:
            former_value = self.data[key]
            self._model.remove_child(former_value)

        # add new value to self._model._children_values
        self._model.append_child_for(value, self.element_def, key)

        super(ModelDict, self).__setitem__(key, value)

    def __delitem__(self, key):
        # remove former value from self._model._children_values
        if key in self.data:
            former_value = self.data[key]
            self._model.remove_child(former_value)

        super(ModelDict, self).__delitem__(key, value)

    #TODO __contains__, keys, items, values, get, __eq__, and __ne__
    #TODO setdefault

    def pop(self, key, default=None):
        if default is None:
            value = super(ModelDict, self).pop(key)
        else:
            value = super(ModelDict, self).pop(key, default)

        # remove former value from self._model._children_values
        self._model.remove_child(value)
        return value

    def popitem(self):
        key, value = super(ModelDict, self).popitem()

        # remove former value from self._model._children_values
        self._model.remove_child(value)
        return key, value

    def clear(self):
        for value in self.data.values():
            self._model.remove_child(value)

        super(ModelDict, self).clear()

    def update(self, other=None, **kwargs):
        if other is None or len(other) <= 0:
            for k,v in kwargs:
                self.__setitem__(k, v)
        else:
            for k in other:
                self.__setitem__(k, other[k])

    def setdefault(self, key, default=None):
        if default is not None and key not in self.data:
            # add new value to self._model._children_values
            self._model.append_child_for(value, self.element_def, key)

        return super(ModelDict, self).setdefault(key, default)

class ModelChild(object):
    def __init__(self, model, element_def, value=None):
        self._model = model
        self.element_def = element_def
        self.value = value

@attribute('http://www.w3.org/XML/1998/namespace', 'lang', type='StringType', into='_xml_lang')
@attribute('http://www.w3.org/XML/1998/namespace', 'space', enum=('default', 'preserve'), into='_xml_space')
@attribute('http://www.w3.org/XML/1998/namespace', 'base', type='AnyUriType', into='_xml_base')
@attribute('http://www.w3.org/XML/1998/namespace', 'id', type='ID', into='_xml_id')
@attribute('http://www.w3.org/2001/XMLSchema-instance', 'type', type='QNameType', into='_xsi_type')
@attribute('http://www.w3.org/2001/XMLSchema-instance', 'nil', type='BooleanType', into='_xsi_nil', default=False)
@attribute('http://www.w3.org/2001/XMLSchema-instance', 'schemaLocation', type='AnyUriType', into='_xsi_schemaLocation')
@attribute('http://www.w3.org/2001/XMLSchema-instance', 'noNamespaceSchemaLocation', type='AnyUriType', into='_xsi_noNamespaceSchemaLocation')
class Model(object):
    __model_mappings = {}

    __xmlns_to_package = {
        'http://www.w3.org/XML/1998/namespace': 'scap.model.xml',
        'http://www.w3.org/2001/XMLSchema': 'scap.model.xs',
        'http://www.w3.org/2001/XMLSchema-hasFacetAndProperty': 'scap.model.xs.hfp',
        'http://www.w3.org/2001/XMLSchema-instance': 'scap.model.xs.i',
    }
    __package_to_xmlns = {
        'scap.model.xml': 'http://www.w3.org/XML/1998/namespace',
        'scap.model.xs': 'http://www.w3.org/2001/XMLSchema',
        'scap.model.xs.hfp': 'http://www.w3.org/2001/XMLSchema-hasFacetAndProperty',
        'scap.model.xs.i': 'http://www.w3.org/2001/XMLSchema-instance',
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
    def load(parent, child_el, element_def=None):
        xmlns, tag_name = Model.parse_tag(child_el.tag)

        # try to load the tag's module
        if parent is None:
            if xmlns is None:
                raise UnregisteredNamespaceException('Unable to determine namespace without fully qualified tag (' + child_el.tag + ') and parent model')

            model_package = Model.xmlns_to_package(xmlns)
            model_package, module_name = Model._map_element_to_module_name(model_package, child_el)
        else:
            if xmlns is None:
                model_package = parent.get_package()
                ns_any = '{' + parent.xmlns + '}*'
                fq_tag = '{' + parent.xmlns + '}' + tag_name
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
                    model_package, module_name = Model._map_element_to_module_name(model_package, child_el)
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
            module_name = module_name.rpartition('.')[2]

        # use cached copy of module if possible
        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)
            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, module_name)
        if element_def is not None:
            inst = class_(element_def=element_def)
        else:
            inst = class_()
        inst.from_xml(parent, child_el)

        return inst

    @staticmethod
    def _map_element_to_module_name(model_package, el):
        pkg_mod = importlib.import_module(model_package)

        tag = el.tag
        if not hasattr(pkg_mod, 'TAG_MAP'):
            raise TagMappingException(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + tag)
        if tag not in pkg_mod.TAG_MAP:
            raise TagMappingException(pkg_mod.__name__ + ' does not define mapping for ' + tag + ' tag')

        return pkg_mod.__name__, pkg_mod.TAG_MAP[tag]

    @staticmethod
    def _get_model_map(model_class):
        # check the __model_mappings cache first, otherwise generate
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

                if not hasattr(class_, 'MODEL_MAP') or not isinstance(class_.MODEL_MAP, dict):
                    raise TagMappingException('Class ' + fq_class_name + ' does not define MODEL_MAP dict')

                # overwrite the super class' ns & tag with what we've already loaded
                if xmlns is None and 'xmlns' in class_.MODEL_MAP:
                    xmlns = class_.MODEL_MAP['xmlns']

                if tag_name is None and 'tag_name' in class_.MODEL_MAP:
                    tag_name = class_.MODEL_MAP['tag_name']

                # update the super class' attribute map with subclass
                if 'attributes' in class_.MODEL_MAP:
                    super_atmap = class_.MODEL_MAP['attributes'].copy()
                    super_atmap.update(at_map)
                    at_map = super_atmap

                # update the super class' element map with subclass
                if 'elements' in class_.MODEL_MAP:
                    super_elmap = class_.MODEL_MAP['elements'].copy()
                    super_elmap.extend(el_map)
                    el_map = super_elmap

            if xmlns is None:
                # try to auto detect from module name
                xmlns = Model.package_to_xmlns(model_class.__module__.rpartition('.')[0])

            el_lookup = {}
            for element_def in el_map:
                if not isinstance(element_def, dict):
                    raise TagMappingException('Class ' + fq_model_class_name + ' has an invalid element definition: ' + str(element_def))

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

    def __init__(self, value=None, xmlns=None, tag_name=None, element_def=None):
        # child_map must be first to prevent recursion of __getattr__
        self._child_map = {}
        self._children_values = []
        self._children_element_defs = []
        self._children_keys = []
        self._parent = None

        self._references = {}

        self._model_map = Model._get_model_map(self.__class__)

        self._value_enum = None
        self._value_pattern = None
        if element_def is not None:
            if 'value_enum' in element_def:
                self._value_enum = element_def['value_enum']
            if 'value_pattern' in element_def:
                self._value_pattern = element_def['value_pattern']

        if tag_name is not None:
            self.tag_name = tag_name
        elif 'tag_name' in self._model_map and self._model_map['tag_name'] is not None:
            self.tag_name = self._model_map['tag_name']

        # must have namespace for concrete classes
        if xmlns is not None:
            self.xmlns = xmlns
        elif 'xmlns' not in self._model_map or self._model_map['xmlns'] is None:
            raise ValueError('No xmlns defined for ' + self.__class__.__name__ + ' & could not detect')
        else:
            self.xmlns = self._model_map['xmlns']

        self._tag_counts = {}

        # initialize attribute values
        for name in self._model_map['attributes']:
            attr_map = self._model_map['attributes'][name]
            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xmlns, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')

            if 'default' in attr_map:
                default_value = attr_map['default']
                setattr(self, attr_name, default_value)
                logger.debug('Default of attribute ' + attr_name + ' = ' + str(default_value))
            else:
                setattr(self, attr_name, None)

        # initialize elements; if subclass defined the corresponding attribute,
        # we don't re-define
        for element_def in self._model_map['elements']:
            if element_def['tag_name'].endswith('*'):
                if 'in' not in element_def:
                    name = '_elements'
                else:
                    name = element_def['in']

                if name not in self._child_map:
                    logger.debug('Initializing ' + name + ' to ModelList()')
                    self._child_map[name] = ModelList(self, element_def)

            elif 'list' in element_def:
                # initialze the array if it doesn't exist
                if element_def['list'] not in self._child_map:
                    logger.debug('Initializing ' + element_def['list'] + ' to ModelList()')
                    self._child_map[element_def['list']] = ModelList(self, element_def)

            elif 'dict' in element_def:
                # initialze the dict if it doesn't exist
                if element_def['dict'] not in self._child_map:
                    logger.debug('Initializing ' + element_def['dict'] + ' to ModelDict()')
                    self._child_map[element_def['dict']] = ModelDict(self, element_def)

            else:
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = element_def['tag_name'].replace('-', '_')

                if name not in self._child_map:
                    logger.debug('Initializing ' + name + ' to ModelChild()')
                    self._child_map[name] = ModelChild(self, element_def)

        # initialize value
        # TODO we use self.text as the value storage; probably a better way
        if value is not None:
            self.set_value(value)
        else:
            self.text = None
        self.tail = None

    def is_nil(self):
        return self._xsi_nil

    def set_nil(self):
        self._xsi_nil = True
        self.set_value(None)

    def get_value(self):
        logger.debug(self.__class__.__name__ + ' value currently ' + str(self.text))
        return self.text

    def set_value(self, value):
        if self._value_enum is not None:
            if value not in self._value_enum:
                raise ValueError(self.__class__.__name__ + ' Invalid value ' + str(value) + '; not in ' + str(self._value_enum))
        if self._value_pattern is not None:
            if not isinstance(value, str) or not re.fullmatch(self._value_pattern, value):
                raise ValueError(self.__class__.__name__ + ' Invalid value ' + str(value) + '; does not match ' + self._value_pattern)
        self.text = value
        logger.debug(self.__class__.__name__ + ' value set to ' + str(self.text))

    def parse_value(self, value):
        return value

    def produce_value(self, value):
        if value is None:
            return value
        return str(value)

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
        try:
            object.__getattribute__(self, '_child_map')
        except:
            # not initialzed yet, just pass through
            object.__setattr__(self, name, value)

        # keep index of 'id' attrs
        if name == 'id':
            if self._parent is not None:
                self._parent._references[value] = self
        if name == 'parent' and hasattr(self, 'id'):
            self._parent._references[self.id] = self

        if name in self._child_map:
            # capture element assignment
            element_def = self._child_map[name].element_def
            if isinstance(self._child_map[name], ModelList):
                if isinstance(value, list):
                    # wrap in ModelList
                    self._child_map[name] = ModelList(self, element_def, value)
                else:
                    raise ValueError('Trying to assign ' + value.__class__.__name__ + ' type to ' + name + ' attribute, but expecting list')
            elif isinstance(self._child_map[name], ModelDict):
                if isinstance(value, dict):
                    # wrap in ModelDict
                    self._child_map[name] = ModelDict(self, element_def, value)
                else:
                    raise ValueError('Trying to assign ' + value.__class__.__name__ + ' type to ' + name + ' attribute, but expecting dict')
            elif isinstance(self._child_map[name], ModelChild):
                # wrapped in ModelChild
                self.remove_child(self._child_map[name].value)
                self._child_map[name].value = value
                self.append_child_for(value, self._child_map[name].element_def)
            else:
                raise ValueError('Child map entry for ' + name + ' is set to an unsupported type')
        else:
            # process as regular attribute
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        try:
            object.__getattribute__(self, '_child_map')
        except:
            # not initialzed yet, just return __getattribute__
            return object.__getattribute__(self, name)

        child_map = self._child_map
        if name in child_map:
            if isinstance(child_map[name], ModelChild):
                return child_map[name].value
            else:
                return child_map[name]
        else:
            raise AttributeError('Attribute ' + name + ' was not found in ' + self.__class__.__name__ + ': ' + str(child_map.keys()))

    def append_child_for(self, value, element_def, key=None):
        self._children_values.append(value)
        self._children_element_defs.append(element_def)
        self._children_keys.append(key)

    def remove_child(self, value):
        try:
            i = self._children_values.index(value)
            del self._children_values[i]
            del self._children_element_defs[i]
            del self._children_keys[i]
        except ValueError:
            pass

    def get_package(self):
        return self.__module__.rpartition('.')[0]

    def find_reference(self, ref):
        if ref in self._references:
            return self._references[ref]
        else:
            for c in self._children_values:
                try:
                    return c.find_reference(ref)
                except:
                    pass

        raise ReferenceException('Could not find reference ' + ref + ' within ' + str(self))

    def from_xml(self, parent, el):
        self._parent = parent

        logger.debug('Parsing ' + el.tag + ' element into ' + self.__class__.__module__ + '.' + self.__class__.__name__ + ' class')

        self.xmlns, self.tag_name = Model.parse_tag(el.tag)
        if self.xmlns is None:
            # copy the parents
            self.xmlns = self._parent.xmlns

        for attrib in self._model_map['attributes']:
            # check that required attributes are defined
            if 'required' in self._model_map['attributes'][attrib] \
            and self._model_map['attributes'][attrib]['required'] \
            and attrib not in el.keys() \
            and 'default' not in self._model_map['attributes'][attrib]:
                raise RequiredAttributeException(el.tag + ' must define ' + attrib + ' attribute')

            # check that prohibited attributes are not defined
            if 'prohibited' in self._model_map['attributes'][attrib] \
            and self._model_map['attributes'][attrib]['prohibited'] \
            and attrib in el.keys():
                raise ProhibitedAttributeException(el.tag + ' must not define ' + attrib + ' attribute')

        for name, value in list(el.items()):
            self._parse_attribute(name, value)

        for sub_el in el:
            self._parse_element(sub_el)

        # check the element restrictions
        for element_def in self._model_map['elements']:
            if 'xmlns' not in element_def and element_def['tag_name'] == '*':
                tag = '*'
            elif 'xmlns' in element_def:
                tag = '{' + element_def['xmlns'] + '}' + element_def['tag_name']
            else:
                tag = '{' + self.xmlns + '}' + element_def['tag_name']

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
            if min_ != 0 and (tag not in self._tag_counts or self._tag_counts[tag] < min_):
                raise MinimumElementException(self.__class__.__name__ + ' must have at least ' + str(min_) + ' ' + tag + ' elements')

            if max_ is not None and tag in self._tag_counts and self._tag_counts[tag] > max_:
                raise MaximumElementException(self.__class__.__name__ + ' may have at most ' + str(max_) + ' ' + tag + ' elements')

        if el.text is not None:
            self.set_value(self.parse_value(el.text))

    def _load_type_class(self, type_):
        if '.' in type_:
            module_name = type_
            class_ = type_.rpartition('.')[2]
            try:
                mod = importlib.import_module(type_)
            except ImportError:
                raise NotImplementedError('Type class ' + type_ + ' was not found')
            return getattr(mod, class_)
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
            ns_any = '{' + self._model_map['xmlns'] + '}*'
        else:
            ns_any = '{' + xmlns + '}*'

        for name in [fq_attr_name, attr_name, ns_any, '*']:
            if name not in self._model_map['attributes']:
                continue

            attr_map = self._model_map['attributes'][name]

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
            ns_any = '{' + self.xmlns + '}*'
            fq_tag = '{' + self.xmlns + '}' + tag_name
        else:
            ns_any = '{' + xmlns + '}*'
            fq_tag = el.tag

        for tag in [fq_tag, tag_name, ns_any, '*']:
            # check both namespace + tag_name and just tag_name
            if tag not in self._model_map['element_lookup']:
                continue

            logger.debug('Tag ' + el.tag + ' matched ' + tag)
            element_def = self._model_map['element_lookup'][tag]

            if 'ignore' in element_def and element_def['ignore'] == True:
                logger.debug('Ignoring ' + fq_tag + ' element in ' + str(self))
                return

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
                    value = Model.load(self, el, element_def=element_def)
                    value.xmlns = xmlns
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
                    value = Model.load(self, el, element_def=element_def)
                    value.xmlns = xmlns
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
                        value = Model.load(self, el, element_def=element_def)
                        value.xmlns = xmlns
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
                    value = Model.load(self, el, element_def=element_def)
                    value.xmlns = xmlns
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

            if tag not in self._tag_counts:
                self._tag_counts[tag] = 1
            else:
                self._tag_counts[tag] += 1

            return

        raise UnknownElementException('Unknown ' + str(self) + ' sub-element ' + el.tag + ' does not match ' + str([fq_tag, tag_name, ns_any, '*']))

    def to_xml(self):
        logger.debug(str(self) + ' to xml')
        el = ET.Element('{' + self.xmlns + '}' + self.tag_name)

        for name in self._model_map['attributes']:
            value = self._produce_attribute(name, el)

        for element_def in self._model_map['elements']:
            if element_def['tag_name'].endswith('*'):
                if 'in' in element_def:
                    lst = getattr(self, element_def['in'])
                else:
                    lst = getattr(self, '_elements')

                # check minimum tag count
                if 'min' in element_def and element_def['min'] > len(lst):
                    raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

                # check maximum tag count
                if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(lst):
                    raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            elif 'list' in element_def:
                lst = getattr(self, element_def['list'])

                # check minimum tag count
                if 'min' in element_def and element_def['min'] > len(lst):
                    raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

                # check maximum tag count
                if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(lst):
                    raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(lst)) + ' found')

            elif 'dict' in element_def:
                dct = getattr(self, element_def['dict'])

                # check minimum tag count
                if 'min' in element_def and element_def['min'] > len(dct):
                    raise MinimumElementException(str(self) + ' must have at least ' + str(element_def['min']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(dct)) + ' found')

                # check maximum tag count
                if 'max' in element_def and element_def['max'] is not None and element_def['max'] < len(dct):
                    raise MaximumElementException(str(self) + ' may have at most ' + str(element_def['max']) + ' ' + element_def['tag_name'] + ' elements; ' + str(len(dct)) + ' found')

        for i in range(0, len(self._children_values)):
            self._produce_child(i, el)

        el.text = self.produce_value(self.get_value())

        if self.tail is not None:
            el.tail = str(self.tail)

        return el

    def _produce_attribute(self, name, el):
        if name.endswith('*'):
            return

        attr_namespace, attr_name = Model.parse_tag(name)
        attr_map = self._model_map['attributes'][name]

        if 'in' in attr_map:
            value_name = attr_map['in']
        else:
            value_name = attr_name.replace('-', '_')

        if not hasattr(self, value_name):
            if 'required' in attr_map and attr_map['required']:
                raise RequiredAttributeException(str(self) + ' must assign required attribute ' + attr_name)
            elif 'prohibited' in attr_map and attr_map['prohibited']:
                logger.debug('Skipping prohibited attribute ' + attr_name)
                return
            else:
                logger.debug('Skipping undefined attribute ' + attr_name)
                return
        else:
            if 'prohibited' in attr_map and attr_map['prohibited']:
                raise ProhibitedAttributeException(str(self) + ' must not assign prohibited attribute ' + attr_name)
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
        if attr_namespace is not None and self.xmlns != attr_namespace:
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
            v = self._produce_value_as_type(value, 'StringType')
            el.set(attr_name, v)

    def _produce_child(self, child_index, el):
        child = self._children_values[child_index]
        element_def = self._children_element_defs[child_index]

        logger.debug(str(self) + ' producing ' + str(child) + ' according to ' + str(element_def))
        if element_def['tag_name'] == '*':
            if 'type' in element_def and child.tag_name is None:
                raise ValueError('Unable to produce wildcard tags with only "type" in the model map, because tag_name is not defined')

            # TODO nillable
            el.append(child.to_xml())

        elif 'list' in element_def:
            if 'xmlns' in element_def:
                xmlns = element_def['xmlns']
            else:
                xmlns = self.xmlns
            tag_name = element_def['tag_name']

            if 'type' in element_def:
                if child is None:
                    sub_el = ET.Element('{' + xmlns + '}' + tag_name)
                    sub_el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    el.append(sub_el)
                else:
                    # wrap value in xs element
                    class_ = self._load_type_class(element_def['type'])
                    child = class_(xmlns=xmlns, tag_name=tag_name, value=child)
                    el.append(child.to_xml())
            elif 'class' in element_def:
                if child is None:
                    sub_el = ET.Element('{' + xmlns + '}' + tag_name)
                    sub_el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    el.append(sub_el)
                else:
                    el.append(child.to_xml())

            else:
                raise ValueError('"class" or "type" must be defined for "list" and "dict" model mapping')

        elif 'dict' in element_def:
            if 'xmlns' in element_def:
                xmlns = element_def['xmlns']
            else:
                xmlns = self.xmlns
            tag_name = element_def['tag_name']

            # TODO: implement key_element as well
            key_name = 'id'
            if 'key' in element_def:
                key_name = element_def['key']

            if 'type' in element_def:
                sub_el = ET.Element('{' + xmlns + '}' + tag_name)
                sub_el.set(key_name, self._children_keys[child_index])
                if 'value_attr' in element_def:
                    if child is None:
                        raise ValueError(str(self) + ' Cannot have none for a value_attr: ' + element_def['dict'] + '[' + self._children_keys[child_index] + ']')
                    value = self._produce_value_as_type(child, element_def['type'])
                    sub_el.set(element_def['value_attr'], value)
                else:
                    if child is None:
                        sub_el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    else:
                        sub_el.text = self._produce_value_as_type(child, element_def['type'])
                el.append(sub_el)

            elif 'class' in element_def:
                if child is None:
                    sub_el = ET.Element('{' + xmlns + '}' + tag_name)
                    sub_el.set(key_name, self._children_keys[child_index])
                    sub_el.set('{http://www.w3.org/2001/XMLSchema-instance}nil', 'true')
                    el.append(sub_el)
                else:
                    setattr(child, key_name, self._children_keys[child_index])
                    el.append(child.to_xml())

            else:
                raise ValueError('"class" or "type" must be defined for "list" and "dict" model mapping')

        elif 'class' in element_def:
            if child is None:
                return

            el.append(child.to_xml())

        elif 'type' in element_def:
            if child is None:
                return

            if 'xmlns' in element_def:
                xmlns = element_def['xmlns']
            else:
                xmlns = self.xmlns
            tag_name = element_def['tag_name']
            class_ = self._load_type_class(element_def['type'])
            child = class_(xmlns=xmlns, tag_name=tag_name, value=child)

            el.append(child.to_xml())

        elif 'enum' in element_def:
            if child is None:
                return

            if child not in element_def['enum']:
                raise EnumerationException(tag + ' value must be one of ' + str(element_def['enum']))

            if 'xmlns' in element_def:
                xmlns = element_def['xmlns']
            else:
                xmlns = self.xmlns
            tag_name = element_def['tag_name']
            child = String(xmlns=xmlns, tag_name=tag_name, value=child)

            el.append(child.to_xml())

        else:
            raise UnknownElementException(str(self) + ' could not produce ' + tag + ' element')
