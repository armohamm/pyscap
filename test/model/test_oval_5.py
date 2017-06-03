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
import pytest
import pkgutil

from scap.Model import Model

# import all the classes in the package
import scap.model.oval_5 as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')

logging.basicConfig(level=logging.DEBUG)

def test_DefinitionIdPattern_parse():
    assert DefinitionIdPattern().parse_value('oval:biz.jaymes:def:12346')

def test_ItemIdPattern_parse():
    assert ItemIdPattern().parse_value('12346')

def test_ObjectIdPattern_parse():
    assert ObjectIdPattern().parse_value('oval:biz.jaymes:obj:12346')

def test_SchemaVersionPattern_parse():
    assert SchemaVersionPattern().parse_value('0.1.2:3.4.5')

def test_StateIdPattern_parse():
    assert StateIdPattern().parse_value('oval:biz.jaymes:ste:12346')

def test_TestIdPattern_parse():
    assert TestIdPattern().parse_value('oval:biz.jaymes:tst:12346')

def test_VariableIdPattern_parse():
    assert VariableIdPattern().parse_value('oval:biz.jaymes:var:12346')
