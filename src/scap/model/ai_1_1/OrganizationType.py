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

from expatriate.model.decorators import *
from scap.model.xnl_2_0.OrganisationNameDetailsType import OrganisationNameDetailsType

from .AssetType import AssetType
from .EmailAddressType import EmailAddressType
from .TelephoneNumberType import TelephoneNumberType
from .WebsiteURLType import WebsiteURLType

logger = logging.getLogger(__name__)

@element(namespace='urn:oasis:names:tc:ciq:xsdschema:xNL:2.0', local_name='OrganisationNameDetails', list='organization_name_details', cls=OrganisationNameDetailsType, min=0, max=None)
@element(local_name='email-address', list='email_addresses', cls=EmailAddressType, min=0, max=None)
@element(local_name='telephone-number', list='telephone_numbers', cls=TelephoneNumberType, min=0, max=None)
@element(local_name='website-url', list='website_urls', cls=WebsiteURLType, min=0, max=None)
class OrganizationType(AssetType):
    pass
