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

from .AddressIdentifierType import AddressIdentifierType
from .AddressLatitudeDirectionType import AddressLatitudeDirectionType
from .AddressLatitudeType import AddressLatitudeType
from .AddressLongitudeDirectionType import AddressLongitudeDirectionType
from .AddressLongitudeType import AddressLongitudeType
from .BarcodeType import BarcodeType
from .EndorsementLineCodeType import EndorsementLineCodeType
from .KeyLineCodeType import KeyLineCodeType
from .SortingCodeType import SortingCodeType
from .SupplementaryPostalServiceDataType import SupplementaryPostalServiceDataType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='*', )
@element(local_name='AddressIdentifier', list='address_identifiers', cls=AddressIdentifierType)
@element(local_name='EndorsementLineCode', cls=EndorsementLineCodeType)
@element(local_name='KeyLineCode', cls=KeyLineCodeType)
@element(local_name='Barcode', cls=BarcodeType)
@element(local_name='SortingCode', cls=SortingCodeType)
@element(local_name='AddressLatitude', cls=AddressLatitudeType)
@element(local_name='AddressLatitudeDirection', cls=AddressLatitudeDirectionType)
@element(local_name='AddressLongitude', cls=AddressLongitudeType)
@element(local_name='AddressLongitudeDirection', cls=AddressLongitudeDirectionType)
@element(local_name='SupplementaryPostalServiceData', cls=SupplementaryPostalServiceDataType)
@element(local_name='*')
class PostalServiceElementsType(Model):
    pass
