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

        from ..UNameCollector import UNameCollector
        UNameCollector(self.host, {}).collect()
        if self.host.facts['uname']['kernel_name'] == 'Linux':
            cpe = CPE()
            cpe.set_value('part', 'o')
            cpe.set_value('vendor', 'linux')
            cpe.set_value('product', 'linux_kernel')

            m = re.fullmatch(r'([0-9.]+)-(\S+)', self.host.facts['uname']['kernel_release'])
            if m:
                cpe.set_value('version', m.group(1))
                cpe.set_value('update', m.group(2))

            if cpe not in self.host.facts['cpe']['os']:
                self.host.facts['cpe']['os'].append(cpe)
        elif self.host.facts['uname']['kernel_name'] == 'Windows NT':
            cpe = CPE()
            cpe.set_value('part', 'o')
            cpe.set_value('vendor', 'microsoft')
            cpe.set_value('product', 'windows')
            cpe.set_value('version', 'nt')

            if cpe not in self.host.facts['cpe']['os']:
                self.host.facts['cpe']['os'].append(cpe)

        # try:
        from .SysDmiCollector import SysDmiCollector
        SysDmiCollector(self.host, {}).collect()

        try:
            cpe = CPE(
                part='h',
                vendor=self.host.facts['devices']['dmi']['bios_vendor'],
                product='BIOS',
                version=self.host.facts['devices']['dmi']['bios_version'],
            )
            if cpe not in self.host.facts['cpe']['hardware']:
                self.host.facts['cpe']['hardware'].append(cpe)
        except KeyError:
            pass

        try:
            cpe = CPE(
                part='h',
                vendor=self.host.facts['devices']['dmi']['board_vendor'],
                product=self.host.facts['devices']['dmi']['board_name'],
                version=self.host.facts['devices']['dmi']['board_version'],
            )
            if cpe not in self.host.facts['cpe']['hardware']:
                self.host.facts['cpe']['hardware'].append(cpe)
        except KeyError:
            pass

        try:
            cpe = CPE(
                part='h',
                vendor=self.host.facts['devices']['dmi']['chassis_vendor'],
                product=self.host.facts['devices']['dmi']['chassis_type'],
                version=self.host.facts['devices']['dmi']['chassis_version'],
            )
            if cpe not in self.host.facts['cpe']['hardware']:
                self.host.facts['cpe']['hardware'].append(cpe)
        except KeyError:
            pass

        try:
            cpe = CPE(
                part='h',
                vendor=self.host.facts['devices']['dmi']['sys_vendor'],
                product=self.host.facts['devices']['dmi']['product_name'],
                version=self.host.facts['devices']['dmi']['product_version'],
            )
            if cpe not in self.host.facts['cpe']['hardware']:
                self.host.facts['cpe']['hardware'].append(cpe)
        except KeyError:
            pass

        from .ProcCpuidCollector import ProcCpuidCollector
        ProcCpuidCollector(self.host, {}).collect()

        for cpu in self.host.facts['devices']['processors']:
            try:
                cpe = CPE(
                    part='h',
                    vendor=cpu['vendor_id'],
                    product=cpu['model name'],
                    version=cpu['stepping'],
                )
                if cpe not in self.host.facts['cpe']['hardware']:
                    self.host.facts['cpe']['hardware'].append(cpe)
            except KeyError:
                pass

        # except:
            # from scap.collector.linux.LshwCollector import LshwCollector
            # LshwCollector(self.host, {}).collect()
            #
            # from scap.collector.linux.LspciCollector import LspciCollector
            # LspciCollector(self.host, {}).collect()
            #
            # from scap.collector.linux.LscpuCollector import LscpuCollector
            # LscpuCollector(self.host, {}).collect()
            # pass

        # os
        from scap.collector.linux.LsbReleaseCollector import LsbReleaseCollector
        LsbReleaseCollector(self.host, {}).collect()

        from scap.collector.UNameCollector import UNameCollector
        UNameCollector(self.host, {}).collect()

        # application
        for cpe in self.host.facts['cpe']['os']:
            if (
                CPE(part='o', vendor='ubuntu').matches(cpe)
                or CPE(part='o', vendor='debian').matches(cpe)
                or CPE(part='o', vendor='linuxmint').matches(cpe)
            ):
                from scap.collector.linux.DpkgCollector import DpkgCollector
                DpkgCollector(self.host, {}).collect()

            # TODO Red Hat, CentOS: yum, rpm
            # TODO Fedora: dnf
            # TODO OpenSUSE: zypper
            # TODO Arch: pacman

        for cpe_part in self.host.facts['cpe']:
            for cpe in self.host.facts['cpe'][cpe_part]:
                logger.debug(cpe.to_uri_string())
