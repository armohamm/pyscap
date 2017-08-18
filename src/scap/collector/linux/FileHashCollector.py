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
    HASH_COMMANDS = {
        'MD5': 'md5sum',
        'SHA-1': 'sha1sum',
        'SHA-224': 'sha224sum',
        'SHA-256': 'sha256sum',
        'SHA-384': 'sha384sum',
        'SHA-512': 'sha512sum',
    }

    def __init__(self, host, args):
        super(FileHashCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('FileHashCollector requires path argument')

        if 'type' not in args:
            raise ArgumentException('FileHashCollector requires type argument')

        if args['type'] not in FileHashCollector.HASH_COMMANDS.keys():
            raise ArgumentException('Unknown hash type: ' + args['type'])

    def collect(self):
        cmd = FileHashCollector.HASH_COMMANDS[self.args['type']] \
            + ' ' + self.args['path'].replace('"', '\\"') + ' | cut -f1 -d" "'
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        if len(out_lines) == 0 or return_code != 0:
            raise FileNotFoundError('Unable to collect hash for ' + self.args['path'])
        else:
            return out_lines[0]
