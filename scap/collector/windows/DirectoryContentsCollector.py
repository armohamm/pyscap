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
import json
import logging

from scap.Collector import Collector, ArgumentException
from scap.collector.windows import convert_json_timestamp

logger = logging.getLogger(__name__)
class DirectoryContentsCollector(Collector):
    def __init__(self, host, args):
        super(DirectoryContentsCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('DirectoryContentsCollector requires path argument')

    def collect(self):
        path = self.args['path'].replace("'", "\\'")
        if 'hidden' in self.args and self.args['hidden']:
            cmd = "Get-ChildItem -LiteralPath '" + path + "' -Force"
        else:
            cmd = "Get-ChildItem -LiteralPath '" + path + "'"
        cmd = cmd + " | Select-Object -Property * | ConvertTo-Json -Compress"
        logger.debug('cmd: ' + cmd)
        return_code, out_lines, err_lines = self.host.exec_command('powershell -Command \"' + cmd + '\"')
        if return_code != 0:
            raise FileNotFoundError('Unable to collect the contents of ' + self.args['path'] + ': ' + str(return_code))

        s = ''
        for l in out_lines:
            s = s + l
        entries = json.loads(s)

        for e in entries:
            e['name'] = e['Name']
            #logger.debug(e['name'] + ': ' + str(e['LastWriteTimeUtc']))
            mtime = convert_json_timestamp(int(e['LastWriteTimeUtc'].replace('/Date(', '').replace(')/', '')))
            e['modified'] = mtime
            #logger.debug(e['name'] + ': ' + str(e['modified']))

            if e['Mode'].startswith('d'):
                e['type'] = 'directory'
            else:
                e['type'] = 'regular file'
                e['size'] = e['Length']

        return entries
