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
    '{http://oval.mitre.org/XMLSchema/oval-common-5}deprecated_info': 'DeprecatedInfoElement',
    '{http://oval.mitre.org/XMLSchema/oval-common-5}element_mapping': 'ElementMappingElement',
    '{http://oval.mitre.org/XMLSchema/oval-common-5}notes': 'NotesElement',
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

DATATYPE_ENUMERATION = [
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

    'record',
]

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
