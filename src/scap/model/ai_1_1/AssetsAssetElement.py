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

from scap.model.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)

@attribute(None, 'id', type='NCNameType', required=True)
@attribute('*', '*')
@element(None, 'circuit', into='asset', cls='CircuitType')
@element(None, 'computing-device', into='asset', cls='ComputingDeviceType')
@element(None, 'data', into='asset', cls='DataType')
@element(None, 'database', into='asset', cls='DatabaseType')
@element(None, 'network', into='asset', cls='NetworkType')
@element(None, 'organization', into='asset', cls='OrganizationType')
@element(None, 'person', into='asset', cls='PersonType')
@element(None, 'service', into='asset', cls='ServiceType')
@element(None, 'software', into='asset', cls='SoftwareType')
@element(None, 'system', into='asset', cls='SystemType')
@element(None, 'website', into='asset', cls='WebsiteType')
class AssetsAssetElement(Model):
    pass
