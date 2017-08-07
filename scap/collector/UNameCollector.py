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

        self.host.facts['uname'] = {}

        for option, key in {
            '-a': 'all',
            '-s': 'kernel_name',
            '-n': 'nodename',
            '-r': 'kernel_release',
            '-v': 'kernel_version',
            '-m': 'machine',
            '-p': 'processor',
            '-i': 'hardware_platform',
            '-o': 'operating_system',
            '--version': 'version',
        }.items():
            return_code, out_lines, err_lines = self.host.exec_command('uname ' + option)
            if return_code == 0 and len(out_lines) > 0:
                self.host.facts['uname'][key] = out_lines[0].strip()

        if len(self.host.facts['uname']) == 0:
            raise RuntimeError('Uname information is unavailable')

        logger.debug('uname: ' + str(self.host.facts['uname']))
