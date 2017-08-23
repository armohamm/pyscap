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

from scap.Model import Model
from scap.model.decorators import *

logger = logging.getLogger(__name__)

@element(local_name='os_name', type=StringType)
@element(local_name='os_version', type=StringType)
@element(local_name='architecture', type=StringType)
@element(local_name='primary_host_name', type=StringType)
@element(local_name='_interfaces', cls=InterfacesType)
@element(local_name='*', min=0, max=None)
class SystemInfoType(Model):
    pass
