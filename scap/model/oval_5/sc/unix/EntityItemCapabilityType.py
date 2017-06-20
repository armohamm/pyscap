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

from scap.model.oval_5.sc.EntityItemType import EntityItemType

logger = logging.getLogger(__name__)
class EntityItemCapabilityType(EntityItemType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enumeration(self):
        return [
            'CAP_CHOWN',
            'CAP_DAC_OVERRIDE',
            'CAP_DAC_READ_SEARCH',
            'CAP_FOWNER',
            'CAP_FSETID',
            'CAP_KILL',
            'CAP_SETGID',
            'CAP_SETUID',
            'CAP_SETPCAP',
            'CAP_LINUX_IMMUTABLE',
            'CAP_NET_BIND_SERVICE',
            'CAP_NET_BROADCAST',
            'CAP_NET_ADMIN',
            'CAP_NET_RAW',
            'CAP_IPC_LOCK',
            'CAP_IPC_OWNER',
            'CAP_SYS_MODULE',
            'CAP_SYS_RAWIO',
            'CAP_SYS_CHROOT',
            'CAP_SYS_PTRACE',
            'CAP_SYS_ADMIN',
            'CAP_SYS_BOOT',
            'CAP_SYS_NICE',
            'CAP_SYS_RESOURCE',
            'CAP_SYS_TIME',
            'CAP_SYS_TTY_CONFIG',
            'CAP_MKNOD',
            'CAP_LEASE',
            'CAP_AUDIT_WRITE',
            'CAP_AUDIT_CONTROL',
            'CAP_SETFCAP',
            'CAP_MAC_OVERRIDE',
            'CAP_MAC_ADMIN',
            'CAP_SYS_PACCT',
            'CAP_SYSLOG',
            'CAP_WAKE_ALARM',
            'CAP_BLOCK_SUSPEND',
            'CAP_AUDIT_READ',
            '',
        ]
