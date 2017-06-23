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

import inspect
import importlib
import logging
import sys

from scap.Inventory import Inventory
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class Host(object):
    @staticmethod
    def load(hostname):
        inventory = Inventory()

        # TODO better connection detection
        if not inventory.has_section(hostname) or not inventory.has_option(hostname, 'connection'):
            if hostname == 'localhost':
                connection_type = 'local'
            else:
                connection_type = 'ssh'
        else:
            connection_type = inventory.get(hostname, 'connection')

        # TODO impacket
        # TODO SMB?
        # TODO PSExec?
        if connection_type == 'ssh':
            from scap.host.cli.SSHHost import SSHHost
            return SSHHost(hostname)
        elif connection_type == 'winrm':
            if not inventory.has_option(hostname, 'winrm_auth_method'):
                raise RuntimeError('Host ' + hostname + ' has not specified option: winrm_auth_method')
            auth_method = inventory.get(hostname, 'winrm_auth_method')
            logger.debug('Using winrm_auth_method ' + auth_method)
            if auth_method == 'ssl':
                from scap.host.cli.winrm.WinRMHostSSL import WinRMHostSSL
                return WinRMHostSSL(hostname)
            elif auth_method == 'ntlm':
                from scap.host.cli.winrm.WinRMHostNTLM import WinRMHostNTLM
                return WinRMHostNTLM(hostname)
            elif auth_method == 'kerberos':
                from scap.host.cli.winrm.WinRMHostKerberos import WinRMHostKerberos
                return WinRMHostKerberos(hostname)
            elif auth_method == 'plaintext':
                from scap.host.cli.winrm.WinRMHostPlaintext import WinRMHostPlaintext
                return WinRMHostPlaintext(hostname)
            else:
                raise RuntimeError('Host ' + hostname + ' specified an invalid winrm_auth_method option')
        elif connection_type == 'local':
            if sys.platform.startswith('linux'):
                from scap.host.cli.local.LinuxLocalHost import LinuxLocalHost
                return LinuxLocalHost(hostname)
            elif sys.platform == 'win32':
                from scap.host.cli.local.WindowsLocalHost import WindowsLocalHost
                return WindowsLocalHost(hostname)
            else:
                raise NotImplementedError('Local connection on ' + sys.platform + ' is not yet supported')
        else:
            raise RuntimeError('Unsupported host connection type: ' + connection_type)

    def __init__(self, hostname):
        self.hostname = hostname
        self.collectors = []
        self.facts = {}
        self.results = {}

    def connect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def disconnect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def detect_collectors(self, args):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def evaluate_oval_object(self, obj, content, imports, export_names):
        if 'oval_family' not in self.facts:
            if 'cpe' not in self.facts or 'os' not in self.facts['cpe'] or len(self.facts['cpe']['os']) <= 0:
                raise ValueError('Need a defined OS CPE to determine family')

            for cpe in self.facts['cpe']['os']:
                logger.debug('Checking ' + str(cpe) + ' for family match')
                if CPE(part='o', vendor='linux').matches(cpe):
                    self.facts['oval_family'] = 'linux'
                elif CPE(part='o', vendor='microsoft').matches(cpe):
                    self.facts['oval_family'] = 'windows'

            if 'oval_family' not in self.facts:
                raise ValueError('Unable to determine family from discovered CPEs')

        collector_module = obj.__module__.replace('ObjectElement', 'Collector').replace('scap.model.oval_5.defs.', 'scap.collector.' + self.facts['oval_family'] + '.oval_5.')
        collector_class = obj.__class__.__name__.replace('ObjectElement', 'Collector')
        mod = importlib.import_module(collector_module, collector_class)
        class_ = getattr(mod, collector_class)
        collector = class_(self, {'object': obj, 'content': content, 'imports': imports, 'export_names': export_names})
        return collector.collect()
