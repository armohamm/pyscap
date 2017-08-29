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
from scap.model.xs.AnyUriType import AnyUriType
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='type', enum=['simple', 'extended', 'locator', 'arc', 'resource', 'title', 'none'])
@attribute(local_name='href', type=AnyUriType)
@attribute(local_name='role', type=AnyUriType) # min length = 1
@attribute(local_name='arcrole', type=AnyUriType) # min length = 1
@attribute(local_name='title', type=StringType)
@attribute(local_name='show', enum=['new', 'replace', 'embed', 'other', 'none'])
@attribute(local_name='actuate', enum=['onLoad', 'onRequest', 'other', 'none'])
@attribute(local_name='label', type=NCNameType)
@attribute(local_name='from', type=NCNameType)
@attribute(local_name='to', type=NCNameType)
class Base(Model):
    pass
