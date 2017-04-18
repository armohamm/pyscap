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

WARNING_CATEGORY_ENUMERATION = [
    'general',
    # broad or general-purpose warning (default for compatibility for XCCDF 1.0)
    'functionality',
    # warning about possible impacts to functionality or operational features
    'performance',
    # warning about changes to target system performance or throughput
    'hardware',
    # warning about hardware restrictions or possible impacts to hardware
    'legal',
    # warning about legal implications
    'regulatory',
    # warning about regulatory obligations or compliance implications
    'management',
    # warning about impacts to the mgmt or administration of the target system
    'audit',
    # warning about impacts to audit or logging
    'dependency',
    # warning about dependencies between this Rule and other parts of the target
    # system, or version dependencies.
]
