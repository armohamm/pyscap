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

import pytest

from scap.Host import Host
from scap.host.cli.LocalHost import LocalHost

def test_host_detection():
    host = Host.load('localhost')
    assert isinstance(host, LocalHost)

def test_load_collector():
    host = Host.load('localhost')
    detection_collectors = [
        'UniqueIdCollector',
        'CpeCollector',
        'FqdnCollector',
        'HostnameCollector',
        'NetworkConnectionCollector',
        'NetworkServiceCollector',
        'IdentityCollector',
    ]

    for col_name in detection_collectors:
        col = host.load_collector(col_name, {})
        # collection is tested elsewhere
        #col.collect()
