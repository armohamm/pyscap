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
import logging
import xml.etree.ElementTree as ET
import types
import importlib
import sys

from scap.Model import Model, UnregisteredNamespaceException
from scap.model.test.RootFixture import RootFixture
from scap.model.test.EnclosedFixture import EnclosedFixture
from scap.model.test.AttributeFixture import AttributeFixture
from scap.model.test.WildcardElementNotInFixture import WildcardElementNotInFixture
from scap.model.test.WildcardElementInFixture import WildcardElementInFixture
from scap.model.test2.EnclosedFixture import EnclosedFixture as EnclosedFixture2

logging.basicConfig(level=logging.DEBUG)
Model.register_namespace('scap.model.test', 'http://jaymes.biz/test')
Model.register_namespace('scap.model.test2', 'http://jaymes.biz/test2')

def test_parse_tag():
    assert Model.parse_tag('{http://jaymes.biz/test}test') == ('http://jaymes.biz/test', 'test')
    assert Model.parse_tag('test') == (None, 'test')

    with pytest.raises(UnregisteredNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')

def test_package_to_xmlns():
    assert Model.package_to_xmlns('scap.model.test') == 'http://jaymes.biz/test'
    assert Model.package_to_xmlns('scap.model.test2') == 'http://jaymes.biz/test2'

def test_xmlns_to_package():
    assert Model.xmlns_to_package('http://jaymes.biz/test') == 'scap.model.test'
    assert Model.xmlns_to_package('http://jaymes.biz/test2') == 'scap.model.test2'

def test_map_tag_to_module_name():
    assert Model.map_tag_to_module_name('scap.model.test', '{http://jaymes.biz/test}RootFixture') == 'RootFixture'

def test_load_root_model():
    root = Model.load(None, ET.fromstring('<test:RootFixture xmlns:test="http://jaymes.biz/test" />'))

    assert isinstance(root, RootFixture)

def test_load_enclosed_model():
    root = RootFixture()
    enc = Model.load(root, ET.fromstring('<test:EnclosedFixture xmlns:test="http://jaymes.biz/test" />'))

    assert isinstance(enc, EnclosedFixture)

def test_init_value():
    root = RootFixture(value='test')
    assert root.text == 'test'

def test_init_tag_name():
    root = RootFixture(tag_name='test')
    assert root.to_xml().tag == '{http://jaymes.biz/test}test'

def test_init_attribute_in():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" in_attribute="test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'in_test')
    assert attr.in_test == 'test'

def test_init_attribute_dash():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" dash-attribute="test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'dash_attribute')
    assert attr.dash_attribute == 'test'

def test_init_attribute_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'default_attribute')
    assert attr.default_attribute == 'test'

def test_init_attribute_no_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'in_test')
    assert attr.in_test is None

def test_init_element_wildcard_not_in():
    el = Model.load(None, ET.fromstring('''
        <test:WildcardElementNotInFixture xmlns:test2="http://jaymes.biz/test2" xmlns:test="http://jaymes.biz/test">
        <test:wildcard_element>test1</test:wildcard_element>
        <test2:wildcard_element>test2</test2:wildcard_element>
        </test:WildcardElementNotInFixture>
        '''))
    assert isinstance(el, WildcardElementNotInFixture)
    assert hasattr(el, '_elements')
    assert isinstance(el._elements, list)
    assert len(el._elements) == 2
    assert isinstance(el._elements[0], EnclosedFixture)
    assert isinstance(el._elements[1], EnclosedFixture2)
    assert el._elements[0].text == 'test1'
    assert el._elements[1].text == 'test2'

def test_init_element_wildcard_in():
    el = Model.load(None, ET.fromstring('''
        <test:WildcardElementInFixture xmlns:test2="http://jaymes.biz/test2" xmlns:test="http://jaymes.biz/test">
        <test:wildcard_element>test1</test:wildcard_element>
        <test2:wildcard_element>test2</test2:wildcard_element>
        </test:WildcardElementInFixture>
        '''))
    assert isinstance(el, WildcardElementInFixture)

    assert hasattr(el, 'test_elements')
    assert isinstance(el.test_elements, list)
    assert len(el.test_elements) == 1

    assert hasattr(el, 'elements')
    assert isinstance(el.elements, list)
    assert len(el.elements) == 1

    assert isinstance(el.test_elements[0], EnclosedFixture)
    assert el.test_elements[0].text == 'test1'

    assert isinstance(el.elements[0], EnclosedFixture2)
    assert el.elements[0].text == 'test2'

def test_init_element_xmlns_wildcard():
    # TODO in
    # TODO not in
    # TODO initialized []
    pass

def test_init_element_append():
    # TODO initialized
    pass

def test_init_element_map():
    # TODO initialized {}
    pass

def test_init_element_wildcard():
    # TODO in
    # TODO not in
    # TODO initialized None
    pass

def test_str_id_func():
    root = RootFixture()
    assert str(root) == ('RootFixture # ' + str(id(root)))

def test_str_id():
    root = RootFixture()
    root.id = 'test'
    assert str(root) == ('RootFixture id: test')

def test_str_Id():
    root = RootFixture()
    root.Id = 'test'
    assert str(root) == ('RootFixture Id: test')

def test_str_name():
    root = RootFixture()
    root.name = 'test'
    assert str(root) == ('RootFixture name: test')

def test_get_package():
    root = RootFixture()
    assert root.get_package() == 'scap.model.test'

def test_get_tag_name_implicit():
    root = RootFixture()
    assert root.get_tag_name() == 'RootFixture'

def test_get_tag_name_explicit():
    root = RootFixture()
    root.tag_name = 'test'
    assert root.get_tag_name() == 'test'

def test_find_reference():
    root = RootFixture()
    root.id = 'test'
    assert root.id == Model.find_reference('test').id
