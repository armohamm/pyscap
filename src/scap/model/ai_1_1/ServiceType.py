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
from .HostType import HostType
from .ServicePortType import ServicePortType
from .PortRangeType import PortRangeType
from .ProtocolType import ProtocolType

logger = logging.getLogger(__name__)

@element(local_name='host', cls=HostType, min=0)
@element(local_name='port', list='ports', cls=ServicePortType, min=0, max=None)
@element(local_name='port-range', list='port_ranges', cls=PortRangeType, min=0, max=None)
@element(local_name='protocol', cls=ProtocolType, min=0)
class ServiceType(ITAssetType):
    pass
