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

from scap.Model import Model
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class AddressDetailsType(Model):
    MODEL_MAP = {
        'tag_name': 'AddressDetails',
        'elements': [
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PostalServiceElements', 'class': 'PostalServiceElementsType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Address', 'class': 'AddressType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'AddressLines', 'class': 'AddressLinesType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Country', 'class': 'CountryType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'AdministrativeArea', 'class': 'AdministrativeAreaType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Locality', 'class': 'LocalityType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Thoroughfare', 'class': 'ThoroughfareType'},
        ],
        'attributes': {
            'AddressType': {},
            'CurrentStatus': {},
            'ValidFromDate': {},
            'ValidToDate': {},
            'Usage': {},
            'Code': {}, # from grPostal
            'AddressDetailsKey': {},
            '*': {},
        }
    }
