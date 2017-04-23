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

RESULT_ENUMERATION = [
    'pass',
    # the test passed, target complies w/ benchmark
    'fail',
    # the test failed, target does not comply
    'error',
    # an error occurred and test could not complete, or the test does not apply
    # to this plaform
    'unknown',
    # could not tell what happened, results  with this status are not to be
    # scored
    'notapplicable',
    # Rule did not apply to test target
    'fixed',
    # rule failed, but was later fixed (score as pass)
    'notchecked',
    # Rule did not cause any evaluation by the checking engine (role of
    # "unchecked")
    'notselected',
    # Rule was not selected in the Benchmark, and therefore was not checked
    # (selected="0")
    'informational',
    # Rule was evaluated by the checking engine, but isn't to be scored (role of
    # "unscored")
]
