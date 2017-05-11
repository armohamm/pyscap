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
class ThoroughfareType(Model):
    MODEL_MAP = {
        'tag_name': 'Thoroughfare',
        'elements': [
            {'tag_name': 'AddressLine', 'list': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'ThoroughfareNumber', 'in': 'thoroughfare_number', 'class': 'ThoroughfareNumberType'},
            {'tag_name': 'ThoroughfareNumberRange', 'in': 'thoroughfare_number_range', 'class': 'ThoroughfareNumberRangeType'},
            {'tag_name': 'ThoroughfareNumberPrefix', 'list': 'thoroughfare_number_prefixes', 'class': 'ThoroughfareNumberPrefixType'},
            {'tag_name': 'ThoroughfareNumberSuffix', 'list': 'thoroughfare_number_suffixes', 'class': 'ThoroughfareNumberSuffixType'},
            {'tag_name': 'ThoroughfarePreDirection', 'in': 'thoroughfare_pre_direction', 'class': 'ThoroughfarePreDirectionType'},
            {'tag_name': 'ThoroughfareLeadingType', 'in': 'thoroughfare_leading_type', 'class': 'ThoroughfareLeadingTypeType'},
            {'tag_name': 'ThoroughfareName', 'list': 'thoroughfare_names', 'class': 'ThoroughfareNameType'},
            {'tag_name': 'ThoroughfareTrailingType', 'in': 'thoroughfare_trailing_type', 'class': 'ThoroughfareTrailingTypeType'},
            {'tag_name': 'ThoroughfarePostDirection', 'in': 'thoroughfare_post_direction', 'class': 'ThoroughfarePostDirectionType'},
            {'tag_name': 'DependentThoroughfare', 'in': 'dependent_thoroughfare', 'class': 'DependentThoroughfareType'},
            {'tag_name': 'DependentLocality', 'in': 'dependent_locality', 'class': 'DependentLocalityType'},
            {'tag_name': 'Premise', 'in': 'premise', 'class': 'PremiseType'},
            {'tag_name': 'Firm', 'in': 'firm', 'class': 'FirmType'},
            {'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},'*': {}
        ],
        'attributes': {
            'Type': {},
            'DependentThoroughfares': {'enum': ['Yes', 'No']},
            'DependentThoroughfaresIndicator': {},
            'DependentThoroughfaresConnector': {},
            'DependentThoroughfaresType': {},
            '*': {},
        },
    }
