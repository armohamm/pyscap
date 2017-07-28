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

from scap.Collector import Collector

logger = logging.getLogger(__name__)
class UniqueIdCollector(Collector):
    def collect(self):
        try:
            return_code, out_lines, err_lines = self.host.exec_command('cat /sys/class/dmi/id/product_uuid')
            if return_code != 0 or len(out_lines) < 1:
                raise RuntimeError('Could not cat /sys/class/dmi/id/product_uuid')

            logger.debug('From /sys/class/dmi/id/product_uuid: ' + out_lines[0])
            u = None
            u = uuid.UUID(out_lines[0].strip())

            if u is None:
                raise RuntimeError('Could not parse dmidecode output: ' + str(out_lines))

            u = uuid.UUID(u)
            self.host.facts['unique_id'] = u.hex
            self.host.facts['motherboard_uuid'] = self.host.facts['unique_id']
        except:
            try:
                from scap.collector.linux.DmiDecodeCollector import DmiDecodeCollector
                DmiDecodeCollector(self.host, {}).collect()
            except:
                # fall back to root fs uuid
                from scap.collector.linux.RootFsUuidCollector import RootFsUuidCollector
                RootFsUuidCollector(self.host, {}).collect()
                self.host.facts['unique_id'] = self.host.facts['root_uuid']
        logger.debug('System UUID: ' + self.host.facts['unique_id'])
