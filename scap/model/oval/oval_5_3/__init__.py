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

}

CHECK_ENUMERATION = [
    'all',
    'at least one',
    'none exist',
    'none satisfy',
    'only one',
]


CHECK_RESULT_ENUMERATION = [
    'true',
    'false',
    'error',
    'unknown',
    'not evaluated',
    'not applicable',
]

def count_check_results(results):
    counts = {}
    for i in CHECK_RESULT_ENUMERATION:
        counts[i] = 0
    for r in results:
        counts[r] += 1
    return counts['true'], counts['false'], counts['error'], counts['unknown'], counts['not evaluated'], counts['not applicable']

def check_all(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_check_results(results)

    if true >= 1 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif false >= 1:
        return 'false'
    elif false == 0 and error >= 1:
        return 'error'
    elif false == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif false == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def check_at_least_one(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_check_results(results)

    if true >= 1:
        return 'true'
    elif true == 0 and false >= 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'false'
    elif true == 0 and error >= 1:
        return 'error'
    elif true == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif true == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def check_none_satisfy(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_check_results(results)

    if true == 0 and false >= 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif true >= 1:
        return 'false'
    elif true == 0 and error >= 1:
        return 'error'
    elif true == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif true == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def check_only_one(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_check_results(results)

    if true == 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif true >= 1:
        return 'false'
    elif true == 0 and false >= 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'false'
    elif (true == 0 or true == 1) and error >=1:
        return 'error'
    elif (true == 0 or true == 1) and error == 0 and unknown >= 1:
        return 'unknown'
    elif (true == 0 or true == 1) and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

DATATYPE_ENUMERATION = [
    'binary',
    'boolean',
    'evr_string',
    'float',
    'ios_version',
    'int',
    'string',
    'version',
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

def count_existence_results(item_status_values):
    counts = {}
    for i in EXISTENCE_RESULT_ENUMERATION:
        counts[i] = 0

    for v in item_status_values:
        counts[v] += 1

    return counts['exists'], counts['does not exist'], counts['error'], counts['not collected']

def existence_all_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_existence_results(item_status_values)

    if exists >= 1 and does_not_exist == 0 and error == 0 and not_collected == 0:
        return 'true'
    elif exists == 0 and does_not_exist == 0 and error == 0 and not_collected == 0:
        return 'false'
    elif does_not_exist >= 1:
        return 'false'
    elif does_not_exist == 0 and error >= 1:
        return 'error'
    elif does_not_exist == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def existence_any_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_existence_results(item_status_values)

    if error == 0:
        return 'true'
    elif exists >= 1 and error >= 1:
        return 'true'
    elif exists == 0 and error >= 1:
        return 'error'

def existence_at_least_one_exists(item_status_values):
    exists, does_not_exist, error, not_collected = count_existence_results(item_status_values)

    if exists >= 1:
        return 'true'
    elif exists == 0 and does_not_exist >= 1 and error == 0 and not_collected == 0:
        return 'false'
    elif exists == 0 and error >= 1:
        return 'error'
    elif exist == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def existence_none_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_existence_results(item_status_values)

    if exists == 0 and error == 0 and not_collected == 0:
        return 'true'
    elif exists >= 1:
        return 'false'
    elif exists == 0 and error >= 1:
        return 'error'
    elif exists == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def existence_only_one_exists(item_status_values):
    exists, does_not_exist, error, not_collected = count_existence_results(item_status_values)

    if exists == 1 and error == 0 and not_collected == 0:
        return 'true'
    elif exists >= 2:
        return 'false'
    elif exists == 0 and error == 0 and not_collected == 0:
        return 'false'
    elif (exists == 0 or exists == 1) and error >= 1:
        return 'error'
    elif (exists == 0 or exists == 1) and error == 0 and not_collected >= 1:
        return 'unknown'

FAMILY_ENUMERATION = [
    'ios',                      # The ios value describes the Cisco IOS operating system.
    'macos',                    # The macos value describes the Mac operating system.
    'unix',                     # The unix value describes the UNIX operating system.
    'windows',                  # The windows value describes the Microsoft Windows operating system.
]

MESSAGE_LEVEL_ENUMERATION = [
    'debug',    # Debug messages should only be displayed by a tool when run in some sort of verbose mode.
    'error',    # Error messages should be recorded when there was an error that did not allow the collection of specific data.
    'fatal',    # A fatal message should be recorded when an error causes the failure of more than just a single piece of data.
    'info',     # Info messages are used to pass useful information about the data collection to a user.
    'warning',  # A warning message reports something that might not correct but information was still collected.
]

OPERATION_ENUMERATION = [
    'equals',
    'not equal',
    'greater than',
    'less than',
    'greater than or equal',
    'less than or equal',
    'bitwise and',
    'bitwise or',
    'pattern match',
]

OPERATOR_ENUMERATION = [
    'AND',
    'ONE',
    'OR',
    'XOR',
]

# NOTE: we include negate here as a convenient place to store the function
def operator_negate(value):
    if value == 'true':
        return 'false'
    elif value == 'false':
        return 'true'
    else:
        return value

def count_operator_results(values):
    counts = {
        'true': 0,
        'false': 0,
        'error': 0,
        'unknown': 0,
        'not evaluated': 0,
        'not applicable': 0,
    }
    for val in values:
        counts[val] += 1

    return counts['true'], counts['false'], counts['error'], counts['unknown'], \
        counts['not evaluated'], counts['not applicable']

def operator_AND(values):
    t, f, e, u, ne, na = count_operator_results(values)
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

def operator_ONE(values):
    t, f, e, u, ne, na = count_operator_results(values)
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

def operator_OR(values):
    t, f, e, u, ne, na = count_operator_results(values)
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

def operator_XOR(values):
    t, f, e, u, ne, na = count_operator_results(values)
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
