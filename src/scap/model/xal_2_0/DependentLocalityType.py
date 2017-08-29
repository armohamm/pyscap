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

from .AddressLineType import AddressLineType
from .DependentLocalityNumberType import DependentLocalityNumberType
from .LargeMailUserType import LargeMailUserType
from .LocalityNameType import LocalityNameType
from .PostBoxType import PostBoxType
from .PostOfficeType import PostOfficeType
from .PostalCodeType import PostalCodeType
from .PostalRouteType import PostalRouteType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='UsageType', )
@attribute(local_name='Connector', )
@attribute(local_name='Indicator', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='DependentLocalityName', list='address_lines', cls=LocalityNameType)
@element(local_name='DependentLocalityNumber', list='address_lines', cls=DependentLocalityNumberType)
@element(local_name='PostBox', into='post_box', cls=PostBoxType)
@element(local_name='LargeMailUser', into='large_mail_user', cls=LargeMailUserType)
@element(local_name='PostOffice', into='post_office', cls=PostOfficeType)
@element(local_name='PostalRoute', into='post_route', cls=PostalRouteType)
@element(local_name='Thoroughfare', into='thoroughfare', cls=defer_class_load('scap.model.xal_2_0.ThoroughfareType', 'ThoroughfareType'))
@element(local_name='Premise', into='premise', cls=defer_class_load('scap.model.xal_2_0.PremiseType', 'PremiseType'))
@element(local_name='DependentLocality', into='premise', cls=defer_class_load('scap.model.xal_2_0.DependentLocalityType', 'DependentLocalityType'))
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='*')
class DependentLocalityType(Model):
    pass
