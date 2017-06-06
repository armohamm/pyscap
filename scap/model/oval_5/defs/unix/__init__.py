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
TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}dnscache_test': 'DnsCacheTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}dnscache_object': 'DnsCacheObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}dnscache_state': 'DnsCacheStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}file_test': 'FileTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}file_object': 'FileObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}file_state': 'FileStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}fileextendedattribute_test': 'FileExtendedAttributeTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}fileextendedattribute_object': 'FileExtendedAttributeObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}fileextendedattribute_state': 'FileExtendedAttributeStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}gconf_test': 'GconfTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}gconf_object': 'GconfObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}gconf_state': 'GconfStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}inetd_test': 'InetdTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}inetd_object': 'InetdObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}inetd_state': 'InetdStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}interface_test': 'InterfaceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}interface_object': 'InterfaceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}interface_state': 'InterfaceStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}password_test': 'PasswordTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}password_object': 'PasswordObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}password_state': 'PasswordStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process_test': 'ProcessTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process_object': 'ProcessObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process_state': 'ProcessStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process58_test': 'Process58TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process58_object': 'Process58ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}process58_state': 'Process58StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}routingtable_test': 'RoutingTableTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}routingtable_object': 'RoutingTableObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}routingtable_state': 'RoutingTableStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}runlevel_test': 'RunLevelTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}runlevel_object': 'RunLevelObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}runlevel_state': 'RunLevelStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sccs_test': 'SccsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sccs_object': 'SccsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sccs_state': 'SccsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}shadow_test': 'ShadowTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}shadow_object': 'ShadowObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}shadow_state': 'ShadowStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}symlink_test': 'SymlinkTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}symlink_object': 'SymlinkObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}symlink_state': 'SymlinkStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sysctl_test': 'SysctlTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sysctl_object': 'SysctlObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}sysctl_state': 'SysctlStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}uname_test': 'UnameTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}uname_object': 'UnameObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}uname_state': 'UnameStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}xinetd_test': 'XinetdTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}xinetd_object': 'XinetdObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#unix}xinetd_state': 'XinetdStateElement',
}

CAPABILITY_ENUMERATION = [
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

ENDPOINT_ENUMERATION = [
    'stream',
    'dgram',
    'raw',
    'seqpacket',
    'tli',
    'sunrpc_tcp',
    'sunrpc_udp',
    '',
]

GCONF_TYPE_ENUMERATION = [
    'GCONF_VALUE_STRING',
    'GCONF_VALUE_INT',
    'GCONF_VALUE_FLOAT',
    'GCONF_VALUE_BOOL',
    'GCONF_VALUE_SCHEMA',
    'GCONF_VALUE_LIST',
    'GCONF_VALUE_PAIR',
    '',
]

ROUTING_TABLE_FLAGS_ENUMERATION = [
    'UP',
    'GATEWAY',
    'HOST',
    'REINSTATE',
    'DYNAMIC',
    'MODIFIED',
    'ADDRCONF',
    'CACHE',
    'REJECT',
    'REDUNDANT',
    'SETSRC',
    'BROADCAST',
    'LOCAL',
    'PROTOCOL_1',
    'PROTOCOL_2',
    'PROTOCOL_3',
    'BLACK_HOLE',
    'CLONING',
    'PROTOCOL_CLONING',
    'INTERFACE_SCOPE',
    'LINK_LAYER',
    'MULTICAST',
    'STATIC',
    'WAS_CLONED',
    'XRESOLVE',
    'USABLE',
    'ACTIVE_DEAD_GATEWAY_DETECTION',
    '',
]

XINETD_TYPE_STATUS_ENUMERATION = [
    'INTERNAL',
    'RPC',
    'UNLISTED',
    'TCPMUX',
    'TCPMUXPLUS',
    '',
]

WAIT_STATUS_ENUMERATION = [
    'wait',
    'nowait',
    '',
]

ENCRYPT_METHOD_ENUMERATION = [
    'DES', # The DES method corresponds to the (none) prefix.
    'BSDi', # The BSDi method corresponds to BSDi modified DES or the '_' prefix.
    'MD5', # The MD5 method corresponds to MD5 for Linux/BSD or the $1$ prefix.
    'Blowfish', # The Blowfish method corresponds to Blowfish (OpenBSD) or the $2$ or $2a$ prefixes.
    'Sun MD5', # The Sun MD5 method corresponds to the $md5$ prefix.
    'SHA-256', # The SHA-256 method corresponds to the $5$ prefix.
    'SHA-512', # The SHA-512 method corresponds to the $6$ prefix.
    '',
]

INTERFACE_TYPE_ENUMERATION = [
    'ARPHRD_ETHER',
    'ARPHRD_FDDI',
    'ARPHRD_LOOPBACK',
    'ARPHRD_VOID',
    'ARPHRD_PPP',
    'ARPHRD_SLIP',
    'ARPHRD_PRONET',
    '',
]
