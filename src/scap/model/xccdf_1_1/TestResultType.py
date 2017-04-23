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
        'elements': [
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'benchmark', 'class': 'BenchmarkReferenceType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'title', 'class': 'TextType', 'append': 'titles', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'remark', 'class': 'TextType', 'append': 'remarks', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'organization', 'type': 'String', 'append': 'organizations', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'identity', 'class': 'IdentityType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'profile', 'class': 'IdrefType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'target', 'type': 'String', 'append': 'targets', 'min': 1, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'target-address', 'type': 'String', 'append': 'target_addresses', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'target-facts', 'class': 'TargetFactsType', 'append': 'target_facts', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'platform', 'class': 'UriIdrefType', 'append': 'platforms', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'set-value', 'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'rule-result', 'class': 'RuleResultType', 'map': 'rule_results', 'key': 'idref', 'min': 0, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'score', 'class': 'ScoreType', 'append': 'scores', 'min': 1, 'max': None},
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            'start-time': {'type': 'DateTime'},
            'end-time': {'type': 'DateTime', 'required': True},
            'test-system': {'type': 'String'},
            'version': {'type': 'String'},
            'Id': {'type': 'ID'},
        },
    }

    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
