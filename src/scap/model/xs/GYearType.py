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

from .AnySimpleType import AnySimpleType
from .SevenPropertyModel import SevenPropertyModel

logger = logging.getLogger(__name__)

class GYearType(AnySimpleType):
    def parse_value(self, value):
        m = re.fullmatch(r'-?([1-9][0-9]{3,}|0[0-9]{3})(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?', value)
        if not m:
            raise ValueError('xs:GYear must match -?([1-9][0-9]{3,}|0[0-9]{3})(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?')

        # fudge for python 3.5 compatibility w/match obj __getitem__
        m = list(m.groups())
        m.insert(0, None)

        return SevenPropertyModel(year=m[1], timezoneOffset=m[2])
