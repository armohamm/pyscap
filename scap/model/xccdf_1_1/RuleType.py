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

import datetime
import logging
import os.path
import shutil
import sys

from scap.Model import Model

from scap.model.xccdf_1_1.SelectableItemType import SelectableItemType
from scap.model.xccdf_1_1.RoleEnumeration import ROLE_ENUMERATION
from scap.model.xccdf_1_1.SeverityEnumeration import SEVERITY_ENUMERATION
from scap.model.xccdf_1_1.ScoringModelEnumeration import SCORING_MODEL_ENUMERATION
from scap.model.xccdf_1_1.RuleResultType import RuleResultType
from scap.model.xccdf_1_1.OverrideType import OverrideType
from scap.model.xccdf_1_1.IdentType import IdentType
from scap.model.xccdf_1_1.MessageType import MessageType
from scap.model.xccdf_1_1.InstanceResultType import InstanceResultType
from scap.model.xccdf_1_1.FixType import FixType
from scap.model.xccdf_1_1.CheckType import CheckType

logger = logging.getLogger(__name__)
class RuleType(SelectableItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'ident', 'list': 'idents', 'min': 0, 'max': None, 'class': 'IdentType'},
            {'tag_name': 'impact-metric', 'min': 0, 'max': 1, 'type': 'String'},
            {'tag_name': 'profile-note', 'list': 'profile_notes', 'min': 0, 'max': None, 'class': 'ProfileNoteType'},
            {'tag_name': 'fixtext', 'class': 'FixtextType', 'min': 0, 'max': None, 'list': 'fixtexts'},
            {'tag_name': 'fix', 'class': 'FixType', 'min': 0, 'max': None, 'list': 'fixes'},# choice
            {'tag_name': 'check', 'class': 'CheckType', 'min': 0, 'max': None, 'dict': 'checks', 'key': 'selector'},
            {'tag_name': 'complex-check', 'class': 'ComplexCheckType', 'min': 0, 'max': 1},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'role': {'enum': ROLE_ENUMERATION, 'default': 'full'},
            'severity': {'enum': SEVERITY_ENUMERATION, 'default': 'unknown'},
            'multiple': {'type': 'Boolean', 'default': False},
        },
    }

    def __init__(self):
        super(RuleType, self).__init__()

        self.check_selector = None

    def _check(self, benchmark, host):
        check = None
        if len(self.checks) != 0:
            if self.check_selector in self.checks:
                check = self.checks[self.check_selector]
            else:
                check = self.checks['']
        elif self.complex_check is not None:
            check = self.complex_check

        check_result = {
            'result': 'notchecked',
            'messages': [
                MessageType(
                    tag_name='message',
                    value='No applicable checks found',
                    severity='error'
                ),
            ],
            'imports': {},
        }
        if check is None:
            for ext in ['.sh', '.ps1', '.bat']:
                path = os.path.join('script', 'check', benchmark.id, self.id + ext)
                if os.path.isfile(path):
                    logger.debug('Found check script: ' + path)
                    # TODO transfer script & get results
        else:
            # call the check
            logger.debug('Running check ' + str(check))
            check_result = check.check(benchmark, host)

        check_result['check'] = check
        check_result['fix'] = None

        logger.debug('Check result: ' + str(check_result))
        return check_result

    def process(self, host, benchmark, profile_id):
        super(RuleType, self).process(benchmark, host, profile_id)

        if not self._continue_processing():
            return

        ### Rule.Content

        # If the Item is a Rule, then process the properties of the Rule.

        # TODO check that if this group has a platform identified, that the
        # target system matches

        logger.debug('Checking for ' + str(self))
        try:
            check_result = self._check(benchmark, host)
        except:
            type_, value = sys.exc_info()[0:2]
            check_result = {
                'result': 'error',
                'messages': [
                    MessageType(
                        tag_name='message',
                        value='Exception while checking ' + str(self) + ': ' + str(type_) + ': ' + str(value),
                        severity='error'
                    ),
                ],
                'imports': {},
                'check': None,
                'fix': None,
            }

        # if it fails and there's a fix available
        if check_result['result'] == 'fail':
            for fix in self.fixes:
                # call the fix
                logger.debug('Attempting to fix with ' + str(fix))
                fix.fix(benchmark, host)

                # call the check again
                check_result = self._check(benchmark, host)

                # if successful, mark as fixed
                if check_result['result'] == 'pass':
                    check_result['result'] = 'fixed'
                    check_result['fix'] = fix
                    break

        # if no fixes worked/are available, check if we have a script available
        if check_result['result'] == 'fail':
            for ext in ['.sh', '.ps1', '.bat']:
                path = os.path.join('script', 'fix', benchmark.id, self.id + ext)
                if os.path.isfile(path):
                    logger.debug('Found fix script: ' + path)
                    # TODO transfer script & run

                    # call the check again
                    check_result = self._check(benchmark, host)

                    # if successful, mark as fixed
                    if check_result['result'] == 'pass':
                        check_result['result'] = 'fixed'
                        break

        rule_result = RuleResultType(tag_name='rule-result')
        rule_result.idref = self.id
        rule_result.role = self.role
        rule_result.severity = self.severity
        rule_result.time = datetime.datetime.utcnow()
        rule_result.version = self.version
        rule_result.weight = self.weight

        rule_result.result = check_result['result']
        # TODO overrides
        rule_result.idents = self.idents.copy()
        rule_result.messages = check_result['messages'].copy()
        # TODO instance
        if check_result['fix'] is not None:
            rule_result.fixes.append(check_result['fix'])
        if check_result['check'] is not None:
            rule_result.checks.append(check_result['check'])

        # result retention
        logger.debug('Rule result: ' + str(check_result))
        host.facts['checklist'][benchmark.id]['profile'][profile_id]['rule'][self.id] = rule_result

    def score(self, host, benchmark, profile_id, model_system):
        ### Score.Rule

        # If the node is a Rule, then assign a count of 1, and if the test
        # result is ‘pass’, assign the node a score of 100, otherwise assign a
        # score of 0.

        rule_result = host.facts['checklist'][benchmark.id]['profile'][profile_id]['rule'][self.id]
        if rule_result.result in ['pass', 'fixed']:
            return {
                self.id: {
                    'result': rule_result.result,
                    'model': model_system,
                    'score': 100.0,
                    'weight': rule_result.weight,
                    'count': 1,
                },
            }
        elif rule_result.result in ['error', 'unknown']:
            return {
                self.id: {
                    'result': rule_result.result,
                    'model': model_system,
                    'score': 0.0,
                    'weight': rule_result.weight,
                    'count': 1,
                },
            }
        else:
            return {
                self.id: {
                    'result': rule_result.result,
                    'model': model_system,
                    'score': None,
                    'weight': rule_result.weight,
                    'count': 1,
                },
            }
