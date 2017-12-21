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
    ('http://oval.mitre.org/XMLSchema/oval-common-5', 'deprecated_info'): 'DeprecatedInfoElement',
    ('http://oval.mitre.org/XMLSchema/oval-common-5', 'element_mapping'): 'ElementMappingElement',
    ('http://oval.mitre.org/XMLSchema/oval-common-5', 'notes'): 'NotesElement',
}

CHECK_ENUMERATION = [
    'all',
    'at least one',
    'none exist',
    'none satisfy',
    'only one',
]

RESULT_ENUMERATION = [
    'true',
    'false',
    'error',
    'unknown',
    'not evaluated',
    'not applicable',
]

def check_all(t, f, e, u, ne, na):
    if t >= 1 and f == 0 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif f >= 1:
        return 'false'
    elif f == 0 and e >= 1:
        return 'error'
    elif f == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif f == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

def check_at_least_one(t, f, e, u, ne, na):
    if t >= 1:
        return 'true'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif t == 0 and e >= 1:
        return 'error'
    elif t == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif t == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

def check_none_satisfy(t, f, e, u, ne, na):
    if t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t >= 1:
        return 'false'
    elif t == 0 and e >= 1:
        return 'error'
    elif t == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif t == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

def check_only_one(t, f, e, u, ne, na):
    if t == 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t >= 1:
        return 'false'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif (t == 0 or t == 1) and e >=1:
        return 'error'
    elif (t == 0 or t == 1) and e == 0 and u >= 1:
        return 'unknown'
    elif (t == 0 or t == 1) and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

CLASS_ENUMERATION = [
    'compliance',
    'inventory',
    'miscellaneous',
    'patch',
    'vulnerability',
]

COMPLEX_DATATYPE_ENUMERATION = [
    'record',
]

SIMPLE_DATATYPE_ENUMERATION = [
    'binary',
    'boolean',
    'evr_string',
    'debian_evr_string',
    'fileset_revision',
    'float',
    'ios_version',
    'int',
    'ipv4_address',
    'ipv6_address',
    'string',
    'version',
]

DATATYPE_ENUMERATION = []
DATATYPE_ENUMERATION.extend(SIMPLE_DATATYPE_ENUMERATION)
DATATYPE_ENUMERATION.extend(COMPLEX_DATATYPE_ENUMERATION)

EXISTENCE_ENUMERATION = [
    'all_exist',
    'any_exist',
    'at_least_one_exists',
    'none_exist',
    'only_one_exists',
]

EXISTENCE_RESULT_ENUMERATION = [
    'exists',
    'does not exist',
    'error',
    'not collected',
]

def existence_all_exist(ex, dne, e, nc):
    if ex >= 1 and dne == 0 and e == 0 and nc == 0:
        return 'true'
    elif ex == 0 and dne == 0 and e == 0 and nc == 0:
        return 'false'
    elif dne >= 1:
        return 'false'
    elif dne == 0 and e >= 1:
        return 'error'
    elif dne == 0 and e == 0 and nc >= 1:
        return 'unknown'

def existence_any_exist(ex, dne, e, nc):
    if e == 0:
        return 'true'
    elif ex >= 1 and e >= 1:
        return 'true'
    elif ex == 0 and e >= 1:
        return 'error'

def existence_at_least_one_exists(ex, dne, e, nc):
    if ex >= 1:
        return 'true'
    elif ex == 0 and dne >= 1 and e == 0 and nc == 0:
        return 'false'
    elif ex == 0 and e >= 1:
        return 'error'
    elif exist == 0 and e == 0 and nc >= 1:
        return 'unknown'

def existence_none_exist(ex, dne, e, nc):
    if ex == 0 and e == 0 and nc == 0:
        return 'true'
    elif ex >= 1:
        return 'false'
    elif ex == 0 and e >= 1:
        return 'error'
    elif ex == 0 and e == 0 and nc >= 1:
        return 'unknown'

def existence_only_one_exists(ex, dne, e, nc):
    if ex == 1 and e == 0 and nc == 0:
        return 'true'
    elif ex >= 2:
        return 'false'
    elif ex == 0 and e == 0 and nc == 0:
        return 'false'
    elif (ex == 0 or ex == 1) and e >= 1:
        return 'error'
    elif (ex == 0 or ex == 1) and e == 0 and nc >= 1:
        return 'unknown'

FAMILY_ENUMERATION = [
    'android',                  # The android value describes the Android mobile operating system.
    'asa',                      # The asa value describes the Cisco ASA security devices.
    'apple_ios',                # The apple_ios value describes the iOS mobile operating system.
    'catos',                    # The catos value describes the Cisco CatOS operating system.
    'ios',                      # The ios value describes the Cisco IOS operating system.
    'iosxe',                    # The iosxe value describes the Cisco IOS XE operating system.
    'junos',                    # The junos value describes the Juniper JunOS operating system.
    'macos',                    # The macos value describes the Mac operating system.
    'pixos',                    # The pixos value describes the Cisco PIX operating system.
    'undefined',                # The undefined value is to be used when the desired family is not available.
    'unix',                     # The unix value describes the UNIX operating system.
    'vmware_infrastructure',    # The vmware_infrastructure value describes VMWare Infrastructure.
    'windows',                  # The windows value describes the Microsoft Windows operating system.
]

MESSAGE_LEVEL_ENUMERATION = [
    'debug',
    'info',
    'warning',
    'error',
    'fatal',
]

OPERATION_ENUMERATION = [
    'equals',
    'not equal',
    'case insensitive equals',
    'case insensitive not equal',
    'greater than',
    'less than',
    'greater than or equal',
    'less than or equal',
    'bitwise and',
    'bitwise or',
    'pattern match',
    'subset of',
    'superset of',
]

OPERATOR_ENUMERATION = [
    'AND',
    'ONE',
    'OR',
    'XOR',
]

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1+ | 0  | 0  | 0  | 0  | 0+ ||  True
#                || 0+ | 1+ | 0+ | 0+ | 0+ | 0+ ||  False
#       AND      || 0+ | 0  | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0+ | 0  | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0+ | 0  | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def operator_AND(t, f, e, u, ne, na):
    if t >= 1 and f == 0 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif f >= 1:
        return 'false'
    elif f == 0 and e >= 1:
        return 'error'
    elif f == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif f == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1  | 0+ | 0  | 0  | 0  | 0+ ||  True
#                || 2+ | 0+ | 0+ | 0+ | 0+ | 0+ ||  ** False **
#                || 0  | 1+ | 0  | 0  | 0  | 0+ ||  ** False **
#       ONE      ||0,1 | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                ||0,1 | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                ||0,1 | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def operator_ONE(t, f, e, u, ne, na):
    if t == 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t >= 2:
        return 'false'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif (t == 0 or t == 1) and e >= 1:
        return 'error'
    elif (t == 0 or t == 1) and e == 0 and u >= 1:
        return 'unknown'
    elif (t == 0 or t == 1) and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1+ | 0+ | 0+ | 0+ | 0+ | 0+ ||  True
#                || 0  | 1+ | 0  | 0  | 0  | 0+ ||  False
#       OR       || 0  | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0  | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0  | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def operator_OR(t, f, e, u, ne, na):
    if t >= 1:
        return 'true'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif t == 0 and e >= 1:
        return 'error'
    elif t == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif t == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                ||odd | 0+ | 0  | 0  | 0  | 0+ ||  True
#                ||even| 0+ | 0  | 0  | 0  | 0+ ||  False
#       XOR      || 0+ | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0+ | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0+ | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def operator_XOR(t, f, e, u, ne, na):
    if t % 2 == 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t % 2 == 0 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif e >= 1:
        return 'error'
    elif e == 0 and u >= 1:
        return 'unknown'
    elif e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'


SET_OPERATOR_ENUMERATION = [
    'COMPLEMENT',
    'INTERSECTION',
    'UNION',
]

DATABASE_ENGINE_ENUMERATION = [
    'access',
    'db2',
    'cache',
    'firebird',
    'firstsql',
    'foxpro',
    'informix',
    'ingres',
    'interbase',
    'lightbase',
    'maxdb',
    'monetdb',
    'mimer',
    'mysql',
    'oracle',
    'paradox',
    'pervasive',
    'postgre',
    'sqlbase',
    'sqlite',
    'sqlserver',
    'sybase',
    '',
]

HASH_TYPE_ENUMERATION = [
    'MD5',
    'SHA-1',
    'SHA-224',
    'SHA-256',
    'SHA-384',
    'SHA-512',
    '',
]

LDAP_TYPE_ENUMERATION = [
    'LDAPTYPE_ACI_ITEM',
    'LDAPTYPE_ACCESS_POINT',
    'LDAPTYPE_ATTRIBUTE_TYPE_DESCRIP_STRING',
    'LDAPTYPE_AUDIO',
    'LDAPTYPE_BINARY',
    'LDAPTYPE_BIT_STRING',
    'LDAPTYPE_BOOLEAN',
    'LDAPTYPE_CERTIFICATE',
    'LDAPTYPE_CERTIFICATE_LIST',
    'LDAPTYPE_CERTIFICATE_PAIR',
    'LDAPTYPE_COUNTRY_STRING',
    'LDAPTYPE_DN_STRING',
    'LDAPTYPE_DATA_QUALITY_SYNTAX',
    'LDAPTYPE_DELIVERY_METHOD',
    'LDAPTYPE_DIRECTORY_STRING',
    'LDAPTYPE_DIR_CONTENT_RULE_DESCRIPTION',
    'LDAPTYPE_DIT_STRUCTURE_RULE_DESCRIPTION',
    'LDAPTYPE_DL_SUBMIT_PERMISSION',
    'LDAPTYPE_DSA_QUALITY_SYNTAX',
    'LDAPTYPE_DSE_TYPE',
    'LDAPTYPE_ENHANCED_GUIDE',
    'LDAPTYPE_FAX_TEL_NUMBER',
    'LDAPTYPE_FAX',
    'LDAPTYPE_GENERALIZED_TIME',
    'LDAPTYPE_GUIDE',
    'LDAPTYPE_IA5_STRING',
    'LDAPTYPE_INTEGER',
    'LDAPTYPE_JPEG',
    'LDAPTYPE_LDAP_SYNTAX_DESCRIPTION',
    'LDAPTYPE_LDAP_SCHEMA_DEFINITION',
    'LDAPTYPE_LDAP_SCHEMA_DESCRIPTION',
    'LDAPTYPE_MASTER_AND_SHADOW_ACCESS_POINTS',
    'LDAPTYPE_MATCHING_RULE_DESCRIPTION',
    'LDAPTYPE_MATCHING_RULE_USE_DESCRIPTION',
    'LDAPTYPE_MAIL_PREFERENCE',
    'LDAPTYPE_MHS_OR_ADDRESS',
    'LDAPTYPE_MODIFY_RIGHTS',
    'LDAPTYPE_NAME_AND_OPTIONAL_UID',
    'LDAPTYPE_NAME_FORM_DESCRIPTION',
    'LDAPTYPE_NUMERIC_STRING',
    'LDAPTYPE_OBJECT_CLASS_DESCRIP_STRING',
    'LDAPTYPE_OCTET_STRING',
    'LDAPTYPE_OID',
    'LDAPTYPE_MAILBOX',
    'LDAPTYPE_POSTAL_ADDRESS',
    'LDAPTYPE_PROTOCOL_INFORMATION',
    'LDAPTYPE_PRESENTATION_ADDRESS',
    'LDAPTYPE_PRINTABLE_STRING',
    'LDAPTYPE_SUBSTRING_ASSERTION',
    'LDAPTYPE_SUBTREE_SPECIFICATION',
    'LDAPTYPE_SUPPLIER_INFORMATION',
    'LDAPTYPE_SUPPLIER_OR_CONSUMER',
    'LDAPTYPE_SUPPLIER_AND_CONSUMER',
    'LDAPTYPE_SUPPORTED_ALGORITHM',
    'LDAPTYPE_TELEPHONE_NUMBER',
    'LDAPTYPE_TELEX_TERMINAL_ID',
    'LDAPTYPE_TELEX_NUMBER',
    'LDAPTYPE_UTC_TIME',
    'LDAPTYPE_TIMESTAMP', # deprecated
    'LDAPTYPE_EMAIL', # deprecated
    '',
]

WINDOWS_VIEW_ENUMERATION = [
    '32_bit',
    '64_bit',
    '',
]

LINUX_PROTOCOL_ENUMERATION = [
    'ETH_P_LOOP',
    'ETH_P_PUP',
    'ETH_P_PUPAT',
    'ETH_P_IP',
    'ETH_P_X25',
    'ETH_P_ARP',
    'ETH_P_BPQ',
    'ETH_P_IEEEPUP',
    'ETH_P_IEEEPUPAT',
    'ETH_P_DEC',
    'ETH_P_DNA_DL',
    'ETH_P_DNA_RC',
    'ETH_P_DNA_RT',
    'ETH_P_LAT',
    'ETH_P_DIAG',
    'ETH_P_CUST',
    'ETH_P_SCA',
    'ETH_P_RARP',
    'ETH_P_ATALK',
    'ETH_P_AARP',
    'ETH_P_8021Q',
    'ETH_P_IPX',
    'ETH_P_IPV6',
    'ETH_P_SLOW',
    'ETH_P_WCCP',
    'ETH_P_PPP_DISC',
    'ETH_P_PPP_SES',
    'ETH_P_MPLS_UC',
    'ETH_P_MPLS_MC',
    'ETH_P_ATMMPOA',
    'ETH_P_ATMFATE',
    'ETH_P_AOE',
    'ETH_P_TIPC',
    'ETH_P_802_3',
    'ETH_P_AX25',
    'ETH_P_ALL',
    'ETH_P_802_2',
    'ETH_P_SNAP',
    'ETH_P_DDCMP',
    'ETH_P_WAN_PPP',
    'ETH_P_PPP_MP',
    'ETH_P_PPPTALK',
    'ETH_P_LOCALTALK',
    'ETH_P_TR_802_2',
    'ETH_P_MOBITEX',
    'ETH_P_CONTROL',
    'ETH_P_IRDA',
    'ETH_P_ECONET',
    'ETH_P_HDLC',
    'ETH_P_ARCNET',
    '',
]

RPM_VERIFY_RESULT_ENUMERATION = [
    'pass',
    'fail',
    'not performed',
    '',
]

UNIX_CAPABILITY_ENUMERATION = [
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

UNIX_ENDPOINT_ENUMERATION = [
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

UNIX_ROUTING_TABLE_FLAGS_ENUMERATION = [
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

UNIX_WAIT_STATUS_ENUMERATION = [
    'wait',
    'nowait',
    '',
]

UNIX_ENCRYPT_METHOD_ENUMERATION = [
    'DES', # The DES method corresponds to the (none) prefix.
    'BSDi', # The BSDi method corresponds to BSDi modified DES or the '_' prefix.
    'MD5', # The MD5 method corresponds to MD5 for Linux/BSD or the $1$ prefix.
    'Blowfish', # The Blowfish method corresponds to Blowfish (OpenBSD) or the $2$ or $2a$ prefixes.
    'Sun MD5', # The Sun MD5 method corresponds to the $md5$ prefix.
    'SHA-256', # The SHA-256 method corresponds to the $5$ prefix.
    'SHA-512', # The SHA-512 method corresponds to the $6$ prefix.
    '',
]

UNIX_INTERFACE_TYPE_ENUMERATION = [
    'ARPHRD_ETHER',
    'ARPHRD_FDDI',
    'ARPHRD_LOOPBACK',
    'ARPHRD_VOID',
    'ARPHRD_PPP',
    'ARPHRD_SLIP',
    'ARPHRD_PRONET',
    '',
]

WINDOWS_ADDR_TYPE_ENUMERATION = [
    'MIB_IPADDR_DELETED',
    'MIB_IPADDR_DISCONNECTED',
    'MIB_IPADDR_DYNAMIC',
    'MIB_IPADDR_PRIMARY',
    'MIB_IPADDR_TRANSIENT',
    '',
]

ADSTYPE_ENUMERATION = [
    'ADSTYPE_INVALID',
    'ADSTYPE_DN_STRING',
    'ADSTYPE_CASE_EXACT_STRING',
    'ADSTYPE_CASE_IGNORE_STRING',
    'ADSTYPE_PRINTABLE_STRING',
    'ADSTYPE_NUMERIC_STRING',
    'ADSTYPE_BOOLEAN',
    'ADSTYPE_INTEGER',
    'ADSTYPE_OCTET_STRING',
    'ADSTYPE_UTC_TIME',
    'ADSTYPE_LARGE_INTEGER',
    'ADSTYPE_PROV_SPECIFIC',
    'ADSTYPE_OBJECT_CLASS',
    'ADSTYPE_CASEIGNORE_LIST',
    'ADSTYPE_OCTET_LIST',
    'ADSTYPE_PATH',
    'ADSTYPE_POSTALADDRESS',
    'ADSTYPE_TIMESTAMP',
    'ADSTYPE_BACKLINK',
    'ADSTYPE_TYPEDNAME',
    'ADSTYPE_HOLD',
    'ADSTYPE_NETADDRESS',
    'ADSTYPE_REPLICAPOINTER',
    'ADSTYPE_FAXNUMBER',
    'ADSTYPE_EMAIL',
    'ADSTYPE_NT_SECURITY_DESCRIPTOR',
    'ADSTYPE_UNKNOWN',
    'ADSTYPE_DN_WITH_BINARY',
    'ADSTYPE_DN_WITH_STRING',
    '',
]

WINDOWS_AUDIT_ENUMERATION = [
    'AUDIT_FAILURE',
    'AUDIT_NONE',
    'AUDIT_SUCCESS',
    'AUDIT_SUCCESS_FAILURE',
    '',
]

CMDLET_VERB_ENUMERATION = [
    'Approve',
    'Assert',
    'Compare',
    'Confirm',
    'Find',
    'Get',
    'Measure',
    'Read',
    'Request',
    'Resolve',
    'Search',
    'Select',
    'Show',
    'Test',
    'Trace',
    'Watch',
    '',
]

WINDOWS_DRIVE_TYPE_ENUMERATION = [
    'DRIVE_UNKNOWN',
    'DRIVE_NO_ROOT_DIR',
    'DRIVE_REMOVABLE',
    'DRIVE_FIXED',
    'DRIVE_REMOTE',
    'DRIVE_CDROM',
    'DRIVE_RAMDISK',
    '',
]

WINDOWS_FILE_TYPE_ENUMERATION = [
    'FILE_ATTRIBUTE_DIRECTORY',
    'FILE_TYPE_CHAR',
    'FILE_TYPE_DISK',
    'FILE_TYPE_PIPE',
    'FILE_TYPE_REMOTE',
    'FILE_TYPE_UNKNOWN',
    '',
]

WINDOWS_INTERFACE_TYPE_ENUMERATION = [
    'MIB_IF_TYPE_ETHERNET',
    'MIB_IF_TYPE_FDDI',
    'MIB_IF_TYPE_LOOPBACK',
    'MIB_IF_TYPE_OTHER',
    'MIB_IF_TYPE_PPP',
    'MIB_IF_TYPE_SLIP',
    'MIB_IF_TYPE_TOKENRING',
    '',
]

WINDOWS_NAMING_CONTEXT_ENUMERATION = [
    'domain',
    'configuration',
    'schema',
    '',
]

NTUSER_ACCOUNT_TYPE_ENUMERATION = [
    'local',
    'domain',
    '',
]

PE_SUBSYSTEM_ENUMERATION = [
    'IMAGE_SUBSYSTEM_UNKNOWN',
    'IMAGE_SUBSYSTEM_NATIVE',
    'IMAGE_SUBSYSTEM_WINDOWS_GUI',
    'IMAGE_SUBSYSTEM_WINDOWS_CUI',
    'IMAGE_SUBSYSTEM_OS2_CUI',
    'IMAGE_SUBSYSTEM_POSIX_CUI',
    'IMAGE_SUBSYSTEM_WINDOWS_CE_GUI',
    'IMAGE_SUBSYSTEM_EFI_APPLICATION',
    'IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER',
    'IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER',
    'IMAGE_SUBSYSTEM_EFI_ROM',
    'IMAGE_SUBSYSTEM_XBOX',
    'IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION',
    '',
]

PE_TARGET_MACHINE_ENUMERATION = [
    'IMAGE_FILE_MACHINE_UNKNOWN',
    'IMAGE_FILE_MACHINE_ALPHA',
    'IMAGE_FILE_MACHINE_ARM',
    'IMAGE_FILE_MACHINE_ALPHA64',
    'IMAGE_FILE_MACHINE_I386',
    'IMAGE_FILE_MACHINE_IA64',
    'IMAGE_FILE_MACHINE_M68K',
    'IMAGE_FILE_MACHINE_MIPS16',
    'IMAGE_FILE_MACHINE_MIPSFPU',
    'IMAGE_FILE_MACHINE_MIPSFPU16',
    'IMAGE_FILE_MACHINE_POWERPC',
    'IMAGE_FILE_MACHINE_R3000',
    'IMAGE_FILE_MACHINE_R4000',
    'IMAGE_FILE_MACHINE_R10000',
    'IMAGE_FILE_MACHINE_SH3',
    'IMAGE_FILE_MACHINE_SH4',
    'IMAGE_FILE_MACHINE_THUMB',
    '',
]

IP_PROTOCOL_ENUMERATION = [
    'TCP',
    'UDP',
    '',
]

WINDOWS_REGISTRY_HIVE_ENUMERATION = [
    'HKEY_CLASSES_ROOT',
    'HKEY_CURRENT_CONFIG',
    'HKEY_CURRENT_USER',
    'HKEY_LOCAL_MACHINE',
    'HKEY_USERS',
    '',
]

WINDOWS_REGISTRY_TYPE_ENUMERATION = [
    'reg_binary',
    'reg_dword',
    'reg_dword_little_endian',
    'reg_dword_big_endian',
    'reg_expand_sz',
    'reg_link',
    'reg_multi_sz',
    'reg_none',
    'reg_qword',
    'reg_qword_little_endian',
    'reg_sz',
    'reg_resource_list',
    'reg_full_resource_descriptor',
    'reg_resource_requirements_list',
    '',
]

WINDOWS_SERVICE_CONTROLS_ACCEPTED_ENUMERATION = [
    'SERVICE_ACCEPT_NETBINDCHANGE',
    'SERVICE_ACCEPT_PARAMCHANGE',
    'SERVICE_ACCEPT_PAUSE_CONTINUE',
    'SERVICE_ACCEPT_PRESHUTDOWN',
    'SERVICE_ACCEPT_SHUTDOWN',
    'SERVICE_ACCEPT_STOP',
    'SERVICE_ACCEPT_HARDWAREPROFILECHANGE',
    'SERVICE_ACCEPT_POWEREVENT',
    'SERVICE_ACCEPT_SESSIONCHANGE',
    'SERVICE_ACCEPT_TIMECHANGE',
    'SERVICE_ACCEPT_TRIGGEREVENT',
    '',
]

WINDOWS_SERVICE_CURRENT_STATE_ENUMERATION = [
    'SERVICE_CONTINUE_PENDING',
    'SERVICE_PAUSE_PENDING',
    'SERVICE_PAUSED',
    'SERVICE_RUNNING',
    'SERVICE_START_PENDING',
    'SERVICE_STOP_PENDING',
    'SERVICE_STOPPED',
    '',
]

WINDOWS_SERVICE_START_TYPE_ENUMERATION = [
    'SERVICE_AUTO_START',
    'SERVICE_BOOT_START',
    'SERVICE_DEMAND_START',
    'SERVICE_DISABLED',
    'SERVICE_SYSTEM_START',
    '',
]

WINDOWS_SERVICE_TYPE_ENUMERATION = [
    'SERVICE_FILE_SYSTEM_DRIVER',
    'SERVICE_KERNEL_DRIVER',
    'SERVICE_WIN32_OWN_PROCESS',
    'SERVICE_WIN32_SHARE_PROCESS',
    'SERVICE_INTERACTIVE_PROCESS',
    '',
]

WINDOWS_SHARED_RESOURCE_TYPE_ENUMERATION = [
    'STYPE_DISKTREE',
    'STYPE_DISKTREE_SPECIAL',
    'STYPE_DISKTREE_TEMPORARY',
    'STYPE_DISKTREE_SPECIAL_TEMPORARY',
    'STYPE_PRINTQ',
    'STYPE_PRINTQ_SPECIAL',
    'STYPE_PRINTQ_TEMPORARY',
    'STYPE_PRINTQ_SPECIAL_TEMPORARY',
    'STYPE_DEVICE',
    'STYPE_DEVICE_SPECIAL',
    'STYPE_DEVICE_TEMPORARY',
    'STYPE_DEVICE_SPECIAL_TEMPORARY',
    'STYPE_IPC',
    'STYPE_IPC_SPECIAL',
    'STYPE_IPC_TEMPORARY',
    'STYPE_IPC_SPECIAL_TEMPORARY',
    'STYPE_SPECIAL',
    'STYPE_TEMPORARY',
    '',
]

WINDOWS_SYSTEM_METRIC_INDEX_ENUMERATION = [
    'SM_ARRANGE',
    'SM_CLEANBOOT',
    'SM_CMONITORS',
    'SM_CMOUSEBUTTONS',
    'SM_CXBORDER',
    'SM_CXCURSOR',
    'SM_CXDLGFRAME',
    'SM_CXDOUBLECLK',
    'SM_CXDRAG',
    'SM_CXEDGE',
    'SM_CXFIXEDFRAME',
    'SM_CXFOCUSBORDER',
    'SM_CXFRAME',
    'SM_CXFULLSCREEN',
    'SM_CXHSCROLL',
    'SM_CXHTHUMB',
    'SM_CXICON',
    'SM_CXICONSPACING',
    'SM_CXMAXIMIZED',
    'SM_CXMAXTRACK',
    'SM_CXMENUCHECK',
    'SM_CXMENUSIZE',
    'SM_CXMIN',
    'SM_CXMINIMIZED',
    'SM_CXMINSPACING',
    'SM_CXMINTRACK',
    'SM_CXPADDEDBORDER',
    'SM_CXSCREEN',
    'SM_CXSIZE',
    'SM_CXSIZEFRAME',
    'SM_CXSMICON',
    'SM_CXSMSIZE',
    'SM_CXVIRTUALSCREEN',
    'SM_CXVSCROLL',
    'SM_CYBORDER',
    'SM_CYCAPTION',
    'SM_CYCURSOR',
    'SM_CYDLGFRAME',
    'SM_CYDOUBLECLK',
    'SM_CYDRAG',
    'SM_CYEDGE',
    'SM_CYFIXEDFRAME',
    'SM_CYFOCUSBORDER',
    'SM_CYFRAME',
    'SM_CYFULLSCREEN',
    'SM_CYHSCROLL',
    'SM_CYICON',
    'SM_CYICONSPACING',
    'SM_CYKANJIWINDOW',
    'SM_CYMAXIMIZED',
    'SM_CYMAXTRACK',
    'SM_CYMENU',
    'SM_CYMENUCHECK',
    'SM_CYMENUSIZE',
    'SM_CYMIN',
    'SM_CYMINIMIZED',
    'SM_CYMINSPACING',
    'SM_CYMINTRACK',
    'SM_CYSCREEN',
    'SM_CYSIZE',
    'SM_CYSIZEFRAME',
    'SM_CYSMCAPTION',
    'SM_CYSMICON',
    'SM_CYSMSIZE',
    'SM_CYVIRTUALSCREEN',
    'SM_CYVSCROLL',
    'SM_CYVTHUMB',
    'SM_DBCSENABLED',
    'SM_DEBUG',
    'SM_DIGITIZER',
    'SM_IMMENABLED',
    'SM_MAXIMUMTOUCHES',
    'SM_MEDIACENTER',
    'SM_MENUDROPALIGNMENT',
    'SM_MIDEASTENABLED',
    'SM_MOUSEPRESENT',
    'SM_MOUSEHORIZONTALWHEELPRESENT',
    'SM_MOUSEWHEELPRESENT',
    'SM_NETWORK',
    'SM_PENWINDOWS',
    'SM_REMOTECONTROL',
    'SM_REMOTESESSION',
    'SM_SAMEDISPLAYFORMAT',
    'SM_SECURE',
    'SM_SERVERR2',
    'SM_SHOWSOUNDS',
    'SM_SHUTTINGDOWN',
    'SM_SLOWMACHINE',
    'SM_STARTER',
    'SM_SWAPBUTTON',
    'SM_TABLETPC',
    'SM_XVIRTUALSCREEN',
    'SM_YVIRTUALSCREEN',
    '',
]

WINDOWS_USER_RIGHT_ENUMERATION = [
    'SE_ASSIGNPRIMARYTOKEN_NAME',
    'SE_AUDIT_NAME',
    'SE_BACKUP_NAME',
    'SE_CHANGE_NOTIFY_NAME',
    'SE_CREATE_GLOBAL_NAME',
    'SE_CREATE_PAGEFILE_NAME',
    'SE_CREATE_PERMANENT_NAME',
    'SE_CREATE_SYMBOLIC_LINK_NAME',
    'SE_CREATE_TOKEN_NAME',
    'SE_DEBUG_NAME',
    'SE_ENABLE_DELEGATION_NAME',
    'SE_IMPERSONATE_NAME',
    'SE_INC_BASE_PRIORITY_NAME',
    'SE_INCREASE_QUOTA_NAME',
    'SE_INC_WORKING_SET_NAME',
    'SE_LOAD_DRIVER_NAME',
    'SE_LOCK_MEMORY_NAME',
    'SE_MACHINE_ACCOUNT_NAME',
    'SE_MANAGE_VOLUME_NAME',
    'SE_PROF_SINGLE_PROCESS_NAME',
    'SE_RELABEL_NAME',
    'SE_REMOTE_SHUTDOWN_NAME',
    'SE_RESTORE_NAME',
    'SE_SECURITY_NAME',
    'SE_SHUTDOWN_NAME',
    'SE_SYNC_AGENT_NAME',
    'SE_SYSTEM_ENVIRONMENT_NAME',
    'SE_SYSTEM_PROFILE_NAME',
    'SE_SYSTEMTIME_NAME',
    'SE_TAKE_OWNERSHIP_NAME',
    'SE_TCB_NAME',
    'SE_TIME_ZONE_NAME',
    'SE_TRUSTED_CREDMAN_ACCESS_NAME',
    'SE_UNDOCK_NAME',
    'SE_UNSOLICITED_INPUT_NAME',
    'SE_BATCH_LOGON_NAME',
    'SE_DENY_BATCH_LOGON_NAME',
    'SE_DENY_INTERACTIVE_LOGON_NAME',
    'SE_DENY_NETWORK_LOGON_NAME',
    'SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME',
    'SE_DENY_SERVICE_LOGON_NAME',
    'SE_INTERACTIVE_LOGON_NAME',
    'SE_NETWORK_LOGON_NAME',
    'SE_REMOTE_INTERACTIVE_LOGON_NAME',
    'SE_SERVICE_LOGON_NAME',
    '',
]
