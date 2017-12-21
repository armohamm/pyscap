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

@element(local_name='append_nil', list='append_nil', nillable=True, cls=EnclosedFixture, min=0)
@element(local_name='append_type', list='append_type', type=DecimalType, min=0)
@element(local_name='append_class', list='append_class', cls=EnclosedFixture, min=0)
class AppendElementFixture(Model):
    pass
