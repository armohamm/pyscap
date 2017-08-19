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
from scap.model.ai_1_1.ITAssetType import ITAssetType

logger = logging.getLogger(__name__)

@element(None, 'distinguished-name', class='DistinguishedNameType', min=0)
@element(None, 'cpe', list='cpes', class='CPEType', min=0, max=None),
@element(None, 'connections', class='ConnectionsType', min=0),
@element(None, 'fqdn', class='FQDNType', min=0),
@element(None, 'hostname', class='ComputingDeviceHostnameType', min=0),
@element(None, 'motherboard-guid', class='MotherboardGUIDType', min=0),
class ComputingDeviceType(ITAssetType):
    #TODO: cpes as fs_string
    pass
