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

import datetime
import logging
import re

from scap.model.xs.SevenPropertyModel import SevenPropertyModel
from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class Date(AnySimpleType):
    def parse_value(self, value):
        m = re.fullmatch(r'(-?\d\d\d\d)-(\d\d)-(\d\d)((([-+])(\d\d):(\d\d))|Z)?', value)
        if not m:
            raise ValueError('Unable to parse Date value')

        return SevenPropertyModel(year=m[1], month=m[2], day=m[3], timezoneOffset=m[4])
