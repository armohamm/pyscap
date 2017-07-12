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
import pytest

from expatriate import *

logging.basicConfig(level=logging.DEBUG)

def test_empty_doc():
    doc = Document()
    doc.parse('''<Document></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 0

def test_xmlns_default_def():
    doc = Document()
    doc.parse('''<Document xmlns="http://jaymes.biz/test"></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 0
    assert len(doc.children[0].attributes) == 1
    assert 'xmlns' in doc.children[0].attributes
    assert doc.children[0].attributes['xmlns'] == 'http://jaymes.biz/test'
    assert len(doc.children[0].namespaces) == 1

def test_xmlns_prefix_def():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 0
    assert len(doc.children[0].attributes) == 1
    assert 'xmlns:test2' in doc.children[0].attributes
    assert doc.children[0].attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.children[0].namespaces) == 1

def test_xmlns_prefix_element():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"><test2:Element/></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 1
    assert len(doc.children[0].attributes) == 1
    assert 'xmlns:test2' in doc.children[0].attributes
    assert doc.children[0].attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.children[0].namespaces) == 1

def test_xmlns_prefix_attribute():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"><test2:Element test2:attribute="test"/></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].attributes) == 1
    assert 'xmlns:test2' in doc.children[0].attributes
    assert doc.children[0].attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.children[0].namespaces) == 1
    assert len(doc.children[0].children) == 1
    assert len(doc.children[0].children[0].attributes) == 1
    assert 'test2:attribute' in doc.children[0].children[0].attributes
    assert doc.children[0].children[0].attributes['test2:attribute'] == 'test'

def test_xmlns_prefix_element_unknown():
    doc = Document()
    with pytest.raises(UnknownNamespaceException):
        doc.parse('''<Document><test:Element/></Document>''')

def test_xmlns_prefix_attribute_unknown():
    doc = Document()
    with pytest.raises(UnknownNamespaceException):
        doc.parse('''<Document><Element test:attribute="test"/></Document>''')

def test_xmlns_prefix_duplicate():
    doc = Document()
    with pytest.raises(DuplicateNamespaceException):
        doc.parse('''<Document xmlns:test="http://jaymes.biz/test"><Element xmlns:test="http://jaymes.biz/test2"/></Document>''')

def test_not_skip_whitespace():
    doc = Document(skip_whitespace=False)
    doc.parse('''<Document>
</Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 1
    assert isinstance(doc.children[0].children[0], CharacterData)

def test_skip_whitespace():
    doc = Document()
    doc.parse('''<Document>
</Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 0

def test_encoding_iso_8859_1():
    doc = Document()
    doc.parse(b"""<?xml version='1.0' encoding='iso-8859-1'?><author><name>fredrik lundh</name><city>link\xF6ping</city></author>""")
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    el = doc.children[0]
    assert len(el.children) == 2
    assert isinstance(el.children[0], Element)

    el = doc.children[0].children[0]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'name'
    assert el.children[0].data == "fredrik lundh"

    el = doc.children[0].children[1]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'city'
    assert el.children[0].data == "linköping"

def test_encoding_utf8():
    doc = Document()
    doc.parse(b"""<?xml version='1.0' encoding='UTF-8'?><author><name>fredrik lundh</name><city>link\xC3\xB6ping</city></author>""")
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    el = doc.children[0]
    assert len(el.children) == 2
    assert isinstance(el.children[0], Element)

    el = doc.children[0].children[0]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'name'
    assert el.children[0].data == "fredrik lundh"

    el = doc.children[0].children[1]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'city'
    assert el.children[0].data == "linköping"

def test_namespaces():
    doc = Document()
    doc.parse('''<Document xmlns="http://jaymes.biz/" xmlns:test="http://jaymes.biz/test"><test2:Element xmlns:test2="http://jaymes.biz/test2"/></Document>''')
    assert len(doc.namespaces) == 3
    assert None in doc.namespaces
    assert 'test' in doc.namespaces
    assert 'test2' in doc.namespaces
