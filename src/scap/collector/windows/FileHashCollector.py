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
class FileHashCollector(Collector):
    HASH_ALGORITHMS = {
        'MD5': 'MD5',
        'SHA-1': 'SHA1',
        #'SHA-224': 'sha224sum',
        'SHA-256': 'SHA256',
        'SHA-384': 'SHA384',
        'SHA-512': 'SHA512',
    }

    def __init__(self, host, args):
        super(FileHashCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('FileHashCollector requires path argument')

        if 'type' not in args:
            raise ArgumentException('FileHashCollector requires type argument')

        if args['type'] not in FileHashCollector.HASH_ALGORITHMS.keys():
            raise ArgumentException('Unknown hash type: ' + args['type'])

    def collect(self):
        path = self.args['path'].replace("'", "\\'")
        cmd = "Get-FileHash -LiteralPath '" + path + "' -Algorithm " + FileHashCollector.HASH_ALGORITHMS[self.args['type']]
        cmd = cmd + ' | % { $_.Hash }'
        return_code, out_lines, err_lines = self.host.exec_command('powershell -Command \"' + cmd + '\"')
        if len(out_lines) == 0 or return_code != 0:
            raise FileNotFoundError('Unable to collect hash for ' + self.args['path'])

        return out_lines[0]
