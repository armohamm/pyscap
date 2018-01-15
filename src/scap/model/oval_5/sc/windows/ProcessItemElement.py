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

from expatriate.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

@element(local_name='command_line', max=1, min=0, cls=EntityItemType)
@element(local_name='pid', max=1, min=0, cls=EntityItemType)
@element(local_name='ppid', max=1, min=0, cls=EntityItemType)
@element(local_name='priority', max=1, min=0, cls=EntityItemType)
@element(local_name='image_path', max=1, min=0, cls=EntityItemType)
@element(local_name='current_dir', max=1, min=0, cls=EntityItemType)
@element(local_name='creation_time', max=1, min=0, cls=EntityItemType)
@element(local_name='dep_enabled', max=1, min=0, cls=EntityItemType)
@element(local_name='primary_window_text', max=1, min=0, cls=EntityItemType)
@element(local_name='name', max=1, min=0, cls=EntityItemType)
class ProcessItemElement(ItemType):
    pass
