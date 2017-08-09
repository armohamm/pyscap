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

logger = logging.getLogger(__name__)
class PremiseType(Model):
    MODEL_MAP = {
        'tag_name': 'Premise',
        'elements': [
            {'tag_name': 'AddressLine', 'list': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'PremiseName', 'list': 'premise_names', 'class': 'PremiseNameType'},
            {'tag_name': 'PremiseLocation', 'in': 'premise_location', 'class': 'PremiseLocationType'},
            {'tag_name': 'PremiseNumber', 'list': 'premise_numbers', 'class': 'PremiseNumberType'},
            {'tag_name': 'PremiseNumberRange', 'in': 'premise_number_range', 'class': 'PremiseNumberRangeType'},
            {'tag_name': 'PremiseNumberPrefix', 'list': 'premise_number_prefixes', 'class': 'PremiseNumberPrefixType'},
            {'tag_name': 'PremiseNumberSuffix', 'list': 'premise_number_suffixes', 'class': 'PremiseNumberSuffixType'},
            {'tag_name': 'BuildingName', 'list': 'building_names', 'class': 'BuildingNameType'},
            {'tag_name': 'SubPremise', 'list': 'sub_premises', 'class': 'SubPremiseType'},
            {'tag_name': 'Firm', 'in': 'firm', 'class': 'FirmType'},
            {'tag_name': 'MailStop', 'in': 'mail_stop', 'class': 'MailStopType'},
            {'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},
            {'tag_name': 'Premise', 'in': 'premise', 'class': 'PremiseType'},
            {'tag_name': '*'},
        ],
        'attributes': {
            'Type': {},
            'PremiseDependency': {},
            'PremiseDependencyType': {},
            'PremiseThoroughfareConnector': {},
            '*': {},
        },
    }
