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
class PostalServiceElementsType(Model):
    MODEL_MAP = {
        'tag_name': 'PostalServiceElements',
        'elements': [
            {'tag_name': 'AddressIdentifier', 'list': 'address_identifiers', 'class': 'AddressIdentifierType'},
            {'tag_name': 'EndorsementLineCode', 'class': 'EndorsementLineCodeType'},
            {'tag_name': 'KeyLineCode', 'class': 'KeyLineCodeType'},
            {'tag_name': 'Barcode', 'class': 'BarcodeType'},
            {'tag_name': 'SortingCode', 'class': 'SortingCodeType'},
            {'tag_name': 'AddressLatitude', 'class': 'AddressLatitudeType'},
            {'tag_name': 'AddressLatitudeDirection', 'class': 'AddressLatitudeDirectionType'},
            {'tag_name': 'AddressLongitude', 'class': 'AddressLongitudeType'},
            {'tag_name': 'AddressLongitudeDirection', 'class': 'AddressLongitudeDirectionType'},
            {'tag_name': 'SupplementaryPostalServiceData', 'class': 'SupplementaryPostalServiceDataType'},
            {'tag_name': '*'},
        ],
        'attributes': {
            'Type': {},
            '*': {},
        }
    }
