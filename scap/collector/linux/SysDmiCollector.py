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
class SysDmiCollector(Collector):
    def collect(self):
        if 'devices' not in self.host.facts:
            self.host.facts['devices'] = {}

        if 'dmi' in self.host.facts['devices']:
            return

        self.host.facts['devices']['dmi'] = {}

        return_code, out_lines, err_lines = self.host.exec_command('ls -1 --color=never /sys/devices/virtual/dmi/id')
        if return_code == 0 and len(out_lines) > 0:
            logger.debug('/sys/devices/virtual/dmi/id contains: ' +' '.join(out_lines))
            dmi_ids = out_lines
            for dmi_id in dmi_ids:
                if dmi_id in ('subsystem', 'power'):
                    continue
                return_code, out_lines, err_lines = self.host.exec_command('cat /sys/devices/virtual/dmi/id/' + dmi_id)
                if return_code == 0 and len(out_lines) > 0:
                    self.host.facts['devices']['dmi'][dmi_id] = out_lines[0].strip()
                    logger.debug(dmi_id + ' = ' + self.host.facts['devices']['dmi'][dmi_id])

        return_code, out_lines, err_lines = self.host.exec_command('ls -1 --color=never /sys/devices/virtual/dmi/id/power')
        if return_code == 0 and len(out_lines) > 0:
            logger.debug('/sys/devices/virtual/dmi/id/power contains: ' +' '.join(out_lines))
            power_items = out_lines
            for p in power_items:
                return_code, out_lines, err_lines = self.host.exec_command('cat /sys/devices/virtual/dmi/id/power/' + p)
                if return_code == 0 and len(out_lines) > 0:
                    self.host.facts['devices']['dmi']['power_' + p] = out_lines[0].strip()
                    logger.debug('power_' + p + ' = ' + self.host.facts['devices']['dmi']['power_' + p])
