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
from scap.model.xccdf_1_1 import *

logger = logging.getLogger(__name__)
class RuleResultType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'result', 'enum': RESULT_ENUMERATION, 'min': 1, 'max': 1},
            {'tag_name': 'override', 'list': 'overrides', 'class': 'OverrideType', 'min': 0, 'max': None},
            {'tag_name': 'ident', 'list': 'idents', 'class': 'IdentType', 'min': 0, 'max': None},
            {'tag_name': 'message', 'list': 'messages', 'class': 'MessageType', 'min': 0, 'max': None},
            {'tag_name': 'instance', 'list': 'instances', 'class': 'InstanceResultType', 'min': 0, 'max': None},
            {'tag_name': 'fix', 'list': 'fixes', 'class': 'FixType', 'min': 0, 'max': None},
            {'tag_name': 'check', 'list': 'checks', 'class': 'CheckType', 'min': 0, 'max': None},
        ],
        'attributes': {
            'idref': {'type': 'NCNameType', 'required': True},
            'role': {'enum': ROLE_ENUMERATION},
            'severity': {'enum': SEVERITY_ENUMERATION},
            'time': {'type': 'DateTimeType'},
            'version': {'type': 'StringType'},
            'weight': {'type': 'WeightType'},
        },
    }
