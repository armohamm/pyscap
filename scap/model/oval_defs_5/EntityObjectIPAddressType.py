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

from scap.model.oval_common_5 import *
from scap.model.oval_defs_5 import *
from scap.model.oval_defs_5.EntitySimpleBaseType import EntitySimpleBaseType
from scap.model.xs.String import String

logger = logging.getLogger(__name__)
class EntityObjectIPAddressType(EntitySimpleBaseType, String):
    MODEL_MAP = {
        'attributes': {
            'datatype': {'enum': ['ipv4_address', 'ipv6_address'], 'required': True},
        }
    }
