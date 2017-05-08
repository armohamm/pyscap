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

from scap.collector.cli.WindowsCollector import WindowsCollector

logger = logging.getLogger(__name__)
class IdentityCollector(WindowsCollector):
    def collect(self):
        if 'identity' in self.host.facts:
            return

        self.host.facts['identity'] = {}

        self.host.facts['identity']['user_name'] = self.host.exec_command('echo %USERNAME%')[0]
        try:
            self.host.facts['identity']['user_dns_domain'] = self.host.exec_command('echo %USERDNSDOMAIN%')[0]
        except:
            pass
        try:
            self.host.facts['identity']['user_domain'] = self.host.exec_command('echo %USERDOMAIN%')[0]
        except:
            pass
        self.host.facts['identity']['computer_name'] = self.host.exec_command('echo %COMPUTERNAME%')[0]

        self.host.facts['identity']['authenticated'] = True
        self.host.facts['identity']['name'] = self.host.facts['identity']['user_name']

        # try:
        #     self.host.exec_command('su', elevate=True)
        #     self.host.facts['identity']['privileged'] = True
        # except ElevationException:
        self.host.facts['identity']['privileged'] = False
