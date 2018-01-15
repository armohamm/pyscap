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
from .BuildingNameType import BuildingNameType
from .DepartmentType import DepartmentType
from .LargeMailUserIdentifierType import LargeMailUserIdentifierType
from .LargeMailUserNameType import LargeMailUserNameType
from .PostBoxType import PostBoxType
from .PostalCodeType import PostalCodeType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='LargeMailUserName', list='large_mail_user_names', cls=LargeMailUserNameType)
@element(local_name='LargeMailUserIdentifier', into='large_mail_user_identifier', cls=LargeMailUserIdentifierType)
@element(local_name='BuildingName', list='building_names', cls=BuildingNameType)
@element(local_name='Department', into='department', cls=DepartmentType)
@element(local_name='PostBox', into='post_box', cls=PostBoxType)
@element(local_name='Thoroughfare', into='thoroughfare', cls=defer_class_load('scap.model.xal_2_0.ThoroughfareType', 'ThoroughfareType'))
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='*')
class LargeMailUserType(Model):
    pass
