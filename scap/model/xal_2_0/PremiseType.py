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
class PremiseType(Model):
    MODEL_MAP = {
        'tag_name': 'Premise',
        'elements': [
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'AddressLine', 'append': 'address_lines', 'class': 'AddressLineType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseName', 'append': 'premise_names', 'class': 'PremiseNameType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseLocation', 'in': 'premise_location', 'class': 'PremiseLocationType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseNumber', 'append': 'premise_numbers', 'class': 'PremiseNumberType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseNumberRange', 'in': 'premise_number_range', 'class': 'PremiseNumberRangeType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseNumberPrefix', 'append': 'premise_number_prefixes', 'class': 'PremiseNumberPrefixType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PremiseNumberSuffix', 'append': 'premise_number_suffixes', 'class': 'PremiseNumberSuffixType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'BuildingName', 'append': 'building_names', 'class': 'BuildingNameType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'SubPremise', 'append': 'sub_premises', 'class': 'SubPremiseType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Firm', 'in': 'firm', 'class': 'FirmType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'MailStop', 'in': 'mail_stop', 'class': 'MailStopType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'Premise', 'in': 'premise', 'class': 'PremiseType'},'*': {},
        ],
        'attributes': {
            'Type': {},
            'PremiseDependency': {},
            'PremiseDependencyType': {},
            'PremiseThoroughfareConnector': {},
            '*': {},
        },
    }
