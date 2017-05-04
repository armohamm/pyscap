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

import scap.model
from scap.Model import Model, UnregisteredNamespaceException

test_pkg = types.ModuleType('scap.model.test')
test_pkg.__package__ = scap.model
test_pkg.__path__ = scap.model.__path__
test_pkg.__path__ += 'test'
Model.register_namespace('test', 'http://jaymes.biz/test')
sys.modules['scap.model.test'] = test_pkg
test_pkg.TAG_MAP = {
    '{http://jaymes.biz/test}RootFixture': 'RootFixture',
    '{http://jaymes.biz/test}AttributeFixture': 'AttributeFixture',
}

test_mod = types.ModuleType('scap.model.test.RootFixture')
test_mod.__package__ = test_pkg
sys.modules['scap.model.test.RootFixture'] = test_mod
RootFixture = types.new_class('RootFixture', (Model,))
test_mod.RootFixture = RootFixture
RootFixture.__module__ = test_mod.__name__
RootFixture.MODEL_MAP = {
    'tag_name': 'RootFixture',
    'elements': [
        {'tag_name': 'EnclosedFixture', 'class': 'EnclosedFixture', 'min': 0},
    ],
}
sys.modules['scap.model.test.RootFixture.RootFixture'] = RootFixture

test_mod = types.ModuleType('scap.model.test.EnclosedFixture')
test_mod.__package__ = test_pkg
sys.modules['scap.model.test.EnclosedFixture'] = test_mod
EnclosedFixture = types.new_class('EnclosedFixture', (Model,))
test_mod.EnclosedFixture = EnclosedFixture
EnclosedFixture.__module__ = test_mod.__name__
EnclosedFixture.MODEL_MAP = {
}
sys.modules['scap.model.test.EnclosedFixture.EnclosedFixture'] = EnclosedFixture

test_mod = types.ModuleType('scap.model.test.AttributeFixture')
test_mod.__package__ = test_pkg
sys.modules['scap.model.test.AttributeFixture'] = test_mod
AttributeFixture = types.new_class('AttributeFixture', (Model,))
test_mod.AttributeFixture = AttributeFixture
AttributeFixture.__module__ = test_mod.__name__
AttributeFixture.MODEL_MAP = {
    'attributes': {
        'in_attribute': {'in': 'in_test'},
        'dash-attribute': {},
        'default_attribute': {'default': 'test'},
    },
}
sys.modules['scap.model.test.AttributeFixture.AttributeFixture'] = AttributeFixture

logging.basicConfig(level=logging.DEBUG)

def test_parse_tag():
    assert Model.parse_tag('{http://jaymes.biz/test}test') == ('http://jaymes.biz/test', 'test')
    assert Model.parse_tag('test') == (None, 'test')

    with pytest.raises(UnregisteredNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')

def test_get_namespace():
    f = RootFixture()
    assert f.get_namespace() == 'test'

def test_namespace_to_xmlns():
    assert Model.namespace_to_xmlns('test') == 'http://jaymes.biz/test'

def test_xmlns_to_namespace():
    assert Model.xmlns_to_namespace('http://jaymes.biz/test') == 'test'

def test_map_tag_to_module_name():
    assert Model.map_tag_to_module_name('test', '{http://jaymes.biz/test}RootFixture') == 'RootFixture'

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
    assert hasattr(attr, 'in_test')
    assert attr.in_test == 'test'

def test_init_attribute_dash():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" dash-attribute="test" />'))
    assert hasattr(attr, 'dash_attribute')
    assert attr.dash_attribute == 'test'

def test_init_attribute_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert hasattr(attr, 'default_attribute')
    assert attr.default_attribute == 'test'

def test_init_attribute_no_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert hasattr(attr, 'in_test')
    assert attr.in_test is None

def test_init_element_wildcard():
    # TODO in
    # TODO not in
    # TODO initialized []
    pass

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

def test_get_namespace():
    root = RootFixture()
    assert root.get_namespace() == 'test'

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
