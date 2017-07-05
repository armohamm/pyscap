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

import getpass
import logging
import subprocess

from scap.host.cli.LocalHost import LocalHost
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class WindowsLocalHost(LocalHost):
    def __init__(self, hostname):
        super(WindowsLocalHost, self).__init__(hostname)

        # so we short circuit any detection
        self.facts['oval_family'] = 'windows'

        # TODO check if powershell is available & at least 4.0

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def exec_command(self, cmd, encoding='cp437'):
        inventory = Inventory()

        logger.debug("Sending command: " + cmd)
        p = subprocess.run(cmd,
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
            shell=True)

        #logger.debug('Got stdout: ' + str(p.stdout))
        #logger.debug('Got stderr: ' + str(p.stderr))

        out_lines = str.splitlines(p.stdout.replace(b'\r\r', b'\r').decode(encoding))
        out_lines = [line.strip('\x0A\x0D') for line in out_lines]
        err_lines = str.splitlines(p.stderr.replace(b'\r\r', b'\r').decode(encoding))
        err_lines = [line.strip('\x0A\x0D') for line in err_lines]

        #logger.debug('stdout lines: ' + str(out_lines))
        #logger.debug('stderr lines: ' + str(err_lines))

        return (p.returncode, out_lines, err_lines)
