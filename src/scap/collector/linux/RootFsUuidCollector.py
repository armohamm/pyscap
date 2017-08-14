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

logger = logging.getLogger(__name__)
class RootFsUuidCollector(Collector):
    def collect(self):
        # return_code, out_lines, err_lines = self.host.exec_command("blkid -o value -s UUID `mount -l | grep 'on / ' | awk '{print $1}'`")
        # if return_code != 0 or len(out_lines) <= 0:
        #     raise RuntimeError('Unable to determine unique id from root fs uuid')
        #
        # self.host.facts['root_filesystem_uuid'] = out_lines[0].strip()
        from .BlkidCollector import BlkidCollector
        BlkidCollector(self.host, {}).collect()
        from .FindMntCollector import FindMntCollector
        FindMntCollector(self.host, {}).collect()
        try:
            mountpoint = self.host.facts['mountpoints']['/']['source']
            self.host.facts['root_filesystem_uuid'] = self.host.facts['blkid'][mountpoint]['uuid']
        except KeyError:
            raise RuntimeError('Unable to determine unique id from root fs uuid')

        logger.debug('Root FS UUID: ' + self.host.facts['root_filesystem_uuid'])
