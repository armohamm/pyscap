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

from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

from .EntityItemGconfTypeType import EntityItemGconfTypeType

logger = logging.getLogger(__name__)

@element(local_name='key', min=0, cls=EntityItemType, max=1)
@element(local_name='source', min=0, cls=EntityItemType, nillable=True, max=1)
@element(local_name='type', min=0, cls=EntityItemGconfTypeType, max=1)
@element(local_name='is_writable', min=0, cls=EntityItemType, max=1)
@element(local_name='mod_user', min=0, cls=EntityItemType, max=1)
@element(local_name='mod_time', min=0, cls=EntityItemType, max=1)
@element(local_name='is_default', min=0, cls=EntityItemType, max=1)
@element(local_name='value', list='values', min=0, cls=EntityItemType, max=None)
class GconfItemElement(ItemType):
    pass
