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
import pytest
import pkgutil
import sys
import xml.etree.ElementTree as ET

from scap.Host import Host
from scap.Inventory import Inventory
from scap.Model import Model

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
    items = host.collect_oval_items(obj, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FamilyItemElement)
    assert items[0].family.text == 'linux'

@pytest.mark.skipif(sys.platform != 'win32', reason="does not apply")
def test_family_windows():
    obj = FamilyObjectElement()
    items = host.collect_oval_items(obj, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FamilyItemElement)
    assert items[0].family.text == 'windows'

# def test_filehash58():
#     obj = FileHash58ObjectElement()
#     obj.
#     items = host.collect_oval_items(obj, None, {}, [])
#     assert len(items) == 1
#     assert isinstance(items[0], FamilyItemElement)
#
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
