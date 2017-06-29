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

import base64
import logging

from scap.Collector import Collector, ArgumentException

logger = logging.getLogger(__name__)
class FileContentsCollector(Collector):
    def __init__(self, host, args):
        super(FileContentsCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('FileContentsCollector requires path argument')

    def collect(self):
        cmd = 'base64 ' \
            + self.args['path'].replace('"', '\\"')
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        if len(out_lines) == 0 or return_code != 0:
            raise FileNotFoundError('Unable to collect contents of ' + self.args['path'])
        else:
            return base64.b64decode(''.join(out_lines))
