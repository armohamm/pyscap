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

from .PostTownSuffixType import PostTownSuffixType
from .AddressLineType import AddressLineType

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='PostTownName', list='post_town_names', cls=defer_class_load('scap.model.xal_2_0.PostTownType', 'PostTownType'))
@element(local_name='PostTownSuffix', into='post_town_suffix', cls=PostTownSuffixType)
@element(local_name='*')
class PostTownType(Model):
    pass
