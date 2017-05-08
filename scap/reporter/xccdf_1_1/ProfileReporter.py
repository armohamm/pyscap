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

from scap import VERSION
from scap.Reporter import Reporter

from scap.model.xccdf_1_1.TestResultType import TestResultType
from scap.model.xccdf_1_1.TextType import TextType
from scap.model.xccdf_1_1.IdentityType import IdentityType
from scap.model.xccdf_1_1.ProfileSetValueType import ProfileSetValueType
from scap.model.xccdf_1_1.IdrefType import IdrefType
from scap.model.xccdf_1_1.ScoreType import ScoreType

from scap.model.xs.String import String

logger = logging.getLogger(__name__)
class ProfileReporter(Reporter):
    def report(self, host, benchmark_id):
        profile_facts = host.facts['checklist'][benchmark_id]['profile'][self.model.id]

        test_result = TestResultType(tag_name='TestResult')

        # attributes
        test_result.id = TestResultType.generate_id()

        test_result.start_time = profile_facts['start_time']

        test_result.end_time = profile_facts['end_time']

        test_result.test_system = 'pyscap ' + VERSION

        test_result.Id = test_result.id

        # elements
        t = TextType(tag_name='title')
        t.text = 'Results for ' + host.hostname + ', profile ' + self.model.id
        test_result.titles.append(t)

        # TODO test_result.remarks.append()

        # TODO test_result.organizations.append()

        if 'identity' in host.facts:
            test_result.identity = IdentityType(tag_name='identity')
            test_result.identity.text = host.facts['identity']['name']
            if 'authenticated' in host.facts['identity']:
                test_result.identity.authenticated = str(host.facts['identity']['authenticated'])
            if 'privileged' in host.facts['identity']:
                test_result.identity.privileged = str(host.facts['identity']['privileged'])

        test_result.profile = IdrefType(tag_name='profile')
        test_result.profile.idref = self.model.id

        test_result.targets.append(String(value=host.hostname, tag_name='target'))

        # TODO test_result.target_addresses =

        # TODO test_result.target_facts =
        # pass off to TargetFactsType

        # TODO test_result.platforms =

        for value_id, value in profile_facts['value']:
            sv = ProfileSetValueType(tag_name='set-value')
            sv.type = value_id
            sv.value = value['value']
            test_result.set_values.append(sv)

        # TODO test_result.rule_results =

        for score in profile_facts['scores']:
            s = ScoreType(tag_name='score', value=score['score'])
            s.system = score['system']
            if 'max_score' in score:
                s.maximum = score['max_score']
            test_result.scores.append(s)

        # TODO signature

        return test_result
