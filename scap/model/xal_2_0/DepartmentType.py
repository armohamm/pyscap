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
class DepartmentType(Model):
    MODEL_MAP = {
        'tag_name': 'Department',
        'elements': [
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'AddressLine', 'append': 'address_lines', 'class': 'AddressLineType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'DepartmentName', 'append': 'department_names', 'class': 'DepartmentNameType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'MailStop', 'in': 'mail_stop', 'class': 'MailStopType'},
            {'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', 'tag_name': 'PostalCode', 'in': 'postal_code', 'class': 'PostalCodeType'},
        ],
        'attributes': {
            'Type': {},
            '*': {},
        }
    }
