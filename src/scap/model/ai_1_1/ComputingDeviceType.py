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

from .ITAssetType import ITAssetType
from .DistinguishedNameType import DistinguishedNameType
from .CPEType import CPEType
from .ConnectionsType import ConnectionsType
from .FQDNType import FQDNType
from .ComputingDeviceHostnameType import ComputingDeviceHostnameType
from .MotherboardGUIDType import MotherboardGUIDType

logger = logging.getLogger(__name__)

@element(local_name='distinguished-name', cls=DistinguishedNameType, min=0)
@element(local_name='cpe', list='cpes', cls=CPEType, min=0, max=None)
@element(local_name='connections', cls=ConnectionsType, min=0)
@element(local_name='fqdn', cls=FQDNType, min=0)
@element(local_name='hostname', cls=ComputingDeviceHostnameType, min=0)
@element(local_name='motherboard-guid', cls=MotherboardGUIDType, min=0)
class ComputingDeviceType(ITAssetType):
    #TODO: cpes as fs_string
    pass
