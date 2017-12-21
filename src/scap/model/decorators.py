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

import importlib
import logging
import os
import sys
import types

logger = logging.getLogger(__name__)

class attribute(object):
    '''
        Decorator to map xml elements to model children

        **kwargs**

        namespace
            The xml namespace to match. It can also be * to match any namespace.
            If not specified, it defaults to the parent element.
        local_name
            Required. The local name of the xml element we're matching. It can
            also be * to match any local name.
        into
            The python attribute to store the value of the element into.
            Defaults to the local_name if not specified.
        list
            The python attribute to store the value of the element into (as a
            list).  Defaults to the local_name if not specified.
        dict
            The python attribute to store the value of the element into (as a
            dict).  Defaults to the local_name if not specified.

        One of *type* or *cls* must be specified. *defer_class_load* can be
        used to load the class upon access instead of passing the class:

        type
            The type of the expected value. Types are stored directly as data,
            no enclosed in a model class. Types usually restrict the domain
            values.
        cls
            The model class with which to load the element.
        min
            The minimum number of elements to be present. Can be numeric or None
            (the  default).
        max
            The maximum number of elements to be present. Can be numeric or None
            (the default).
    '''
    def __init__(self, **kwargs):
        if 'local_name' not in kwargs:
            raise DecoratorException('Attributes need at least local_name defined')

        self._kwargs = kwargs

    def __call__(self, cls):
        if not hasattr(cls, '_model_attributes'):
            cls._model_attributes = {}
        if 'namespace' in self._kwargs:
            key = (self._kwargs['namespace'], self._kwargs['local_name'])
        else:
            key = (None, self._kwargs['local_name'])
        cls._model_attributes[key] = self._kwargs
        return cls

class element(object):
    '''
        Decorator to map xml elements to model children

        **kwargs**

        namespace
            The xml namespace to match. It can also be * to match any namespace.
            If not specified, it defaults to the parent element.
        local_name
            Required. The local name of the xml element we're matching. It can
            also be * to match any local name.
        into
            The python attribute to store the value of the element into.
            Defaults to the local_name if not specified.
        list
            The python attribute to store the value of the element into (as a
            list).  Defaults to the local_name if not specified.
        dict
            The python attribute to store the value of the element into (as a
            dict). Defaults to the local_name if not specified.
        key
            The key of the sub-element to use as the key of the dict. By default
            it is the *id* attribute.

        One of *type* or *cls* must be specified. *defer_class_load* can be
        used to load the class upon access instead of passing the class:

        type
            The type of the expected value. Types are stored directly as data,
            no enclosed in a model class. Types usually restrict the domain
            values.
        cls
            The model class with which to load the element.

        min
            The minimum number of elements to be present. Can be numeric or None
            (the  default).
        max
            The maximum number of elements to be present. Can be numeric or None
            (the default).

        value_enum
            Enumeration to which the value of the element must belong.
        value_pattern
            Pattern which the value of the element must match.

        nillable
            If True, the element can be nil (from the xsi spec). False
            specifies that it cannot (the default).
    '''
    def __init__(self, **kwargs):
        if 'local_name' not in kwargs:
            raise DecoratorException('Attributes need at least local_name defined')

        self._kwargs = kwargs

    def __call__(self, cls):
        if not hasattr(cls, '_model_element_definitions'):
            cls._model_element_definitions = {}
        if 'namespace' in self._kwargs:
            key = (self._kwargs['namespace'], self._kwargs['local_name'])
        else:
            key = (None, self._kwargs['local_name'])
        cls._model_element_definitions[key] = self._kwargs

        if not hasattr(cls, '_model_element_order'):
            cls._model_element_order = []
        # have to insert at the front because decorators are applied in reverse order
        cls._model_element_order.insert(0, key)
        return cls

class content(object):
    '''
        Decorator to map content of a xml element for use by the model

        **kwargs**

    '''
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, cls):
        cls._model_content = self._kwargs
        return cls

def defer_class_load(module, class_name):
    '''
        Returns a class from *module* and *class_name* specification at runtime,
        avoiding reference loops between classes and model definitions.
    '''
    def _load_class():
        # use cached copy of module if possible
        if module not in sys.modules:
            logger.debug('Loading module ' + module)
            mod = importlib.import_module(module)
        else:
            mod = sys.modules[module]

        return setattr(mod, class_name)

    return _load_class
