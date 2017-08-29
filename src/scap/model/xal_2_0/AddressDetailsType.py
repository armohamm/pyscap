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

from .AddressLinesType import AddressLinesType
from .AddressType import AddressType
from .AdministrativeAreaType import AdministrativeAreaType
from .CountryType import CountryType
from .LocalityType import LocalityType
from .PostalServiceElementsType import PostalServiceElementsType
from .ThoroughfareType import ThoroughfareType

logger = logging.getLogger(__name__)

@attribute(local_name='AddressType', )
@attribute(local_name='CurrentStatus', )
@attribute(local_name='ValidFromDate', )
@attribute(local_name='ValidToDate', )
@attribute(local_name='Usage', )
@attribute(local_name='Code', ) # from grPostal
@attribute(local_name='AddressDetailsKey', )
@attribute(local_name='*', )
@element(local_name='PostalServiceElements', cls=PostalServiceElementsType)
@element(local_name='Address', cls=AddressType)
@element(local_name='AddressLines', cls=AddressLinesType)
@element(local_name='Country', cls=CountryType)
@element(local_name='AdministrativeArea', cls=AdministrativeAreaType)
@element(local_name='Locality', cls=LocalityType)
@element(local_name='Thoroughfare', cls=ThoroughfareType)
class AddressDetailsType(Model):
    pass
