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

from scap.Collector import Collector
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class CpeCollector(Collector):
    def collect(self):
        self.host.facts['cpe'] = {'os':[], 'application':[], 'hardware':[]}

        # hardware
        from scap.collector.linux.LshwCollector import LshwCollector
        LshwCollector(self.host, {}).collect()

        from scap.collector.linux.LspciCollector import LspciCollector
        LspciCollector(self.host, {}).collect()

        from scap.collector.linux.LscpuCollector import LscpuCollector
        LscpuCollector(self.host, {}).collect()

        # TODO hwinfo
        # TODO lsusb
        # TODO lsscsi
        # TODO hdparm

        # os
        from scap.collector.linux.LsbReleaseCollector import LsbReleaseCollector
        LsbReleaseCollector(self.host, {}).collect()

        from scap.collector.UNameCollector import UNameCollector
        UNameCollector(self.host, {}).collect()

        # application
        for cpe in self.host.facts['cpe']['os']:
            if CPE(part='o', vendor='ubuntu').matches(cpe) \
            or CPE(part='o', vendor='debian').matches(cpe) \
            or CPE(part='o', vendor='linuxmint').matches(cpe):
                from scap.collector.linux.DpkgCollector import DpkgCollector
                DpkgCollector(self.host, {}).collect()

            # TODO Red Hat, CentOS: yum, rpm
            # TODO Fedora: dnf
            # TODO OpenSUSE: zypper
            # TODO Arch: pacman

        for cpe_part in self.host.facts['cpe']:
            for cpe in self.host.facts['cpe'][cpe_part]:
                logger.debug(cpe.to_uri_string())
