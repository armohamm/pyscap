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

import pytest
import xml.etree.ElementTree as ET

from scap.model.test.RootFixture import RootFixture
from scap.model.test.EnclosedFixture import EnclosedFixture
from scap.Model import Model
from scap.Inventory import Inventory
#from scap.LocalFileAdapter import LocalFileAdapter

Model.register_namespace('scap.model.xlink', 'http://www.w3.org/1999/xlink')

#requests.session().mount('file://', LocalFileAdapter())

def test_simple_local():
    model = Model.load(None, ET.fromstring('<test:XLinkFixture ' +
        'xmlns:test="http://jaymes.biz/test" ' +
        'xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" ' +
        'xlink:href="file://' + str(pytest.config.rootdir) + '/test/test.xml" />'))
    assert isinstance(model._elements, list)
    assert len(model._elements) > 0
    assert isinstance(model._elements[0], RootFixture)
    assert isinstance(model._elements[0].EnclosedFixture, EnclosedFixture)

def test_simple_remote():
    model = Model.load(None, ET.fromstring('<test:XLinkFixture ' +
        'xmlns:test="http://jaymes.biz/test" ' +
        'xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" ' +
        'xlink:href="http://jaymes.biz/test.xml" />'))
    assert isinstance(model._elements, list)
    assert len(model._elements) > 0
    assert isinstance(model._elements[0], RootFixture)
    assert isinstance(model._elements[0].EnclosedFixture, EnclosedFixture)
