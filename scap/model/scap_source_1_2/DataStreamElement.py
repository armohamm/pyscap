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
from scap.model.scap_source_1_2 import *

logger = logging.getLogger(__name__)
class DataStreamElement(Model):
    MODEL_MAP = {
        'tag_name': 'data-stream',
        'elements': [
            {'tag_name': 'dictionaries',  'class': 'RefListType', 'min': 0 },
            {'tag_name': 'checklists',  'class': 'RefListType', 'min': 0 },
            {'tag_name': 'checks',  'class': 'RefListType' },
            {'tag_name': 'extended-components', 'min': 0, 'class': 'RefListType' },
        ],
        'attributes': {
            'id': {'required': True, 'type': 'DataStreamIDPattern'},
            'use-case': {'required': True, 'enum': USE_CASE_ENUMERATION}, # TODO: spec also allows Token
            'scap-version': {'required': True, 'enum': SCAP_VERSION_ENUMERATION}, # TODO: spec also allows Token
            'timestamp': {'required': True, 'type': 'DateTime'},
        },
    }
