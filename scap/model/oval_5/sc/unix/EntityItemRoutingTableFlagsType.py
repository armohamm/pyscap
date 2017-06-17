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

from scap.model.oval_5.sc.EntityItemStringType import EntityItemStringType

logger = logging.getLogger(__name__)
class EntityItemRoutingTableFlagsType(EntityItemStringType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enumeration(self):
        return [
            'UP',
            'GATEWAY',
            'HOST',
            'REINSTATE',
            'DYNAMIC',
            'MODIFIED',
            'ADDRCONF',
            'CACHE',
            'REJECT',
            'REDUNDANT',
            'SETSRC',
            'BROADCAST',
            'LOCAL',
            'PROTOCOL_1',
            'PROTOCOL_2',
            'PROTOCOL_3',
            'BLACK_HOLE',
            'CLONING',
            'PROTOCOL_CLONING',
            'INTERFACE_SCOPE',
            'LINK_LAYER',
            'MULTICAST',
            'STATIC',
            'WAS_CLONED',
            'XRESOLVE',
            'USABLE',
            'PINNED',
            'ACTIVE_DEAD_GATEWAY_DETECTION',
            '',
        ]

