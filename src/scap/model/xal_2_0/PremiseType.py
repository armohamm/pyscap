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
from .BuildingNameType import BuildingNameType
from .FirmType import FirmType
from .MailStopType import MailStopType
from .PostalCodeType import PostalCodeType
from .PremiseLocationType import PremiseLocationType
from .PremiseNameType import PremiseNameType
from .PremiseNumberPrefixType import PremiseNumberPrefixType
from .PremiseNumberRangeType import PremiseNumberRangeType
from .PremiseNumberSuffixType import PremiseNumberSuffixType
from .PremiseNumberType import PremiseNumberType
from .SubPremiseType import SubPremiseType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='PremiseDependency', )
@attribute(local_name='PremiseDependencyType', )
@attribute(local_name='PremiseThoroughfareConnector', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='PremiseName', list='premise_names', cls=PremiseNameType)
@element(local_name='PremiseLocation', into='premise_location', cls=PremiseLocationType)
@element(local_name='PremiseNumber', list='premise_numbers', cls=PremiseNumberType)
@element(local_name='PremiseNumberRange', into='premise_number_range', cls=PremiseNumberRangeType)
@element(local_name='PremiseNumberPrefix', list='premise_number_prefixes', cls=PremiseNumberPrefixType)
@element(local_name='PremiseNumberSuffix', list='premise_number_suffixes', cls=PremiseNumberSuffixType)
@element(local_name='BuildingName', list='building_names', cls=BuildingNameType)
@element(local_name='SubPremise', list='sub_premises', cls=SubPremiseType)
@element(local_name='Firm', into='firm', cls=FirmType)
@element(local_name='MailStop', into='mail_stop', cls=MailStopType)
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='Premise', into='premise', cls=defer_class_load('scap.model.xal_2_0.PremiseType', 'PremiseType'))
@element(local_name='*')
class PremiseType(Model):
    pass
