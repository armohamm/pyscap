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
import os
import pytest
import uuid

from scap.Host import Host
from scap.model.cpe_matching_2_3.CPE import CPE
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)

filename = os.path.expanduser('~/.pyscap/inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')
for col in host.detect_collectors({}):
    col.collect()

def test_collected_network_connections():
    assert 'network_connections' in host.facts
    assert isinstance(host.facts['network_connections'], dict)

    for dev, netcon in host.facts['network_connections'].items():
        assert isinstance(dev, str)
        for i in ['mac_address', 'default_route']:
            if i in netcon:
                assert isinstance(netcon[i], str)

        assert 'network_addresses' in netcon
        assert isinstance(netcon['network_addresses'], list)
        for netadd in netcon['network_addresses']:
            for i in ['type', 'address', 'subnet_mask']:
                assert i in netadd
                assert isinstance(netadd[i], str)
