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
class UNameCollector(Collector):
    def collect(self):
        if 'uname' in self.host.facts:
            return

        return_code, out_lines, err_lines = self.host.exec_command('uname -a')
        self.host.facts['uname'] = out_lines[0]

        if self.host.facts['uname'].startswith('Linux'):
            cpe = CPE()
            cpe.set_value('part', 'o')
            cpe.set_value('vendor', 'linux')
            cpe.set_value('product', 'linux_kernel')

            m = re.match(r'^Linux \S+ ([0-9.]+)-(\S+)', self.host.facts['uname'])
            if m:
                cpe.set_value('version', m.group(1))
                cpe.set_value('update', m.group(2))

            if 'cpe' not in self.host.facts:
                self.host.facts['cpe'] = {'os':[], 'application':[], 'hardware':[]}

            if cpe not in self.host.facts['cpe']['os']:
                self.host.facts['cpe']['os'].append(cpe)
