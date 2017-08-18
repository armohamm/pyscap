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

# Based on https://github.com/MyNameIsMeerkat/GetSysUUID/blob/master/GetSysUUID.py

import logging
import re

from scap.Collector import Collector
from scap.host.exceptions import *

logger = logging.getLogger(__name__)
class UniqueIdCollector(Collector):
    def collect(self):
        from .VirtualMachineDetectionCollector import VirtualMachineDetectionCollector
        VirtualMachineDetectionCollector(self.host, {}).collect()

        if self.host.facts['in_virtual_machine'] and self.host.facts['hosting_hypervisor'] == 'docker':
            return_code, out_lines, err_lines = self.host.exec_command('cat /proc/self/cgroup')
            if return_code != 0 or len(out_lines) <= 0:
                raise RuntimeError('Unable to collect unique id from docker: return_code=' + str(return_code) + ' out_lines=' + str(out_lines))

            logger.debug('/proc/self/cgroup: ' + str(out_lines))
            for line in out_lines:
                m = re.fullmatch(r'.*docker[/.-]([a-fA-F0-9]+).*', line)
                if m:
                    self.host.facts['unique_id'] = m.group(1)
                    logger.debug('Found docker id: ' + self.host.facts['unique_id'])
                    break

            # raise if we didn't find it
            if 'unique_id' not in self.host.facts or self.host.facts['unique_id'] is None:
                raise RuntimeError('Unable to parse unique id from docker')
            return

        # TODO other container types
        # TODO virtual  machines not covered by the below

        # Try dmidecode; both unique id & mobo uuid
        try:
            from .DmiDecodeCollector import DmiDecodeCollector
            DmiDecodeCollector(self.host, {}).collect()

            if 'system-uuid' not in self.host.facts['dmidecode']:
                raise RuntimeError('Unable to determine unique id from DmiDecodeCollector')

            self.host.facts['unique_id'] = self.host.facts['dmidecode']['system-uuid']
            self.host.facts['motherboard_uuid'] = self.host.facts['dmidecode']['system-uuid']
            logger.debug('System unique id: ' + self.host.facts['unique_id'])
            return
        except (RuntimeError, SudoException):
            pass

        # try /sys/devices/virtual/dmi/id; both unique id & mobo uuid
        try:
            from .SysDmiCollector import SysDmiCollector
            SysDmiCollector(self.host, {}).collect()

            if 'product_uuid' not in self.host.facts['devices']['dmi']:
                raise RuntimeError('Unable to determine unique id from SysDmiCollector')

            logger.debug('From SysDmiCollector: ' + self.host.facts['devices']['dmi']['product_uuid'])

            self.host.facts['unique_id'] = self.host.facts['devices']['dmi']['product_uuid']
            self.host.facts['motherboard_uuid'] = self.host.facts['devices']['dmi']['product_uuid']
            logger.debug('System unique id: ' + self.host.facts['unique_id'])
            return
        except (RuntimeError, SudoException):
            pass

        # try the dbus machine id; should be stable
        try:
            from .DBusMachineIdCollector import DBusMachineIdCollector
            DBusMachineIdCollector(self.host, {}).collect()

            self.host.facts['unique_id'] = self.host.facts['dbus_machine_id']
            logger.debug('System unique id: ' + self.host.facts['unique_id'])
            return
        except RuntimeError:
            pass

        # try the root fs uuid; should be somewhat stable
        try:
            from .RootFsUuidCollector import RootFsUuidCollector
            RootFsUuidCollector(self.host, {}).collect()

            self.host.facts['unique_id'] = self.host.facts['root_filesystem_uuid']
            logger.debug('System unique id: ' + self.host.facts['unique_id'])
            return
        except RuntimeError:
            pass

        # this is a crappy unique id to use since it changes on the next boot, but better than nothing
        return_code, out_lines, err_lines = self.host.exec_command('cat /proc/sys/kernel/random/boot_id')
        if return_code != 0 or len(out_lines) <= 0:
            raise RuntimeError('Unable to determine unique id from /proc/sys/kernel/random/boot_id')

        self.host.facts['unique_id'] = out_lines[0]
        logger.debug('System unique id: ' + self.host.facts['unique_id'])
