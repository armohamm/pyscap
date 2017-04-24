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

import pytest, logging
from scap.Model import Model, UnsupportedNamespaceException
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.DEBUG)

def test_parse_tag():
    assert Model.parse_tag('{http://www.w3.org/XML/1998/namespace}test') == ('http://www.w3.org/XML/1998/namespace', 'test')
    assert Model.parse_tag('test') == (None, 'test')

    with pytest.raises(UnsupportedNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')

def test_get_namespace():
    from scap.model.xml_cat_1_1.Catalog import Catalog
    m = Catalog()
    assert m.get_namespace() == 'xml_cat_1_1'

def test_namespace_to_xmlns():
    assert Model.namespace_to_xmlns('xml_cat_1_1') == 'urn:oasis:names:tc:entity:xmlns:xml:catalog'

def test_xmlns_to_namespace():
    assert Model.xmlns_to_namespace('urn:oasis:names:tc:entity:xmlns:xml:catalog') == 'xml_cat_1_1'

def test_map_tag_to_module_name():
    assert Model.map_tag_to_module_name('xml_cat_1_1', '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog') == 'Catalog'

def test_load_root_class():
    from scap.model.xml_cat_1_1.Catalog import Catalog

    cat1 = Model.load(None, ET.fromstring('''<cat:catalog xmlns:cat="urn:oasis:names:tc:entity:xmlns:xml:catalog">
        <cat:uri name="name1" uri="uri1"/>
        <cat:uri name="name2" uri="uri2"/>
        <cat:uri name="name3" uri="uri3"/>
    </cat:catalog>'''))

    assert isinstance(cat1, Catalog)
    assert 'name1' in cat1.entries

def test_load_enclosed_class():
    from scap.model.xccdf_1_1.BenchmarkType import BenchmarkType
    benchmark = BenchmarkType()

    status = Model.load(benchmark, ET.fromstring('<xccdf:status xmlns:xccdf="http://checklists.nist.gov/xccdf/1.1" date="2010-01-21"/>'))

    from scap.model.xccdf_1_1.StatusElement import StatusElement
    assert isinstance(status, StatusElement)

    import datetime
    assert status.date == datetime.date(2010, 1, 21)
