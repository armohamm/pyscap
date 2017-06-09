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
from scap.model.xccdf_1_2 import *

logger = logging.getLogger(__name__)
class RuleResultType(Model):
    MODEL_MAP = {
        'attributes': {
            'idref': {'type': 'NCNameType', 'required': True},
            'role': {'enum': ROLE_ENUMERATION},
            'severity': {'enum': SEVERITY_ENUMERATION},
            'time': {'type': 'DateTime'},
            'version': {'type': 'StringType'},
            'weight': {'type': 'Weight'},
        },
        'elements': [
            {'tag_name': 'result', 'enum': RESULT_ENUMERATION, 'min': 1, 'max': 1},
            {'tag_name': 'override', 'class': 'OverrideType', 'list': 'overrides', 'min': 0, 'max': None},
            {'tag_name': 'ident', 'class': 'IdentType', 'list': 'idents', 'min': 0, 'max': None},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'list': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'message', 'class': 'MessageType', 'list': 'messages', 'min': 0, 'max': None},
            {'tag_name': 'instance', 'class': 'InstanceResultType', 'list': 'instances', 'min': 0, 'max': None},
            {'tag_name': 'fix', 'class': 'FixType', 'list': 'fixes', 'min': 0, 'max': None},
            {'tag_name': 'check', 'class': 'CheckType', 'list': 'checks', 'min': 0, 'max': None},
            {'tag_name': 'complex-check', 'class': 'ComplexCheckType', 'min': 0, 'max': 1},
        ],
    }
