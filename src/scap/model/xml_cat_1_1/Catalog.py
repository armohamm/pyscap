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

from collections.abc import MutableMapping
from scap.Model import Model
from scap.model.decorators import *
from scap.model.xs.IdType import IdType
from scap.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=IdType)
@attribute(local_name='prefer', enum=['system', 'public'])
@attribute(local_name='*')
@element(local_name='uri', dict='entries', key='name', value_attr='uri', type=StringType)
@element(local_name='*', min=0)
class Catalog(Model, MutableMapping):
    def __delitem__(self, key):
        del self.entries[key]

    def __getitem__(self, key):
        return self.entries[key]

    def __setitem__(self, key, value):
        self.entries[key] = value

    def __contains__(self, item):
        return item in self.entries

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries.keys().sort())
