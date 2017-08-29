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
from .FirmType import FirmType
from .PostBoxNumberExtensionType import PostBoxNumberExtensionType
from .PostBoxNumberPrefixType import PostBoxNumberPrefixType
from .PostBoxNumberSuffixType import PostBoxNumberSuffixType
from .PostBoxNumberType import PostBoxNumberType
from .PostalCodeType import PostalCodeType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='Indicator', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='PostBoxNumber', into='post_box_number', cls=PostBoxNumberType)
@element(local_name='PostBoxNumberPrefix', into='post_box_number_prefix', cls=PostBoxNumberPrefixType)
@element(local_name='PostBoxNumberSuffix', into='post_box_number_suffix', cls=PostBoxNumberSuffixType)
@element(local_name='PostBoxNumberExtension', into='post_box_number_extension', cls=PostBoxNumberExtensionType)
@element(local_name='Firm', into='firm', cls=FirmType)
@element(local_name='PostalCode', into='postal_code', cls=PostalCodeType)
@element(local_name='*')
class PostBoxType(Model):
    pass
