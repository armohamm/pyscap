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

from scap.Model import Model
from scap.model.decorators import *

logger = logging.getLogger(__name__)

@attribute(local_name='max_depth', type='Integer', default=-1)
# 'max_depth' defines the maximum depth of recursion to perform when a
# recurse_direction is specified. A value of '0' is equivalent to no recursion,
# '1' means to step only one directory level up/down, and so on. The default
# value is '-1' meaning no limitation. For a 'max_depth' of -1 or any value of 1
# or more the starting directory must be considered in the recursive search.

# Note that the default recurse_direction behavior is 'none' so even though
# max_depth specifies no limitation by default, the recurse_direction behavior
# turns recursion off.

# Note that this behavior only applies with the equality operation on the path
# entity.
@attribute(local_name='recurse', enum=['directories', 'symlinks', 'symlinks and directories'], default='symlinks and directories')
# 'recurse' defines how to recurse into the path entity, in other words what to
# follow during recursion. Options include symlinks, directories, or both. Note
# that a max-depth other than 0 has to be specified for recursion to take place
# and for this attribute to mean anything. Also note that this behavior does not
# apply to Windows systems since they do not support symbolic links. On Windows
# systems the 'recurse' behavior is always equivalent to directories.

# Note that this behavior only applies with the equality operation on the path
# entity.
@attribute(local_name='recurse_direction', enum=['none', 'up', 'down'], default='none')
# 'recurse_direction' defines the direction to recurse, either 'up' to parent
# directories, or 'down' into child directories. The default value is 'none' for
# no recursion.

# Note that this behavior only applies with the equality operation on the path
# entity.
@attribute(local_name='recurse_file_system', enum=['all', 'local', 'defined'], default='all')
# 'recurse_file_system' defines the file system limitation of any searching and
# applies to all operations as specified on the path or filepath entity.

# The value of 'local' limits the search scope to local file systems (as opposed
# to file systems mounted from an external system).

# The value of 'defined' keeps any recursion within the file system that the
# file_object (path+filename or filepath) has specified. For example, on
# Windows, if the path specified was "C:\", you would search only the C: drive,
# not other filesystems mounted to descendant paths. Similarly, on UNIX, if the
# path specified was "/", you would search only the filesystem mounted there,
# not other filesystems mounted to descendant paths. The value of 'defined' only
# applies when an equality operation is used for searching because the path or
# filepath entity must explicitly define a file system.

# The default value is 'all' meaning to search all available file systems for
# data collection.

# Note that in most cases it is recommended that the value of 'local' be used to
# ensure that file system searching is limited to only the local file systems.
# Searching 'all' file systems may have performance implications.
@attribute(local_name='windows_view', enum=['32_bit', '64_bit'], default='64_bit')
# 64-bit versions of Windows provide an alternate file system and registry views
# to 32-bit applications. This behavior allows the OVAL Object to specify which
# view should be examined. This behavior only applies to 64-bit Windows, and
# must not be applied on other platforms.

# Note that the values have the following meaning: '64_bit' – Indicates that the
# 64-bit view on 64-bit Windows operating systems must be examined. On a 32-bit
# system, the Object must be evaluated without applying the behavior. '32_bit' –
# Indicates that the 32-bit view must be examined. On a 32-bit system, the
# Object must be evaluated without applying the behavior. It is recommended that
# the corresponding 'windows_view' entity be set on the OVAL Items that are
# collected when this behavior is used to distinguish between the OVAL Items
# that are collected in the 32-bit or 64-bit views.
class FileBehaviors(Model):
    pass
