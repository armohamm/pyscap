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
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)

class ElevationException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class CLIHost(Host):
    def __init__(self, hostname):
        super(CLIHost, self).__init__(hostname)

        inventory = Inventory()

        if inventory.has_option(self.hostname, 'sudo_password'):
            self.sudo_password = inventory.get(self.hostname, 'sudo_password')
        else:
            self.sudo_password = None

        if inventory.has_option(self.hostname, 'enable_password'):
            self.sudo_password = inventory.get(self.hostname, 'enable_password')
        else:
            self.sudo_password = None

    def can_sudo(self):
        return self.sudo_password is not None

    def can_enable(self):
        return self.sudo_password is not None

    def exec_command(self, cmd):
        ''' should return (status, out_lines, err_lines) '''
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
