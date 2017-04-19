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

from scap.Reporter import Reporter
import logging

logger = logging.getLogger(__name__)
class BenchmarkReporter(Reporter):
    def __init__(self, hosts, args, model):
        super(BenchmarkReporter, self).__init__(hosts, args, model)

        self.test_result = TestResultType()
        self.test_result.id = TestResultType.generate_id()
        self.test_result.start_time =
        self.test_result.end_time =
        self.test_result.test_system =
        # TODO Id

        self.test_result.targets =
        self.test_result.titles =
        self.test_result.remarks =
        self.test_result.organizations =
        self.test_result.identity =
        self.test_result.profile =
        self.test_result.targets =
        self.test_result.target_addresses =
        self.test_result.target_facts =
        self.test_result.platforms =
        self.test_result.set_values =
        self.test_result.rule_results =
        self.test_result.scores =
        # TODO signature

    def report(self):
        return self.test_result.to_xml()
