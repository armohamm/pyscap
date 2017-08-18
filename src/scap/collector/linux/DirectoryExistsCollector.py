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
class DirectoryExistsCollector(Collector):
    def __init__(self, host, args):
        super(DirectoryExistsCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('DirectoryExistsCollector requires path argument')

    def collect(self):
        path = self.args['path'].replace('"', '\\"')
        if 'case_insensitive' in self.args and self.args['case_insensitive']:
            cmd = 'find `dirname "' + path + '"` -type d -iwholename "' + path + '"'
        else:
            cmd = 'find `dirname "' + path + '"` -type d -wholename "' + path + '"'
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        if len(out_lines) > 0:
            return True
        else:
            return False
