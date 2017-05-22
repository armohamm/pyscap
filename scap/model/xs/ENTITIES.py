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

from scap.model.xs.AnySimpleType import AnySimpleType
from scap.model.xs.ENTITY import ENTITY

logger = logging.getLogger(__name__)
class ENTITIES(AnySimpleType):
    def parse_value(self, value):
        value = super(ENTITIES, self).parse_value(value)

        if len(value) < 1:
            raise ValueError('ENTITIES must contain at least 1 character')

        r = []
        for i in re.split(r'\s+', value):
            r.append(ENTITY().parse_value(i))

        return tuple(r)

    def produce_value(self, value):
        return ' '.join(value)
