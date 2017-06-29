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
class DirectoryContentsCollector(Collector):
    def __init__(self, host, args):
        super(DirectoryContentsCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('DirectoryContentsCollector requires path argument')

    TYPE_MAP = {
        '-': 'regular file',
        'b': 'block special file',
        'c': 'character special file',
        'C': 'high performance (contiguous data) file',
        'd': 'directory',
        'D': 'door', # Solaris 2.5 and up
        'l': 'symbolic link',
        'M': 'off-line (migrate) file', # Cray DMF
        'n': 'network special file', # HP-UX
        'p': 'FIFO (named pipe)',
        'P': 'port', # Solaris 10 and up
        's': 'socket',
        '?': 'some other file type',
    }

    def collect(self):
        path = self.args['path'].replace('"', '\\"')
        if 'hidden' in self.args and self.args['hidden']:
            cmd = 'ls --color=never -l1A "' + path + '"'
        else:
            cmd = 'ls --color=never -l1 "' + path + '"'
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        entries = []
        for l in out_lines:
            if l.startswith('total'):
                continue

            m = re.fullmatch(r'([-a-z])([-sStTrwx]{3})([-sStTrwx]{3})([-rwx]{3})(\.)?\s+([0-9]+)\s+(\S+)\s+(\S+)\s+([0-9]+)\s+(\S+\s+\S+\s+\S+)\s+(.*)( -> (.*))?', l)
            if m:
                entry = {
                    'type': DirectoryContentsCollector.TYPE_MAP[m.group(1)],
                    'user_mode': m.group(2),
                    'group_mode': m.group(3),
                    'other_mode': m.group(4),
                    'link_count': m.group(6),
                    'owner': m.group(7),
                    'group_owner': m.group(8),
                    'size': int(m.group(9)),
                    'modified': m.group(10),
                    'name': m.group(11),
                }
                if m.group(5) is not None:
                    entry['has_security_context'] = True
                if m.group(12) is not None:
                    entry['link_target'] = m.group(12)

                entries.append(entry)
            else:
                raise ValueError('Unable to parse line from ls: ' + l)
        return entries
