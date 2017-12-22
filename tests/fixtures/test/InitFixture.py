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

from scap.Model import Model
from scap.model.decorators import *
from scap.model.types import *
from .EnclosedFixture import EnclosedFixture

@attribute(local_name='attr')
@attribute(local_name='in_attr', into='test_attr')
@attribute(local_name='dash-attr')
@attribute(local_name='default_attr', default='Default')
@element(local_name='list', list='list_', cls=EnclosedFixture)
@element(local_name='dict', dict='dict_', cls=EnclosedFixture)
@element(local_name='in_test', into='test_in', cls=EnclosedFixture)
@element(local_name='dash-test', cls=EnclosedFixture)
@element(namespace='http://jaymes.biz/test2', local_name='*', into='test2_elements')
@element(local_name='*'},
class InitFixture(Model):
    pass
