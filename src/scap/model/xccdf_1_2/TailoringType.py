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

import logging

from scap.Model import Model

logger = logging.getLogger(__name__)
class TailoringType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'TailoringIdPattern', 'required': True},
            'Id': {'type': 'ID'},
        },
        'elements': [
            {'tag_name': 'benchmark', 'class': 'TailoringBenchmarkReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'status', 'class': 'StatusType', 'list': 'statuses', 'min': 0, 'max': None},
            {'tag_name': 'dc-status', 'class': 'DcStatusType', 'list': 'dc_statuses', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'TailoringVersionType', 'min': 1, 'max': 1},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'list': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'Profile', 'class': 'ProfileType', 'list': 'profiles', 'min': 1, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': None},
        ],
    }
