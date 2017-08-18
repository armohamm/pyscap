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
import pathlib
import pytest
import uuid

from scap.collector.exceptions import *
from scap.Host import Host
from scap.model.cpe_matching_2_3.CPE import CPE
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

def test_exists():
    c = host.load_collector('FileExistsCollector', {'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml')})
    assert c.collect() == True

def test_exists_ci():
    c = host.load_collector('FileExistsCollector', {'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'TEST_XLINK.xml'), 'case_insensitive': True})
    assert c.collect() == True

def test_not_exists():
    c = host.load_collector('FileExistsCollector', {'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'nope.xml')})
    assert c.collect() == False

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('FileExistsCollector', {})
