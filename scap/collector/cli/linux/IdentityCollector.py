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

        self.host.facts['identity']['effective_user_name'] = self.host.exec_command('id -un')[0]
        self.host.facts['identity']['effective_user_id'] = self.host.exec_command('id -u')[0]
        self.host.facts['identity']['effective_primary_group_name'] = self.host.exec_command('id -gn')[0]
        self.host.facts['identity']['effective_primary_group_id'] = self.host.exec_command('id -g')[0]
        self.host.facts['identity']['effective_all_groups'] = self.host.exec_command('id -Gn')[0]
        self.host.facts['identity']['effective_all_group_ids'] = self.host.exec_command('id -G')[0]

        self.host.facts['identity']['real_user_name'] = self.host.exec_command('id -run')[0]
        self.host.facts['identity']['real_user_id'] = self.host.exec_command('id -ru')[0]
        self.host.facts['identity']['real_primary_group_name'] = self.host.exec_command('id -rgn')[0]
        self.host.facts['identity']['real_primary_group_id'] = self.host.exec_command('id -rg')[0]
        self.host.facts['identity']['real_all_groups'] = self.host.exec_command('id -rGn')[0]
        self.host.facts['identity']['real_all_group_ids'] = self.host.exec_command('id -rG')[0]

        self.host.facts['identity']['security_context'] = self.host.exec_command('id -Z')[0]

        self.host.facts['identity']['authenticated'] = True
        self.host.facts['identity']['name'] = self.host.facts['identity']['effective_user_name']

        try:
            self.host.exec_command('su', sudo=True)
            self.host.facts['identity']['privileged'] = True
        except ElevationException:
            self.host.facts['identity']['privileged'] = False
