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

from scap.Collector import ArgumentException
from scap.Host import Host
from scap.model.cpe_matching_2_3.CPE import CPE
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG)

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

def test_exists():
    c = host.load_collector('DirectoryContentsCollector', {'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'scap')})
    entries = c.collect()
    assert isinstance(entries, list)
    assert len(entries) >= 11
    for e in entries:
        assert 'type' in e
        assert 'name' in e
        assert e['name'] in [
            '__pycache__',
            'collector',
            'host',
            'model',
            'reporter',
            '__init__.py',
            '__init__.pyc',
            'Collector.py',
            'Collector.pyc',
            'ColorFormatter.py',
            'ColorFormatter.pyc',
            'Host.py',
            'Host.pyc',
            'Inventory.py',
            'Inventory.pyc',
            'Model.py',
            'Model.pyc',
            'Reporter.py',
            'Reporter.pyc',
        ]

def test_not_exists():
    with pytest.raises(FileNotFoundError):
        host.load_collector('DirectoryContentsCollector', {'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'nope')}).collect()

# TODO test empty == []

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('DirectoryContentsCollector', {})
