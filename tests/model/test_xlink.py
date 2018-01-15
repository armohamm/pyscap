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
import pathlib

import expatriate
import pytest
import scap.model.xlink
from expatriate.model.Model import Model
from fixtures.test.EnclosedFixture import EnclosedFixture
from fixtures.test.RootFixture import RootFixture
from scap.Inventory import Inventory

logging.basicConfig(level=logging.DEBUG)
Model.register_namespace('scap.model.xlink', 'http://www.w3.org/1999/xlink')

def test_simple_local():
    path = (
        pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml'
    ).as_posix()
    if not path.startswith('/'):
        path = '/' + path
    test_xml = '<test:XLinkFixture ' \
        + 'xmlns:test="http://jaymes.biz/test" ' \
        + 'xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" ' \
        + 'xlink:href="file://' + path + '" />'
    doc = expatriate.Document()
    doc.parse(test_xml)
    model = Model.load(None, doc.root_element)
    assert isinstance(model._elements, list)
    assert len(model._elements) > 0
    assert isinstance(model._elements[0], RootFixture)
    assert isinstance(model._elements[0].EnclosedFixture, EnclosedFixture)

def test_simple_remote():
    test_xml = '<test:XLinkFixture ' +
        'xmlns:test="http://jaymes.biz/test" ' +
        'xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" ' +
        'xlink:href="http://jaymes.biz/test.xml" />'
    doc = expatriate.Document()
    doc.parse(test_xml)
    model = Model.load(None, doc.root_element)
    assert isinstance(model._elements, list)
    assert len(model._elements) > 0
    assert isinstance(model._elements[0], RootFixture)
    assert isinstance(model._elements[0].EnclosedFixture, EnclosedFixture)
