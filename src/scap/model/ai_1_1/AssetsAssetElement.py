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

from scap.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)

@attributes(None, 'id', type='NCNameType', required=True)
@attributes('*', '*')
@element(None, 'circuit', in='asset', class='CircuitType')
@element(None, 'computing-device', in='asset', class='ComputingDeviceType')
@element(None, 'data', in='asset', class='DataType')
@element(None, 'database', in='asset', class='DatabaseType')
@element(None, 'network', in='asset', class='NetworkType')
@element(None, 'organization', in='asset', class='OrganizationType')
@element(None, 'person', in='asset', class='PersonType')
@element(None, 'service', in='asset', class='ServiceType')
@element(None, 'software', in='asset', class='SoftwareType')
@element(None, 'system', in='asset', class='SystemType')
@element(None, 'website', in='asset', class='WebsiteType')
class AssetsAssetElement(Model):
    pass
