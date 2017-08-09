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
class TestResultType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'TestResultIdPattern'},
            'start-time': {'type': 'DateTimeType'},
            'end-time': {'type': 'DateTimeType'},
            'test-system': {'type': 'StringType'},
            'version': {'type': 'StringType'},
            'Id': {'type': 'ID'},
        },
        'elements': [
            {'tag_name': 'benchmark', 'class': 'BenchmarkReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'tailoring-file', 'class': 'TailoringReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'class': 'TextType', 'list': 'titles', 'min': 0, 'max': None},
            {'tag_name': 'remark', 'class': 'TextType', 'list': 'remarks', 'min': 0, 'max': None},
            {'tag_name': 'organization', 'type': 'StringType', 'list': 'organizations', 'min': 0, 'max': None},
            {'tag_name': 'identity', 'class': 'IdentityType', 'min': 0, 'max': 1},
            {'tag_name': 'profile', 'class': 'IdRefType', 'min': 0, 'max': 1},
            {'tag_name': 'target', 'type': 'StringType', 'list': 'targets', 'min': 1, 'max': None},
            {'tag_name': 'target-address', 'type': 'StringType', 'list': 'target_addresses', 'min': 0, 'max': None},
            {'tag_name': 'target-facts', 'class': 'TargetFactsType', 'list': 'target_facts', 'min': 0, 'max': None},
            {'tag_name': 'target-id-ref', 'class': 'TargetIdRefType', 'list': 'target_id_refs', 'min': 0, 'max': None},{'tag_name': '*', 'min': 0, 'max': None},
            {'tag_name': 'platform', 'class': 'Cpe2IdRefType', 'list': 'platforms', 'min': 0, 'max': None},
            {'tag_name': 'set-value', 'class': 'ProfileSetValueType', 'dict': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-complex-value', 'class': 'ProfileSetComplexValueType', 'dict': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'rule-result', 'class': 'RuleResultType', 'dict': 'rule_results', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'score', 'class': 'ScoreType', 'list': 'scores', 'min': 1, 'max': None},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'list': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
    }

    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
