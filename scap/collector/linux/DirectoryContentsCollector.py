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

import datetime
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
            cmd = 'ls -1A --color=never --full-time "' + path + '"'
        else:
            cmd = 'ls -1 --color=never --full-time "' + path + '"'
        return_code, out_lines, err_lines = self.host.exec_command(cmd)
        if return_code != 0:
            raise FileNotFoundError('Unable to collect the contents of ' + self.args['path'])

        entries = []
        for l in out_lines:
            if re.fullmatch(r'\w+\s+[0-9]+', l):   # total line
                continue

            #2011-11-08 18:02:08.954092000 -0700
            m = re.fullmatch(r'([-a-z])([-sStTrwx]{3})([-sStTrwx]{3})([-rwx]{3})(\.)?\s+([0-9]+)\s+(\S+)\s+(\S+)\s+([0-9]+)\s+([0-9]+-[0-9]+-[0-9]+\s+[0-9]+:[0-9]+:[0-9.]+\s+[0-9-]+)\s+(.*)( -> (.*))?', l)
            if m:
                mtime = m.group(10)
                logger.debug('original mtime: ' + str(mtime))

                # an unfortunate circumstance of the mtime %f not always being 6 or less chars
                mtime = m.group(10).partition('.')
                msecs = mtime[2]
                mtime = mtime[0] + '.'
                msecs = msecs.partition(' ')
                mtime = mtime + msecs[0][:5] + ' ' + msecs[2]
                logger.debug('reduced precision mtime: ' + str(mtime))

                mtime = datetime.datetime.strptime(mtime, '%Y-%m-%d %H:%M:%S.%f %z')
                logger.debug('parsed mtime: ' + str(mtime))

                entry = {
                    'type': DirectoryContentsCollector.TYPE_MAP[m.group(1)],
                    'user_mode': m.group(2),
                    'group_mode': m.group(3),
                    'other_mode': m.group(4),
                    'link_count': m.group(6),
                    'owner': m.group(7),
                    'group_owner': m.group(8),
                    'size': int(m.group(9)),
                    'modified_raw': m.group(10),
                    'modified': mtime,
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
