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
import uuid

from scap.Model import Model
from scap.model.xccdf_1_1 import *

logger = logging.getLogger(__name__)
class TestResultType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'benchmark', 'class': 'BenchmarkReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'list': 'titles', 'class': 'TextType', 'min': 0, 'max': None},
            {'tag_name': 'remark', 'list': 'remarks', 'class': 'TextType', 'min': 0, 'max': None},
            {'tag_name': 'organization', 'list': 'organizations', 'type': 'StringType', 'min': 0, 'max': None},
            {'tag_name': 'identity', 'class': 'IdentityType', 'min': 0, 'max': 1},
            {'tag_name': 'profile', 'class': 'IdrefType', 'min': 0, 'max': 1},
            {'tag_name': 'target', 'list': 'targets', 'type': 'StringType', 'min': 1, 'max': None},
            {'tag_name': 'target-address', 'list': 'target_addresses', 'type': 'StringType', 'min': 0, 'max': None},
            {'tag_name': 'target-facts', 'class': 'TargetFactsType', 'min': 0, 'max': 1},
            {'tag_name': 'platform', 'list': 'platforms', 'class': 'UriIdrefType', 'min': 0, 'max': None},
            {'tag_name': 'set-value', 'dict': 'set_values', 'class': 'ProfileSetValueType', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'rule-result', 'dict': 'rule_results', 'class': 'RuleResultType', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'score', 'list': 'scores', 'class': 'ScoreType', 'min': 1, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'type': 'NCNameType', 'required': True},
            'start-time': {'type': 'DateTime'},
            'end-time': {'type': 'DateTime', 'required': True},
            'test-system': {'type': 'StringType'},
            'version': {'type': 'StringType'},
            'Id': {'type': 'ID'},
        },
    }

    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
