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

from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class Date(AnySimpleType):
    def parse_value(self, value):
        m = re.match(r'(-?\d\d\d\d)-(\d\d)-(\d\d)((([-+])(\d\d):(\d\d))|Z)?', value)
        if m:
            year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if m.group(4) is None:
                # naive date
                return datetime.date(int(year), int(month), int(day))
            elif m.group(4) == 'Z':
                tz = datetime.timezone.utc
            else:
                if m.group(5) is not None:
                    sign, hours, minutes = m.groups(6), int(m.groups(7)), int(m.groups(8))
                    if sign == '-':
                        tz = datetime.timezone(- datetime.timedelta(hours=hours, minutes=minutes))
                    else:
                        tz = datetime.timezone(datetime.timedelta(hours=hours, minutes=minutes))
                else:
                    tz = datetime.timezone.utc

            return datetime.datetime(year, month, day, 0, 0, 0, 0, tz)
        else:
            raise ValueError('Unable to parse Date value')

    def produce_value(self, value):
        return value.strftime('%Y-%m-%d%z')
