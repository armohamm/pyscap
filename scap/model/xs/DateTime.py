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

import re
import datetime
import logging

from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class DateTime(AnySimpleType):
    def parse_value(self, value):
        m = re.match(r'(-?\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(\.(\s+))?((([-+])(\d\d):(\d\d))|Z)?', value)
        if m:
            year, month, day, hour, minute, second = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6))
            if m.group(7) is not None and m.group(8) is not None:
                microsecond = int(m.group(8))
            else:
                microsecond = 0

            if m.group(9) is None:
                # naive
                return datetime.datetime(year, month, day, hour, minute, second, microsecond)
            elif m.group(9) == 'Z':
                tz = datetime.timezone.utc
            else:
                if m.group(10) is not None:
                    sign, hours, minutes = m.groups(11), int(m.group(12)), int(m.group(13))
                    if sign == '-':
                        tz = datetime.timezone(- datetime.timedelta(hours=hours, minutes=minutes))
                    else:
                        tz = datetime.timezone(datetime.timedelta(hours=hours, minutes=minutes))
                else:
                    tz = datetime.timezone.utc

            return datetime.datetime(year, month, day, hour, minute, second, microsecond, tz)
        else:
            raise ValueError('Unable to parse DateTime value')

    def produce_value(self, value):
        return value.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
