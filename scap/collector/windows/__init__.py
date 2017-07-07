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

def convert_file_time(t):
    t = t / 10 # convert to microseconds
    t = datetime.timedelta(microseconds=t)
    t = datetime.datetime(1601, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc) + t # 12:00 A.M. January 1, 1601 UTC
    return t

def convert_json_timestamp(t):
    t = t / 1000 # convert to seconds
    t = datetime.datetime.utcfromtimestamp(t)
    return t
