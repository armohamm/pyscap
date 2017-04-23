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

ROLE_ENUMERATION = [
    'full',
    # if the rule is selected, then check it and let the result contribute to
    # the score and appear in reports (default, for compatibility for XCCDF
    # 1.0).
    'unscored',
    # check the rule, and include the results in  any report, but do not include
    # the result in  score computations (in the default scoring model the same
    # effect can be achieved with weight=0)
    'unchecked',
    # don't check the rule, just force the result status to 'unknown'.  Include
    # the rule's  information in any reports.
]
