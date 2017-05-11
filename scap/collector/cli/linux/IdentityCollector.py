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

from scap.collector.cli.LinuxCollector import LinuxCollector
from scap.host.CLIHost import ElevationException

logger = logging.getLogger(__name__)
class IdentityCollector(LinuxCollector):
    def collect(self):
        if 'identity' in self.host.facts:
            return

        self.host.facts['identity'] = {}

        return_code, out_lines, err_lines = self.host.exec_command('id -un')
        self.host.facts['identity']['effective_user_name'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -u')
        self.host.facts['identity']['effective_user_id'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -gn')
        self.host.facts['identity']['effective_primary_group_name'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -g')
        self.host.facts['identity']['effective_primary_group_id'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -Gn')
        self.host.facts['identity']['effective_all_groups'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -G')
        self.host.facts['identity']['effective_all_group_ids'] = out_lines[0]

        return_code, out_lines, err_lines = self.host.exec_command('id -run')
        self.host.facts['identity']['real_user_name'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -ru')
        self.host.facts['identity']['real_user_id'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -rgn')
        self.host.facts['identity']['real_primary_group_name'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -rg')
        self.host.facts['identity']['real_primary_group_id'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -rGn')
        self.host.facts['identity']['real_all_groups'] = out_lines[0]
        return_code, out_lines, err_lines = self.host.exec_command('id -rG')
        self.host.facts['identity']['real_all_group_ids'] = out_lines[0]

        return_code, out_lines, err_lines = self.host.exec_command('id -Z')
        if len(out_lines) > 0:
            self.host.facts['identity']['security_context'] = out_lines[0]

        self.host.facts['identity']['authenticated'] = True
        self.host.facts['identity']['name'] = self.host.facts['identity']['effective_user_name']

        return_code, out_lines, err_lines = self.host.exec_command('whoami', sudo=True)
        if return_code == 0 and out_lines[0] == 'root':
            self.host.facts['identity']['privileged'] = True
        else:
            self.host.facts['identity']['privileged'] = False
