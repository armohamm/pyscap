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

from scap.collector.cli.IdentityCollector import IdentityCollector as Col
from scap.host.CLIHost import ElevationException

logger = logging.getLogger(__name__)
class IdentityCollector(Col):
    def collect(self):
        if 'identity' in self.host.facts:
            return

        self.host.facts['identity'] = {}

        return_code, out_lines, err_lines = self.host.exec_command('echo %USERNAME%')
        self.host.facts['identity']['user_name'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('echo %COMPUTERNAME%')
        self.host.facts['identity']['computer_name'] = out_lines[0]
        self.host.facts['identity']['authenticated'] = True

        try:
            return_code, out_lines, err_lines = self.host.exec_command('echo %USERDNSDOMAIN%')
            self.host.facts['identity']['user_dns_domain'] = out_lines[0]
            self.host.facts['identity']['name'] = self.host.facts['identity']['user_name'] + '@' + self.host.facts['identity']['user_dns_domain']
        except:
            pass

        try:
            return_code, out_lines, err_lines = self.host.exec_command('echo %USERDOMAIN%')
            self.host.facts['identity']['user_domain'] = out_lines[0]
            self.host.facts['identity']['name'] = self.host.facts['identity']['user_domain'] + '\\' + self.host.facts['identity']['user_name']
        except:
            pass

        if 'name' not in self.host.facts['identity']:
            # must be local account
            self.host.facts['identity']['name'] = self.host.facts['identity']['computer_name'] + '\\' + self.host.facts['identity']['user_name']

        return_code, out_lines, err_lines = self.host.exec_command('"%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system" >nul 2>&1')
        if return_code == 0:
            self.host.facts['identity']['privileged'] = True
        else:
            self.host.facts['identity']['privileged'] = False
