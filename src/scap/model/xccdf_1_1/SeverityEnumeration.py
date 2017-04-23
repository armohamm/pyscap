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

SEVERITY_ENUMERATION = [
    'unknown',
    # severity not defined (default, for forward compatibility from XCCDF 1.0)
    'info',
    # rule is informational only, failing the rule does not imply failure to
    # conform to the security guidance of the benchmark. (usually would also
    # have a weight of 0)
    'low',
    # not a serious problem
    'medium',
    # fairly serious problem
    'high',
    # a grave or critical problem
]
