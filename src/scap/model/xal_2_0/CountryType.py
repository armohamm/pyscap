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

from .AddressLineType import AddressLineType
from .AdministrativeAreaType import AdministrativeAreaType
from .CountryNameCodeType import CountryNameCodeType
from .CountryNameType import CountryNameType
from .LocalityType import LocalityType
from .ThoroughfareType import ThoroughfareType

logger = logging.getLogger(__name__)

@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='CountryNameCode', list='country_codes', cls=CountryNameCodeType)
@element(local_name='CountryName', list='countries', cls=CountryNameType)
@element(local_name='AdministrativeArea', into='administrative_area', cls=AdministrativeAreaType)
@element(local_name='Locality', into='locality', cls=LocalityType)
@element(local_name='Thoroughfare', into='thoroughfare', cls=ThoroughfareType)
@element(local_name='*')
class CountryType(Model):
    pass
