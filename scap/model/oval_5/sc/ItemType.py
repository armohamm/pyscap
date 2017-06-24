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
from scap.model.oval_5 import EXISTENCE_RESULT_ENUMERATION

logger = logging.getLogger(__name__)
class ItemType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'message', 'list': 'messages', 'class': 'scap.model.oval_5.MessageType', 'min': 0, 'max': 50},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.ItemIdPattern', 'required': True},
            'status': {'enum': EXISTENCE_RESULT_ENUMERATION, 'default': 'exists'},
        }
    }

    __last_item_id = 0

    def __init__(self, obj, args, result, value=None, xmlns=None, tag_name=None):
        super(ItemType, self).__init__(value=value, xmlns=xmlns, tag_name=tag_name)

        self._generating_object = obj

        ItemType.__last_item_id += 1
        self.id = ItemType.__last_item_id

        if 'status' in result:
            self.status = result['status']

        if 'messages' in result:
            for m in messages:
                msg = MessageType(value=m['message'])
                msg.level = m['level']
                self.messages.append(msg)

        self.process_result(args, result)

    def process_result(self, args, result):
        raise NotImplementedError(self.__class__.__name__ + ' does not define process_result')
