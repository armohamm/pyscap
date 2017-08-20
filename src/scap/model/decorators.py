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

class attribute(object):
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
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, cls):
        cls._model_content = self._kwargs
        return cls
