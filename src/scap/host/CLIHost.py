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

from scap.Host import Host
from .exceptions import *
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CLIHost(Host):
    def __init__(self, hostname):
        super(CLIHost, self).__init__(hostname)

        inventory = Inventory()

        if inventory.has_option(self.hostname, 'sudo_password'):
            self.sudo_password = inventory.get(self.hostname, 'sudo_password')
        else:
            self.sudo_password = None

        if inventory.has_option(self.hostname, 'enable_password'):
            self.enable_password = inventory.get(self.hostname, 'enable_password')
        else:
            self.enable_password = None

        self._cmd_out_buf = ''
        self._cmd_err_buf = ''

    def can_sudo(self):
        return self.sudo_password is not None

    def can_enable(self):
        return self.enable_password is not None

    def _recv_stdout(self, session, data):
        logger.debug('Stdout received: ' + str(data))
        self._cmd_out_buf += data

    def _recv_stderr(self, session, data):
        logger.debug('Stderr received: ' + str(data))
        self._cmd_err_buf += data
        if self._cmd_err_buf.startswith('[sudo]') or self._cmd_err_buf.startswith('Password:'):
            if self.can_sudo:
                logger.debug("Sending sudo_password...")
                self._send_stdin(session, self.sudo_password + "\n")
                self._cmd_err_buf = ''
            else:
                raise SudoException("Cannot sudo without sudo_password defined in inventory.ini file")

    def _send_stdin(self, session, data):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def exec_command(self, cmd):
        ''' should return (status, out_lines, err_lines) '''
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
