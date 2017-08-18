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
        print('__init__')
        self._namespace = namespace
        self._local_name = local_name
        self._kwargs = kwargs

    def __call__(self, cls):
        print('__call__' + str(cls))
        if not hasattr(cls, '_attributes'):
            cls._attributes = {}
        cls._attributes[(self._namespace, self._local_name)] = self._kwargs
        return cls

@attribute('http://jaymes.biz', 'test', type='testType')
class DecoratedClass(object):
    pass

c = DecoratedClass()
print(str(c.__class__._attributes))
