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

from scap.model.ai_1_1.AssetType import AssetType
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class PersonType(AssetType):
    MODEL_MAP = {
        'tag_name': 'person',
        'elements': [
            {'xmlns': 'urn:oasis:names:tc:ciq:xsdschema:xNL:2.0', 'tag_name': 'PersonName', 'class': 'PersonNameType', 'min': 0},
            {'tag_name': 'email-address', 'list': 'email_addresses', 'class': 'EmailAddressType', 'min': 0, 'max': None},
            {'tag_name': 'telephone-number', 'list': 'telephone_numbers', 'class': 'TelephoneNumberType', 'min': 0, 'max': None},
            {'tag_name': 'birthdate', 'class': 'BirthdateType', 'min': 0},
        ],
    }
