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

from expatriate.model.Model import Model
from expatriate.model.decorators import *

from .IPAddressType import IPAddressType
from .MACAddressType import MACAddressType
from .URLType import URLType

logger = logging.getLogger(__name__)

@element(local_name='ip-address', cls=IPAddressType, min=0)
@element(local_name='mac-address', cls=MACAddressType, min=0)
@element(local_name='url', list='urls', cls=URLType, min=0, max=None)
@element(local_name='subnet-mask', cls=IPAddressType, min=0)
@element(local_name='default-route', cls=IPAddressType, min=0)
class NetworkInterfaceType(Model):
    pass
