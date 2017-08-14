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
logging.basicConfig(level=logging.DEBUG)

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

def test_existing_file_equals():
    filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml')
    c = host.load_collector('ResolveFilepathCollector', {
        'filepath': filepath,
        'value_datatypes': {'filepath': 'string'},
        'value_operations': {'filepath': 'equals'},
        'value_masks': {'filepath': False},
        'behavior_recurse_file_system': 'all',
    })
    assert c.collect() == [filepath]

def test_existing_file_pattern():
    regexfilepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / '.*xlink.xml').replace('\\', '\\\\')
    filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml')
    c = host.load_collector('ResolveFilepathCollector', {
        'filepath': regexfilepath,
        'value_datatypes': {'filepath': 'string'},
        'value_operations': {'filepath': 'pattern match'},
        'value_masks': {'filepath': False},
        'behavior_recurse_file_system': 'all',
    })
    assert c.collect() == [filepath]

def test_existing_dir_equals():
    filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model')
    c = host.load_collector('ResolveFilepathCollector', {
        'filepath': filepath,
        'value_datatypes': {'filepath': 'string'},
        'value_operations': {'filepath': 'equals'},
        'value_masks': {'filepath': False},
        'behavior_recurse_file_system': 'all',
    })
    assert c.collect() == [filepath]

# TODO existing dir pattern

def test_not_existing_file_equals():
    filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink2.xml')
    c = host.load_collector('ResolveFilepathCollector', {
        'filepath': filepath,
        'value_datatypes': {'filepath': 'string'},
        'value_operations': {'filepath': 'equals'},
        'value_masks': {'filepath': False},
        'behavior_recurse_file_system': 'all',
    })
    with pytest.raises(FileNotFoundError):
        c.collect()

def test_not_existing_file_pattern():
    filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink2.xml')
    regexfilepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / '.*xlink2.xml').replace('\\', '\\\\')
    c = host.load_collector('ResolveFilepathCollector', {
        'filepath': regexfilepath,
        'value_datatypes': {'filepath': 'string'},
        'value_operations': {'filepath': 'equals'},
        'value_masks': {'filepath': False},
        'behavior_recurse_file_system': 'all',
    })
    with pytest.raises(FileNotFoundError):
        c.collect()

# TODO not existing dir equals, pattern

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('ResolveFilepathCollector', {})
