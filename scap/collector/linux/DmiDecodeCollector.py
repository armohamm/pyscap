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

# Based on https://github.com/MyNameIsMeerkat/GetSysUUID/blob/master/GetSysUUID.py

import logging
import uuid

from scap.Collector import Collector

logger = logging.getLogger(__name__)
class DmiDecodeCollector(Collector):
    def collect(self):
        if 'dmidecode' in self.host.facts:
            return

        self.host.facts['dmidecode'] = {}

        return_code, out_lines, err_lines = self.host.exec_command('sudo -S dmidecode -s system-uuid')
        if return_code != 0 or len(out_lines) < 1:
            raise RuntimeError('Could not run sudo -S dmidecode -s system-uuid')

        self.host.facts['dmidecode']['system_uuid'] = out_lines[0]
