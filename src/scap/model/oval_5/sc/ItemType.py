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

from .. import EXISTENCE_RESULT_ENUMERATION
from ..MessageType import MessageType
from ..ItemIdPattern import ItemIdPattern

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=ItemIdPattern, required=True)
@attribute(local_name='status', enum=EXISTENCE_RESULT_ENUMERATION, default='exists')
@element(local_name='message', list='messages', cls=MessageType, min=0, max=50)
class ItemType(Model):
    __last_item_id = 0

    def __init__(self, obj, item_args, *args, **kwargs):
        super(ItemType, self).__init__(*args, **kwargs)

        self._generating_object = obj

        ItemType.__last_item_id += 1
        self.id = ItemType.__last_item_id
