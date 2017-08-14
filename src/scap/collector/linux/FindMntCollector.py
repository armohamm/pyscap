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

from scap.Collector import Collector

logger = logging.getLogger(__name__)
class FindMntCollector(Collector):
    def collect(self):
        if 'findmnt' in self.host.facts:
            return

        return_code, out_lines, err_lines = self.host.exec_command("findmnt -P")
        if return_code != 0 or len(out_lines) <= 0:
            raise RuntimeError('Unable to collect mount points')

        self.host.facts['findmnt'] = ''.join(out_lines)
        self.host.facts['mountpoints'] = {}

        for line in out_lines:
            values = {}
            for value in line.split(' '):
                name, sep, val = value[:-1].partition('="')
                values[name.lower()] = val
            self.host.facts['mountpoints'][values['target']] = values
            logger.debug('Discovered mountpoint: ' + str(values))
