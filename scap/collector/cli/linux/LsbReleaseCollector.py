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

import re
import logging

from scap.collector.cli.LinuxCollector import LinuxCollector
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class LsbReleaseCollector(LinuxCollector):
    def collect(self):
        try:
            return_code, out_lines, err_lines = self.host.exec_command('lsb_release -a')
        except:
            return

        cpe = CPE(part='o')
        for line in out_lines:
            m = re.match(r'^([^:]+):\s+(.+)$', line)
            if m:
                name = m.group(1)
                value = m.group(2)

                if name == 'Distributor ID':
                    if re.match(r'^RedHat', value):
                        cpe.set_value('vendor', 'redhat')
                    elif re.match(r'Debian', value):
                        cpe.set_value('vendor', 'debian')
                    elif re.match(r'LinuxMint', value):
                        cpe.set_value('vendor', 'linuxmint')
                        cpe.set_value('product', 'linux_mint')
                    elif re.match(r'Arch', value):
                        cpe.set_value('vendor', 'archlinux')
                        cpe.set_value('product', 'archlinux')
                    elif re.match(r'openSUSE project', value):
                        cpe.set_value('vendor', 'opensuse_project')
                        cpe.set_value('product', 'opensuse_project')
                    elif re.match(r'Ubuntu', value):
                        cpe.set_value('vendor', 'ubuntu')
                        cpe.set_value('product', 'ubuntu')
                    elif re.match(r'CentOS', value):
                        cpe.set_value('vendor', 'centos')
                        cpe.set_value('product', 'centos')

                elif name == 'Description':
                    vendor = cpe.get_value('vendor')
                    if vendor == 'redhat':
                        if re.match(r'^Enterprise Linux', value):
                            cpe.set_value('product', 'enterprise_linux')

                elif name == 'Release':
                    cpe.set_value('version', value)

        if 'cpe' not in self.host.facts:
            self.host.facts['cpe'] = {'os':[], 'application':[], 'hardware':[]}

        if cpe not in self.host.facts['cpe']['os']:
            self.host.facts['cpe']['os'].append(cpe)
