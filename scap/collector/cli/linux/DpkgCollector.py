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
import re

from scap.Collector import Collector
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class DpkgCollector(Collector):
    def collect(self):
        return_code, out_lines, err_lines = self.host.exec_command('dpkg --list')
        for line in out_lines:
            m = re.match(r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)$', line)
            if not m:
                continue
            state, name, version, arch, desc = m.group(1,2,3,4,5)
            if ':' in name:
                name, arch2 = name.split(':')
            if '-' in version:
                version, dist_version = version.split('-', 1)

            # knock out some low hanging fruit to skip
            if True in [name.startswith(x) for x in [
                'python-',
                'python3-',
                'printer-driver-',
                'xserver-xorg-',
                'fonts-',
            ]]:
                continue

            if name.startswith('lib') and True not in [name.startswith(x) for x in [
                'libreoffice',
                'librecad',
            ]]:
                continue

            if True in [name.endswith(x) for x in [
                '-java',
                '-perl',
                '-common',
                '-dev',
                '-cil',
            ]]:
                continue

            cpe = CPE(part='a', product=name, version=version)
            if cpe not in self.host.facts['cpe']['application']:
                self.host.facts['cpe']['application'].append(cpe)
