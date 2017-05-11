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
class SubPremiseType(Model):
    MODEL_MAP = {
        'tag_name': 'SubPremise',
        'elements': [
            {'tag_name': 'AddressLine', 'list': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'SubPremiseName', 'list': 'sub_premise_names', 'class': 'SubPremiseNameType'},
            {'tag_name': 'SubPremiseLocation', 'in': 'sub_premise_location', 'class': 'SubPremiseLocationType'},
            {'tag_name': 'SubPremiseNumber', 'list': 'sub_premise_numbers', 'class': 'SubPremiseNumberType'},
            {'tag_name': 'SubPremiseNumberPrefix', 'list': 'sub_premise_number_prefixes', 'class': 'SubPremiseNumberPrefixType'},
            {'tag_name': 'SubPremiseNumberSuffix', 'list': 'sub_premise_number_suffixes', 'class': 'SubPremiseNumberSuffixType'},
            {'tag_name': 'BuildingName', 'list': 'building_names', 'class': 'BuildingNameType'},
            {'tag_name': 'Firm', 'in': 'firm', 'class': 'FirmType'},
            {'tag_name': 'MailStop', 'in': 'firm', 'class': 'MailStopType'},
            {'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},
            {'tag_name': 'SubPremise', 'list': 'sub_premises', 'class': 'SubPremiseType'},'*': {},
        ],
        'attributes': {
            'Type': {},
            '*': {},
        },
    }
