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
from scap.model.oval_5 import *
from scap.model.oval_5.res import *

logger = logging.getLogger(__name__)
class TestType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5', 'tag_name': 'message', 'list': 'messages', 'min': 0, 'max': None},
            {'tag_name': 'tested_item', 'list': 'tested_items', 'class': 'TestedItemType', 'min': 0, 'max': None},
            {'tag_name': 'tested_variable', 'list': 'tested_variables', 'class': 'TestedVariableType', 'min': 0, 'max': None},
        ],
        'attributes': {
            'test_id': {'type': 'scap.model.oval_5.TestIdPattern', 'required': True},
            'version': {'type': 'NonNegativeIntegerType', 'required': True},
            'variable_instance': {'type': 'NonNegativeIntegerType', 'default': 1},
            'check_existence': {'enum': EXISTENCE_ENUMERATION, 'default': 'at_least_one_exists'},
            'check': {'enum': CHECK_ENUMERATION, 'required': True},
            'state_operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'result': {'enum': RESULT_ENUMERATION, 'required': True},
        }
    }
