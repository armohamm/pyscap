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

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

hash_params = [
    # Need separate test for linux & windows because line ending difference changes the hashes
    ('linux', 'MD5', '088c92cb4d6c96cc3981678e4355fa4a'),
    ('linux', 'SHA-1', '8d1f3a9fe1fdef59204dbbbe163e1098c49d142b'),
    ('linux', 'SHA-224', '05dfa237b19462f5042625fd6301c03aa31b7ab23ec1ab990fd0aac6'),
    ('linux', 'SHA-256', '2eb5d6d679443b74e168948cba53f689572d7b0fabf4052016cd71241cb31356'),
    ('linux', 'SHA-384', '220d7a9e4035522342bda46f02dc9c0fd2dc20a9ad97cc005ff973f5f56c3461bedaffd506bd363593730102d8bf384c'),
    ('linux', 'SHA-512', '9e50035cb3b290015ce44dbd4152ee3dc506677b98329129c1440144fa1da591e1d77a3522ee780d5390391431ebee4336eb4ddaa1af20adfef07aacf71b65f8'),
    ('windows', 'MD5', '64383C3236AA3F8E8416C2D284A6C368'),
    ('windows', 'SHA-1', '703884F0C787F3A287815FE4A793F71591671894'),
    #('windows', 'SHA-224', ''), # not supported by powershell
    ('windows', 'SHA-256', '09617D45A40CB8CC577C73996D4723513F6C04E68D8AE6B0F1F25B3F34178748'),
    ('windows', 'SHA-384', '0EDEAB27A4C3008F80DADBE116997CADAA47A6327C3E9CC420578CA843D904E089E7A83D5701CE80DD0B5CE1237322E0'),
    ('windows', 'SHA-512', '5055CE3D494D4E003EA8F875E50BAC35AA4EFF13AEBADA45FC295763E2386FE007EC901F968D6D64BBA5DE1B3A17904E11ADDDE470A36DA018DCD660475FF2B7'),
]

@pytest.mark.parametrize("oval_family, hash_type, hash_value", hash_params)
def test_hash(oval_family, hash_type, hash_value):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    c = host.load_collector('FileHashCollector', {'type': hash_type, 'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml')})
    assert c.collect() == hash_value

def test_not_exists():
    c = host.load_collector('FileHashCollector', {'type': 'MD5', 'path': str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'nope.xml')})
    with pytest.raises(FileNotFoundError):
        c.collect()

def test_args():
    with pytest.raises(ArgumentException):
        host.load_collector('FileHashCollector', {})
    with pytest.raises(ArgumentException):
        host.load_collector('FileHashCollector', {'path': None})
    with pytest.raises(ArgumentException):
        host.load_collector('FileHashCollector', {'type': None})
