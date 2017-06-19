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

import importlib
import logging
import os
import pathlib
import pytest
import pkgutil
import sys
import xml.etree.ElementTree as ET

from scap.Host import Host
from scap.Inventory import Inventory
from scap.Model import Model
from scap.model.oval_5.defs.EntityObjectStringType import EntityObjectStringType
from scap.model.oval_5.defs.independent.EntityObjectHashTypeType import EntityObjectHashTypeType

# import all the classes in the package
import scap.model.oval_5.sc.independent as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass
import scap.model.oval_5.defs.independent as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval_5.sc', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5')
Model.register_namespace('scap.model.oval_5.sc.independent', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent')
Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

filename = os.path.expanduser('~/.pyscap/inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')
for collector in host.detect_collectors({}):
    collector.collect()

@pytest.mark.skipif(sys.platform != 'linux', reason="does not apply")
def test_family_linux():
    obj = FamilyObjectElement()
    items = obj.collect_items(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FamilyItemElement)
    assert items[0].family.text == 'linux'

@pytest.mark.skipif(sys.platform != 'win32', reason="does not apply")
def test_family_windows():
    obj = FamilyObjectElement()
    items = obj.collect_items(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FamilyItemElement)
    assert items[0].family.text == 'windows'

@pytest.mark.parametrize(
    "hash_type,hash_value",
    [
        ('MD5', '088c92cb4d6c96cc3981678e4355fa4a'),
        ('SHA-1', '8d1f3a9fe1fdef59204dbbbe163e1098c49d142b'),
        ('SHA-224', '05dfa237b19462f5042625fd6301c03aa31b7ab23ec1ab990fd0aac6'),
        ('SHA-256', '2eb5d6d679443b74e168948cba53f689572d7b0fabf4052016cd71241cb31356'),
        ('SHA-384', '220d7a9e4035522342bda46f02dc9c0fd2dc20a9ad97cc005ff973f5f56c3461bedaffd506bd363593730102d8bf384c'),
        ('SHA-512', '9e50035cb3b290015ce44dbd4152ee3dc506677b98329129c1440144fa1da591e1d77a3522ee780d5390391431ebee4336eb4ddaa1af20adfef07aacf71b65f8'),
    ]
)
def test_filehash58_filepath(hash_type, hash_value):
    obj = FileHash58ObjectElement()
    obj.filepath = EntityObjectStringType(value=str(pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model' / 'test_xlink.xml'))

    obj.hash_type = EntityObjectHashTypeType(value=hash_type)
    items = obj.collect_items(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FileHash58ItemElement)
    assert items[0].status == 'exists'
    assert items[0].hash_type.text == hash_type
    assert items[0].hash.text == hash_value

# def test_filehash():
#     pass
#
# def test_ldap57():
#     pass
#
# def test_ldap():
#     pass
#
# def test_sql57():
#     pass
#
# def test_sql():
#     pass
#
# def test_textfilecontent():
#     pass
#
# def test_variable():
#     pass
#
# def test_xmlfilecontent():
#     pass
