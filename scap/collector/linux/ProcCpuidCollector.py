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
import pprint

from scap.Collector import Collector
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class ProcCpuidCollector(Collector):
    def collect(self):
        if 'devices' not in self.host.facts:
            self.host.facts['devices'] = {}

        if 'processors' in self.host.facts['devices']:
            return

        self.host.facts['devices']['processors'] = []

        return_code, out_lines, err_lines = self.host.exec_command('cat /proc/cpuinfo')
        if return_code == 0 and len(out_lines) >= 1:
            self.host.facts['cpuinfo'] = '\n'.join(out_lines)
            cur_proc = {}
            for line in out_lines:
                line = line.strip()
                if line == '':
                    self.host.facts['devices']['processors'].append(cur_proc)
                    cur_proc = {}
                    continue

                k, eq, v = line.partition(':')
                k = k.strip()
                v = v.strip()
                cur_proc[k] = v
                logger.debug(k + ' = ' + v)
