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

from scap.model.ai_1_1.ITAssetType import ITAssetType
import logging

logger = logging.getLogger(__name__)
class ComputingDeviceType(ITAssetType):
    MODEL_MAP = {
        'tag_name': 'computing-device',
        'elements': [
            {'tag_name': 'distinguished-name', 'class': 'DistinguishedNameType', 'min': 0},
            {'tag_name': 'cpe', 'list': 'cpes', 'class': 'CPEType', 'min': 0, 'max': None},
            {'tag_name': 'connections', 'class': 'ConnectionsType', 'min': 0},
            {'tag_name': 'fqdn', 'class': 'FQDNType', 'min': 0},
            {'tag_name': 'hostname', 'class': 'ComputingDeviceHostnameType', 'min': 0},
            {'tag_name': 'motherboard-guid', 'class': 'MotherboardGUIDType', 'min': 0},
        ],
    }
    #TODO: cpes as fs_string
