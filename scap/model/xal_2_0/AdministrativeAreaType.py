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
class AdministrativeAreaType(Model):
    MODEL_MAP = {
        'tag_name': 'AdministrativeArea',
        'elements': [
            {'tag_name': 'AddressLine', 'append': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'AdministrativeAreaName', 'append': 'administrative_areas', 'class': 'AdministrativeAreaNameType'},
            {'tag_name': 'SubAdministrativeArea', 'in': 'sub_administrative_area', 'class': 'SubAdministrativeAreaNameType'},
            {'tag_name': 'Locality', 'in': 'locality', 'class': 'LocalityType'},
            {'tag_name': 'PostOffice', 'in': 'post_office', 'class': 'PostOfficeType'},
            {'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},
            {'tag_name': '*'},
        ],
        'attributes': {
            'Type': {},
            'UsageType': {},
            'Indicator': {},
            '*': {},
        }
    }
