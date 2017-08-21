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

logger = logging.getLogger(__name__)
class VirtualMachineDetectionCollector(Collector):
    def collect(self):
        if 'in_virtual_machine' in self.host.facts:
            return

        from .ProcCpuidCollector import ProcCpuidCollector
        ProcCpuidCollector(self.host, {}).collect()

        self.host.facts['in_virtual_machine'] = False

        if (
            'processors' in self.host.facts['devices']
            and len(self.host.facts['devices']['processors']) > 0
            and 'hypervisor' in self.host.facts['devices']['processors'][0]['flags']
        ):
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'unknown'

        self._detect_virt()
        logger.debug('In VM: ' + str(self.host.facts['in_virtual_machine']))
        if 'hosting_hypervisor' in self.host.facts:
            logger.debug('Hosting Hypervisor: ' + self.host.facts['hosting_hypervisor'])

    def _detect_virt(self):
        # The following adapted from the virt-what script from Red Hat

        return_code, out_lines, err_lines = self.host.exec_command('if [ -f "/.dockerinit" ]; then echo docker; fi')
        if return_code == 0 and len(out_lines) >= 1 and out_lines[0].strip() == 'docker':
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'docker'
            return

        return_code, out_lines, err_lines = self.host.exec_command('if [ -f "/.dockerenv" ]; then echo docker; fi')
        if return_code == 0 and len(out_lines) >= 1 and out_lines[0].strip() == 'docker':
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'docker'
            return

        from .SysDmiCollector import SysDmiCollector
        SysDmiCollector(self.host, {}).collect()

        if 'sys_vendor' in self.host.facts['devices']['dmi']:
            sys_vendor = self.host.facts['devices']['dmi']['sys_vendor'].lower()
            if 'product_name' in self.host.facts['devices']['dmi']:
                product_name = self.host.facts['devices']['dmi']['product_name'].lower()
            else:
                product_name = ''

            if 'vmware' in sys_vendor:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'vmware'
                return
            elif 'xen' in sys_vendor:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'xen'
                if 'hvm' in product_name:
                    self.host.facts['hosting_hypervisor'] = 'xen-hvm'
                    return
                # else allow further detection techniques
            elif 'innotek' in sys_vendor or 'oracle' in sys_vendor:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'virtualbox'
                return
            elif 'qemu' in sys_vendor:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'qemu'
                return
            elif 'microsoft' in sys_vendor:
                if 'hv' in sys_vendor or 'hv' in product_name:
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'hyperv'
                    return
                else:
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'virtualpc'
                    return
            elif 'hitachi' in sys_vendor and 'lpar' in product_name:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'virtage'
                return
            elif 'parallels' in sys_vendor:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'parallels'
                return

        return_code, out_lines, err_lines = self.host.exec_command('if [ -d "/proc/vz" -a ! -d "/proc/bc" ]; then echo openvz; fi')
        if return_code == 0 and len(out_lines) >= 1 and out_lines[0].strip() == 'openvz':
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'openvz'
            return

        # TODO check if we have sudo
        # return_code, out_lines, err_lines = self.host.exec_command('if [ -e "/proc/1/environ" ] && cat "/proc/1/environ" | tr \'\\000\' \'\n\' | grep -Eiq \'^container=\'; then echo lxc; fi')
        # if return_code == 0 and len(out_lines) >= 1 and out_lines[0].strip() == 'lxc':
        #     self.host.facts['in_virtual_machine'] = True
        #     self.host.facts['hosting_hypervisor'] = 'lxc'
        #     return

        return_code, out_lines, err_lines = self.host.exec_command('cat /proc/self/status')
        if return_code == 0 and len(out_lines) >= 1:
            for line in out_lines:
                if re.match(r'VxID: 0$', line):
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'linux_vserver'
                    return
                elif re.match(r'VxID:\s+[0-9]*', line):
                    self.host.facts['in_virtual_machine'] = False
                    self.host.facts['running_hypervisor'] = 'linux_vserver'
                    return

        if 'UML' in self.host.facts['cpuinfo']:
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'uml'
            return

        if re.match(r'^vendor_id.*PowerVM Lx86', self.host.facts['cpuinfo']):
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'powervm_lx86'
            return

        if re.match(r'^vendor_id.*IBM/S390', self.host.facts['cpuinfo']):
            return_code, out_lines, err_lines = self.host.exec_command('cat /proc/sysinfo')
            if return_code == 0 and len(out_lines) >= 1:
                s = '\n'.join(out_lines)
                if re.match(r'VM.*Control Program.*z/VM', s):
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'ibm_systemz-zvm'
                    return
                elif re.match(r'^LPAR', s):
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'ibm_systemz-lpar'
                    return
                else:
                    # This is unlikely to be correct.
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'ibm_systemz-direct'
                    return
            else:
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'ibm_systemz'
                return

        if re.match(r'Xen', self.host.facts['cpuinfo']):
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'xen-hvm'
            return

        return_code, out_lines, err_lines = self.host.exec_command('if [ -d "/proc/xen" ]; then echo True; fi')
        if return_code == 0 and len(out_lines) >= 1 and out_lines[0].strip() == 'True':
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'xen'

            return_code, out_lines, err_lines = self.host.exec_command('cat /proc/xen/capabilities')
            if return_code == 0 and len(out_lines) >= 1:
                if 'control_d' in out_lines[0].strip():
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'xen-dom0'
                    return
                else:
                    self.host.facts['in_virtual_machine'] = True
                    self.host.facts['hosting_hypervisor'] = 'xen-domU'
                    return

        return_code, out_lines, err_lines = self.host.exec_command('cat /sys/hypervisor/type')
        if return_code == 0 and len(out_lines) >= 1:
            if 'xen' in out_lines[0].strip():
                self.host.facts['in_virtual_machine'] = True
                self.host.facts['hosting_hypervisor'] = 'xen'
                # TODO Ordinary kernel with pv_ops.  There does not seem to be
                # enough information at present to tell whether this is dom0
                # or domU.

        from ..UNameCollector import UNameCollector
        UNameCollector(self.host, {}).collect()
        return_code, out_lines, err_lines = self.host.exec_command('if [ -d "/sys/bus/xen" -a ! -d "/sys/bus/xen-backend" ]; then echo "xen-hvm"; fi')
        if (
            return_code == 0
            and len(out_lines) >= 1
            and self.host.facts['uname']['processor'] == 'ia64'
            and out_lines[0].strip() == 'xen-hvm'
        ):
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'xen-hvm'

        if 'KVM' in self.host.facts['cpuinfo']:
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'kvm'
            return

        if 'QEMU' in self.host.facts['cpuinfo']:
            self.host.facts['in_virtual_machine'] = True
            self.host.facts['hosting_hypervisor'] = 'qemu'
            return
