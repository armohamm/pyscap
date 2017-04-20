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

from scap.Reporter import Reporter

from scap.reporter.xccdf_1_1.ProfileReporter import ProfileReporter

logger = logging.getLogger(__name__)
class BenchmarkReporter(Reporter):
    def report(self, hosts):
        for host in hosts:
            for profile_id in self.model.selected_profiles:
                test_result = ProfileReporter(self.args, self.model.profiles[profile_id]).report(host, self.model.id)
                self.model.test_results[test_result.id] = test_result
        return self.model.to_xml()
