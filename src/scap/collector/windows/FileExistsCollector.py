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
from ..exceptions import *

logger = logging.getLogger(__name__)
class FileExistsCollector(Collector):
    def __init__(self, host, args):
        super(FileExistsCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('FileExistsCollector requires path argument')

    def collect(self):
        path = self.args['path'].replace("'", "\\'")
        # NOTE: windows fs are always case insensitive
        cmd = "Test-Path '" + path + "' -PathType Leaf"
        return_code, out_lines, err_lines = self.host.exec_command('powershell -Command \"' + cmd + '\"')
        if len(out_lines) > 0 and out_lines[0] == 'True':
            return True
        else:
            return False
