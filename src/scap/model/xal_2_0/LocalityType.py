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
from .DependentLocalityType import DependentLocalityType
from .LargeMailUserType import LargeMailUserType
from .LocalityNameType import LocalityNameType
from .PostBoxType import PostBoxType
from .PostOfficeType import PostOfficeType
from .PostalCodeType import PostalCodeType
from .PostalRouteType import PostalRouteType
from .PremiseType import PremiseType
from .ThoroughfareType import ThoroughfareType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='UsageType', )
@attribute(local_name='Indicator', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='LocalityName', list='address_lines', cls=LocalityNameType)
@element(local_name='PostBox', into='post_box', cls=PostBoxType)
@element(local_name='LargeMailUser', into='large_mail_user', cls=LargeMailUserType)
@element(local_name='PostOffice', into='post_office', cls=PostOfficeType)
@element(local_name='PostalRoute', into='post_route', cls=PostalRouteType)
@element(local_name='Thoroughfare', into='thoroughfare', cls=ThoroughfareType)
@element(local_name='Premise', into='premise', cls=PremiseType)
@element(local_name='DependentLocality', into='premise', cls=DependentLocalityType)
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='*')
class LocalityType(Model):
    pass
