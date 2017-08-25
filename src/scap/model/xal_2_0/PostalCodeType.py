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
from .PostCodeNumberType import PostCodeNumberType
from .PostalCodeNumberExtensionType import PostalCodeNumberExtensionType
from .PostTownType import PostTownType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='PostalCodeNumber', list='postal_code_numbers', cls=PostCodeNumberType)
@element(local_name='PostalCodeNumberExtension', list='postal_code_number_extensions', cls=PostalCodeNumberExtensionType)
@element(local_name='PostTown', into='post_town', cls=PostTownType)
@element(local_name='*')
class PostalCodeType(Model):
    pass
