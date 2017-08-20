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

@attribute(local_name='id', type='NCNameType', required=True)
@attribute(namespace='*', local_name='*')
@element(local_name='circuit', into='asset', cls='CircuitType')
@element(local_name='computing-device', into='asset', cls='ComputingDeviceType')
@element(local_name='data', into='asset', cls='DataType')
@element(local_name='database', into='asset', cls='DatabaseType')
@element(local_name='network', into='asset', cls='NetworkType')
@element(local_name='organization', into='asset', cls='OrganizationType')
@element(local_name='person', into='asset', cls='PersonType')
@element(local_name='service', into='asset', cls='ServiceType')
@element(local_name='software', into='asset', cls='SoftwareType')
@element(local_name='system', into='asset', cls='SystemType')
@element(local_name='website', into='asset', cls='WebsiteType')
class AssetsAssetElement(Model):
    pass
