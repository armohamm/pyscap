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

from expatriate.CharacterData import CharacterData
from expatriate.Document import Document
from expatriate.Element import Element

logging.basicConfig(level=logging.DEBUG)

def test_empty_doc():
    doc = Document()
    doc.parse('''<Document></Document>''')
    assert len(doc.children) == 1
    assert isinstance(doc.children[0], Element)
    assert len(doc.children[0].children) == 0

def test_whitespace():
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
