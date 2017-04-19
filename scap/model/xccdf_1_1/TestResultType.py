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

logger = logging.getLogger(__name__)
class TestResultType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}benchmark': {'class': 'BenchmarkReferenceType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'class': 'TextType', 'append': 'titles', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}remark': {'class': 'TextType', 'append': 'remarks', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}organization': {'type': 'String', 'append': 'organizations', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}identity': {'class': 'IdentityType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}profile': {'class': 'IdrefType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}target': {'type': 'String', 'append': 'targets', 'min': 1, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}target-address': {'type': 'String', 'append': 'target_addresses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}target-facts': {'class': 'TargetFactsType', 'append': 'target_facts', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}platform': {'class': 'UriIdrefType', 'append': 'platforms', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}set-value': {'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}rule-result': {'class': 'RuleResultType', 'map': 'rule_results', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}score': {'class': 'ScoreType', 'append': 'scores', 'min': 1, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            'start-time': {'type': 'DateTime'},
            'end-time': {'type': 'DateTime', 'required': True},
            'test-system': {'type': 'String'},
            'version': {'type': 'String'},
            'Id': {'ignore': True, 'type': 'ID'},
        },
    }

    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
