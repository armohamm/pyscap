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
from scap.model.xs.IntegerType import IntegerType

logger = logging.getLogger(__name__)

@attribute(local_name='max_depth', type=IntegerType, default=-1)
@attribute(local_name='recurse', enum=['none', 'files', 'directories', 'files and directories', 'symlinks', 'symlinks and directories'], default='symlinks and directories')
@attribute(local_name='recurse_direction', enum=['none', 'up', 'down'], default='none')
@attribute(local_name='recurse_file_system', enum=['all', 'local', 'defined'], default='all')
class FileBehaviors(Model):
    pass
