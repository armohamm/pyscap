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

FIX_STRATEGY_ENUMERATION = [
    'unknown',
    # strategy not defined (default for forward compatibility for XCCDF 1.0)
    'configure',
    # adjust target config or settings
    'patch',
    # apply a patch, hotfix, or update
    'policy',
    # remediation by changing policies/procedures
    'disable',
    # turn off or deinstall something
    'enable',
    # turn on or install something
    'restrict',
    # adjust permissions or ACLs
    'update',
    # install upgrade or update the system
    'combination',
    # combo of two or more of the above
]
