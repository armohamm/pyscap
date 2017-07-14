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
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 0

def test_xmlns_default_def():
    doc = Document()
    doc.parse('''<Document xmlns="http://jaymes.biz/test"></Document>''')
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 0
    assert len(doc.root_element.attributes) == 1
    assert 'xmlns' in doc.root_element.attributes
    assert doc.root_element.attributes['xmlns'] == 'http://jaymes.biz/test'
    assert len(doc.root_element.namespaces) == 1

def test_xmlns_prefix_def():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"></Document>''')
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 0
    assert len(doc.root_element.attributes) == 1
    assert 'xmlns:test2' in doc.root_element.attributes
    assert doc.root_element.attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.root_element.namespaces) == 1

def test_xmlns_prefix_element():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"><test2:Element/></Document>''')
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 1
    assert len(doc.root_element.attributes) == 1
    assert 'xmlns:test2' in doc.root_element.attributes
    assert doc.root_element.attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.root_element.namespaces) == 1

def test_xmlns_prefix_attribute():
    doc = Document()
    doc.parse('''<Document xmlns:test2="http://jaymes.biz/test2"><test2:Element test2:attribute="test"/></Document>''')
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.attributes) == 1
    assert 'xmlns:test2' in doc.root_element.attributes
    assert doc.root_element.attributes['xmlns:test2'] == 'http://jaymes.biz/test2'
    assert len(doc.root_element.namespaces) == 1
    assert len(doc.root_element.children) == 1
    assert len(doc.root_element.children[0].attributes) == 1
    assert 'test2:attribute' in doc.root_element.children[0].attributes
    assert doc.root_element.children[0].attributes['test2:attribute'] == 'test'

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
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 1
    assert isinstance(doc.root_element.children[0], CharacterData)

def test_skip_whitespace():
    doc = Document()
    doc.parse('''<Document>
</Document>''')
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 0

def test_parse_xml_decl_version_1_0():
    doc = Document()
    doc.parse(b"""<?xml version='1.0'?><author></author>""")
    assert doc.version == 1.0
    assert doc.encoding == None
    assert doc.standalone == None

def test_parse_xml_decl_version_1_1():
    doc = Document()
    doc.parse(b"""<?xml version='1.1'?><author></author>""")
    assert doc.version == 1.1
    assert doc.encoding == None
    assert doc.standalone == None

def test_encoding_iso_8859_1():
    doc = Document()
    doc.parse(b"""<?xml version='1.0' encoding='iso-8859-1'?><author><name>fredrik lundh</name><city>link\xF6ping</city></author>""")
    assert isinstance(doc.root_element, Element)
    el = doc.root_element
    assert len(el.children) == 2
    assert isinstance(el.children[0], Element)

    el = doc.root_element.children[0]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'name'
    assert el.children[0].data == "fredrik lundh"

    el = doc.root_element.children[1]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'city'
    assert el.children[0].data == "linköping"

def test_encoding_utf8():
    doc = Document()
    doc.parse(b"""<?xml version='1.0' encoding='UTF-8'?><author><name>fredrik lundh</name><city>link\xC3\xB6ping</city></author>""")
    assert isinstance(doc.root_element, Element)
    el = doc.root_element
    assert len(el.children) == 2
    assert isinstance(el.children[0], Element)

    el = doc.root_element.children[0]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'name'
    assert el.children[0].data == "fredrik lundh"

    el = doc.root_element.children[1]
    assert len(el.children) == 1
    assert isinstance(el.children[0], CharacterData)
    assert el.name == 'city'
    assert el.children[0].data == "linköping"

def test_namespaces():
    doc = Document()
    doc.parse('''<Document xmlns="http://jaymes.biz/" xmlns:test="http://jaymes.biz/test"><test2:Element xmlns:test2="http://jaymes.biz/test2"/></Document>''')
    assert len(doc.namespaces) == 4
    assert 'xml' in doc.namespaces
    assert None in doc.namespaces
    assert 'test' in doc.namespaces
    assert 'test2' in doc.namespaces

def test_whitespace_preservation():
    doc = Document()
    doc.parse('''<Document><Element xml:space="preserve">
test
  test
</Element></Document>''')
    assert len(doc.root_element.children) == 1
    assert doc.root_element.children[0].name == 'Element'
    assert len(doc.root_element.children[0].children) == 5
    i = 0
    assert isinstance(doc.root_element.children[0].children[i], CharacterData)
    assert doc.root_element.children[0].children[i].data == '\n'

    i += 1
    assert isinstance(doc.root_element.children[0].children[i], CharacterData)
    assert doc.root_element.children[0].children[i].data == 'test'

    i += 1
    assert isinstance(doc.root_element.children[0].children[i], CharacterData)
    assert doc.root_element.children[0].children[i].data == '\n'

    i += 1
    assert isinstance(doc.root_element.children[0].children[i], CharacterData)
    assert doc.root_element.children[0].children[i].data == '  test'

    i += 1
    assert isinstance(doc.root_element.children[0].children[i], CharacterData)
    assert doc.root_element.children[0].children[i].data == '\n'

def test_namespace_resolve():
    doc = Document()
    doc.parse('''
    <Level0 xmlns="http://jaymes.biz/">
        <test:Level1 xmlns:test="http://jaymes.biz/test">
            <test2:Level2 xmlns:test2="http://jaymes.biz/test2">
            </test2:Level2>
        </test:Level1>
    </Level0>''')

    assert len(doc.namespaces) == 4
    assert isinstance(doc.root_element, Element)
    assert len(doc.root_element.children) == 1
    assert isinstance(doc.root_element.children[0], Element)
    assert len(doc.root_element.children[0].children) == 1
    assert isinstance(doc.root_element.children[0].children[0], Element)
    assert doc.root_element.children[0].children[0].resolve_namespace(None) == "http://jaymes.biz/"

def test_produce_elements():
    doc = Document()
    doc.parse('''
    <Level0 xmlns="http://jaymes.biz/">
        <test:Level1 xmlns:test="http://jaymes.biz/test">
            <test2:Level2 xmlns:test2="http://jaymes.biz/test2">
            </test2:Level2>
        </test:Level1>
    </Level0>''')

    assert doc.produce() == b'<?xml version="1.0" encoding="UTF-8"><Level0 xmlns="http://jaymes.biz/"><test:Level1 xmlns:test="http://jaymes.biz/test"><test2:Level2 xmlns:test2="http://jaymes.biz/test2"/></test:Level1></Level0>'

def test_produce_cdata():
    doc = Document()
    doc.parse('''
    <Document>
        <![CDATA[test]]>
    </Document>''')

    assert doc.produce() == b'<?xml version="1.0" encoding="UTF-8"><Document><![CDATA[test]]></Document>'

def test_produce_char_data():
    doc = Document()
    doc.parse('''
    <Document>
        test
    </Document>''')

    assert doc.produce() == b'<?xml version="1.0" encoding="UTF-8"><Document>test</Document>'

def test_produce_pi():
    doc = Document()
    doc.parse('''
    <Document>
        <?target data?>
    </Document>''')

    assert doc.produce() == b'<?xml version="1.0" encoding="UTF-8"><Document><?target data?></Document>'

def test_produce_comment():
    doc = Document()
    doc.parse('''
    <Document>
        <!-- comment data -->
    </Document>''')

    assert doc.produce() == b'<?xml version="1.0" encoding="UTF-8"><Document><!-- comment data --></Document>'
