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
class BlkidCollector(Collector):
    def collect(self):
        if 'blkid' in self.host.facts:
            return

        self.host.facts['blkid'] = {}
        return_code, out_lines, err_lines = self.host.exec_command("blkid")
        if return_code != 0 or len(out_lines) <= 0:
            raise RuntimeError('Unable to collect filesystem blkids')

        for line in out_lines:
            dev, sep, values = line.partition(':')
            self.host.facts['blkid'][dev] = {}
            for value in values.split(' '):
                name, sep, val = value[:-1].partition('="')
                self.host.facts['blkid'][dev][name.lower()] = val
                logger.debug(dev + ' blkid field ' + name.lower() + ' = ' + val)
