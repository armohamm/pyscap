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
import json
import pprint
import re

from scap.Collector import Collector
from ..exceptions import *

logger = logging.getLogger(__name__)
class EnvironmentCollector(Collector):
    def collect(self):
        cmd = 'Get-ChildItem Env:'
        cmd = cmd + " | Select-Object -Property * | ConvertTo-Json -Compress"
        return_code, out_lines, err_lines = self.host.exec_command('powershell -Command \"' + cmd + '\"')

        s = ''
        for l in out_lines:
            s = s + l
        j = json.loads(s)

        env = {}
        for e in j:
            env[e['Key']] = e['Value']

        return env
