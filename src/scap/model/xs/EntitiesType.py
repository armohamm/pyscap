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
import re

from scap.model.decorators import *

from .EntityType import EntityType
from .List import List

logger = logging.getLogger(__name__)

class EntitiesType(List):
    def parse_item(self, item_value):
        return EntityType().parse_value(item_value)

    def produce_item(self, item_value):
        return EntityType().produce_value(item_value)
