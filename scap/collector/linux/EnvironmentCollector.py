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

from scap.Collector import Collector, ArgumentException

logger = logging.getLogger(__name__)
class EnvironmentCollector(Collector):
    def collect(self):
        cmd = 'export'
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        env = {}
        for l in out_lines:
            m = re.fullmatch(r'declare -x (\S+)=[\'"](.*)[\'"]', l)
            if m:
                env[m.group(1)] = m.group(2)
                continue
            m = re.fullmatch(r'export (\S+)=[\'"](.*)[\'"]', l)
            if m:
                env[m.group(1)] = m.group(2)
                continue
                raise ValueError('Unable to parse export line: ' + l)
        return env
