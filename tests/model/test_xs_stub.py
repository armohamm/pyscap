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
import pathlib
import pkgutil

import expatriate
# import all the classes in the package
import expatriate.model.xs as pkg
import pytest
from expatriate.model.Model import Model

for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

logging.basicConfig(level=logging.DEBUG)

def test_parse_xsd():
    path = pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xs_stub.xsd'
    doc = expatriate.Document()
    doc.parse_file(str(path))
    model = Model.load(None, doc.root_element)

# TODO test stub functions; writes a file
