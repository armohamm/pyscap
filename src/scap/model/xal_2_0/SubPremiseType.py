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
from .SubPremiseNameType import SubPremiseNameType
from .SubPremiseLocationType import SubPremiseLocationType
from .SubPremiseNumberType import SubPremiseNumberType
from .SubPremiseNumberPrefixType import SubPremiseNumberPrefixType
from .SubPremiseNumberSuffixType import SubPremiseNumberSuffixType
from .BuildingNameType import BuildingNameType
from .FirmType import FirmType
from .MailStopType import MailStopType
from .PostalCodeType import PostalCodeType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='SubPremiseName', list='sub_premise_names', cls=SubPremiseNameType)
@element(local_name='SubPremiseLocation', into='sub_premise_location', cls=SubPremiseLocationType)
@element(local_name='SubPremiseNumber', list='sub_premise_numbers', cls=SubPremiseNumberType)
@element(local_name='SubPremiseNumberPrefix', list='sub_premise_number_prefixes', cls=SubPremiseNumberPrefixType)
@element(local_name='SubPremiseNumberSuffix', list='sub_premise_number_suffixes', cls=SubPremiseNumberSuffixType)
@element(local_name='BuildingName', list='building_names', cls=BuildingNameType)
@element(local_name='Firm', into='firm', cls=FirmType)
@element(local_name='MailStop', into='firm', cls=MailStopType)
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='SubPremise', list='sub_premises', cls=defer_class_load('scap.model.xal_2_0.SubPremiseType', 'SubPremiseType'))
@element(local_name='*')
class SubPremiseType(Model):
    pass
