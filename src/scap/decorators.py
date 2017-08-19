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
    def __init__(self, namespace, local_name, **kwargs):
        self._namespace = namespace
        self._local_name = local_name
        self._kwargs = kwargs

    def __call__(self, cls):
        if not hasattr(cls, '_model_attributes'):
            cls._model_attributes = {}
        cls._model_attributes[(self._namespace, self._local_name)] = self._kwargs
        return cls

class element(object):
    def __init__(self, namespace, local_name, **kwargs):
        self._namespace = namespace
        self._local_name = local_name
        self._kwargs = kwargs

    def __call__(self, cls):
        if not hasattr(cls, '_model_element_definitions'):
            cls._model_element_definitions = {}
        cls._model_element_definitions[(self._namespace, self._local_name)] = self._kwargs

        if not hasattr(cls, '_model_element_order'):
            cls._model_element_order = []
        # have to insert at the front because decorators are applied in reverse order
        cls._model_element_order.insert(0, (self._namespace, self._local_name))
        return cls

class content(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, cls):
        cls._model_content = self._kwargs
        return cls
