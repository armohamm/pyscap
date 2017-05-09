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
from scap.Model import Model
from scap.model.xml_cat_1_1.Catalog import Catalog
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.DEBUG)
Model.register_namespace('scap.model.xml_cat_1_1', 'urn:oasis:names:tc:entity:xmlns:xml:catalog')

cat1 = Model.load(None, ET.fromstring('''<xml_cat_1_1:catalog xmlns:xml_cat_1_1="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <xml_cat_1_1:uri name="name1" uri="uri1"/>
    <xml_cat_1_1:uri name="name2" uri="uri2"/>
    <xml_cat_1_1:uri name="name3" uri="uri3"/>
</xml_cat_1_1:catalog>'''))

def test_parsed():
    assert 'name1' in cat1.entries
    assert 'name2' in cat1.entries
    assert 'name2' in cat1.entries
    assert cat1.entries['name1'] == 'uri1'
    assert cat1.entries['name2'] == 'uri2'
    assert cat1.entries['name3'] == 'uri3'
    assert 'name4' not in cat1.entries

def test_dict():
    assert 'name1' in cat1
    assert 'name2' in cat1
    assert 'name2' in cat1
    assert cat1['name1'] == 'uri1'
    assert cat1['name2'] == 'uri2'
    assert cat1['name3'] == 'uri3'
    assert 'name4' not in cat1

cat2 = Catalog()
cat2['n1'] = 'u1'
cat2['n2'] = 'u2'

def test_to_xml():
    xml = ET.tostring(cat2.to_xml())
    print(xml)
    assert xml == b'<xml_cat_1_1:catalog xmlns:xml_cat_1_1="urn:oasis:names:tc:entity:xmlns:xml:catalog"><xml_cat_1_1:uri name="n1" uri="u1" /><xml_cat_1_1:uri name="n2" uri="u2" /></xml_cat_1_1:catalog>'
