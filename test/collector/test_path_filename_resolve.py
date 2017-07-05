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

@pytest.mark.parametrize(
    'path, filename, results, path_operation, filename_operation, max_depth, recurse, recurse_direction, recurse_file_system',
    [
        (
            str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
            'test_xlink.xml',
            [filepath],
            'equals',
            'equals',
            -1,
            'symlinks and directories',
            'none',
            'all'
        ),
        (
            str(pytest.config.rootdir),
            'test_xlink.xml',
            [filepath],
            'equals',
            'equals',
            -1,
            'symlinks and directories',
            'down',
            'all'
        ),
        (
            str(pytest.config.rootdir),
            'test_xlink.xml',
            [],
            'equals',
            'equals',
            1,
            'symlinks and directories',
            'down',
            'all'
        ),
        (
            str(pytest.config.rootdir),
            'test_xlink.xml',
            [],
            'equals',
            'equals',
            2,
            'symlinks and directories',
            'down',
            'all'
        ),
        (
            str(pytest.config.rootdir),
            'test_xlink.xml',
            [filepath],
            'equals',
            'equals',
            3,
            'symlinks and directories',
            'down',
            'all'
        ),
        (
            str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
            '.*xlink.xml',
            [filepath],
            'equals',
            'pattern match',
            -1,
            'symlinks and directories',
            'down',
            'all'
        ),
        (
            str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model'),
            '.*xlink.xml',
            [filepath],
            'equals',
            'pattern match',
            -1,
            'symlinks and directories',
            'down',
            'defined'
        )
    ]
)
def test_existing(path, filename, results, path_operation, filename_operation, max_depth, recurse, recurse_direction, recurse_file_system):
    c = host.load_collector('ResolvePathFilenameCollector', {
        'path': path,
        'filename': filename,
        'value_datatypes': {'path': 'string', 'filename': 'string'},
        'value_operations': {'path': path_operation, 'filename': filename_operation},
        'value_masks': {'path': False, 'filename': False},
        'behavior_max_depth': max_depth,
        'behavior_recurse': recurse,
        'behavior_recurse_direction': recurse_direction,
        'behavior_recurse_file_system': recurse_file_system,
        'behavior_windows_view': '64_bit',
    })
    assert c.collect() == results

# TODO recurse symlinks
# TODO path operation pattern match
# TODO recurse_direction up
# TODO recurse_file_system local, all
# TODO windows view

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('ResolvePathFilenameCollector', {})
