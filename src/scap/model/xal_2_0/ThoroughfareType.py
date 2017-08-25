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

from .PostalCodeType import PostalCodeType
from .FirmType import FirmType
from .PremiseType import PremiseType
from .DependentLocalityType import DependentLocalityType
from .DependentThoroughfareType import DependentThoroughfareType
from .ThoroughfarePostDirectionType import ThoroughfarePostDirectionType
from .ThoroughfareTrailingTypeType import ThoroughfareTrailingTypeType
from .ThoroughfareNameType import ThoroughfareNameType
from .ThoroughfareLeadingTypeType import ThoroughfareLeadingTypeType
from .ThoroughfarePreDirectionType import ThoroughfarePreDirectionType
from .ThoroughfareNumberSuffixType import ThoroughfareNumberSuffixType
from .ThoroughfareNumberPrefixType import ThoroughfareNumberPrefixType
from .ThoroughfareNumberRangeType import ThoroughfareNumberRangeType
from .ThoroughfareNumberType import ThoroughfareNumberType
from .AddressLineType import AddressLineType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='DependentThoroughfares', enum=['Yes', 'No'])
@attribute(local_name='DependentThoroughfaresIndicator', )
@attribute(local_name='DependentThoroughfaresConnector', )
@attribute(local_name='DependentThoroughfaresType', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='ThoroughfareNumber', into='thoroughfare_number', cls=ThoroughfareNumberType)
@element(local_name='ThoroughfareNumberRange', into='thoroughfare_number_range', cls=ThoroughfareNumberRangeType)
@element(local_name='ThoroughfareNumberPrefix', list='thoroughfare_number_prefixes', cls=ThoroughfareNumberPrefixType)
@element(local_name='ThoroughfareNumberSuffix', list='thoroughfare_number_suffixes', cls=ThoroughfareNumberSuffixType)
@element(local_name='ThoroughfarePreDirection', into='thoroughfare_pre_direction', cls=ThoroughfarePreDirectionType)
@element(local_name='ThoroughfareLeadingType', into='thoroughfare_leading_type', cls=ThoroughfareLeadingTypeType)
@element(local_name='ThoroughfareName', list='thoroughfare_names', cls=ThoroughfareNameType)
@element(local_name='ThoroughfareTrailingType', into='thoroughfare_trailing_type', cls=ThoroughfareTrailingTypeType)
@element(local_name='ThoroughfarePostDirection', into='thoroughfare_post_direction', cls=ThoroughfarePostDirectionType)
@element(local_name='DependentThoroughfare', into='dependent_thoroughfare', cls=DependentThoroughfareType)
@element(local_name='DependentLocality', into='dependent_locality', cls=DependentLocalityType)
@element(local_name='Premise', into='premise', cls=PremiseType)
@element(local_name='Firm', into='firm', cls=FirmType)
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='*')
class ThoroughfareType(Model):
    pass
