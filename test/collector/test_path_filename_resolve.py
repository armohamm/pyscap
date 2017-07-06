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

filepath = str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model' / 'test_xlink.xml')

def test_recurse_none():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'none',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_recurse_down():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pytest.config.rootdir),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_recurse_down_depth_1():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pytest.config.rootdir),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': 1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == []

def test_recurse_down_depth_2():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pytest.config.rootdir),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': 2,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == []

def test_recurse_down_depth_3():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pytest.config.rootdir),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': 3,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_filename_pattern_recurse_down():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
        'filename': '.*xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'pattern match'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_recurse_down_fs_defined():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'defined',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_recurse_down_fs_local():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'local',
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == [filepath]

def test_recurse_down_view_32():
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
        'filename': 'test_xlink.xml',
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': 'equals', 'filename': 'equals'},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': -1,
        'behavior_recurse': 'symlinks and directories',
        'behavior_recurse_direction': 'down',
        'behavior_recurse_file_system': 'all',
        'behavior_windows_view': '32_bit',
    })
    assert c.collect() == [filepath]

# TODO empty path
# TODO no matching files
# TODO recurse symlinks
# TODO path operation pattern match
# TODO recurse_direction up

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('ResolvePathFilenameCollector', {})
