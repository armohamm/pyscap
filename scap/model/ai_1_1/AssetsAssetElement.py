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
class AssetsAssetElement(Model):
    MODEL_MAP = {
        'tag_name': 'asset',
        'elements': [
            {'tag_name': 'circuit', 'in': 'asset', 'class': 'CircuitType'},
            {'tag_name': 'computing-device', 'in': 'asset', 'class': 'ComputingDeviceType'},
            {'tag_name': 'data', 'in': 'asset', 'class': 'DataType'},
            {'tag_name': 'database', 'in': 'asset', 'class': 'DatabaseType'},
            {'tag_name': 'network', 'in': 'asset', 'class': 'NetworkType'},
            {'tag_name': 'organization', 'in': 'asset', 'class': 'OrganizationType'},
            {'tag_name': 'person', 'in': 'asset', 'class': 'PersonType'},
            {'tag_name': 'service', 'in': 'asset', 'class': 'ServiceType'},
            {'tag_name': 'software', 'in': 'asset', 'class': 'SoftwareType'},
            {'tag_name': 'system', 'in': 'asset', 'class': 'SystemType'},
            {'tag_name': 'website', 'in': 'asset', 'class': 'WebsiteType'},
        ],
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            '*': {},
        }
    }
