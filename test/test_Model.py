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
import sys

from scap.Model import Model, UnregisteredNamespaceException, \
    TagMappingException, RequiredAttributeException, MinimumElementException, \
    MaximumElementException, ReferenceException

from fixtures.test.RootFixture import RootFixture
from fixtures.test.EnclosedFixture import EnclosedFixture
from fixtures.test.AttributeFixture import AttributeFixture
from fixtures.test.RequiredAttributeFixture import RequiredAttributeFixture
from fixtures.test.WildcardElementNotInFixture import WildcardElementNotInFixture
from fixtures.test.WildcardElementInFixture import WildcardElementInFixture
from fixtures.test.AppendElementFixture import AppendElementFixture
from fixtures.test.MapElementFixture import MapElementFixture
from fixtures.test.MappableElementFixture import MappableElementFixture
from fixtures.test.InitFixture import InitFixture
from fixtures.test.MinMaxElementFixture import MinMaxElementFixture

from fixtures.test2.EnclosedFixture import EnclosedFixture as EnclosedFixture2

logging.basicConfig(level=logging.DEBUG)
Model.register_namespace('fixtures.test', 'http://jaymes.biz/test')
Model.register_namespace('fixtures.test2', 'http://jaymes.biz/test2')

def test_namespace_registration():
    Model.register_namespace('scap.model.derp', 'http://jaymes.biz/derp')

    Model.xmlns_to_package('http://jaymes.biz/derp') == 'scap.model.derp'

    Model.unregister_namespace('scap.model.derp')

    with pytest.raises(UnregisteredNamespaceException):
        Model.xmlns_to_package('http://jaymes.biz/derp')

def test_parse_tag():
    assert Model.parse_tag('{http://jaymes.biz/test}test') == ('http://jaymes.biz/test', 'test')
    assert Model.parse_tag('test') == (None, 'test')

    with pytest.raises(UnregisteredNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')

def test_package_to_xmlns():
    assert Model.package_to_xmlns('fixtures.test') == 'http://jaymes.biz/test'
    assert Model.package_to_xmlns('fixtures.test2') == 'http://jaymes.biz/test2'

    with pytest.raises(UnregisteredNamespaceException):
        Model.package_to_xmlns('scap.model.derp')

def test_xmlns_to_package():
    assert Model.xmlns_to_package('http://jaymes.biz/test') == 'fixtures.test'
    assert Model.xmlns_to_package('http://jaymes.biz/test2') == 'fixtures.test2'

    with pytest.raises(UnregisteredNamespaceException):
        Model.xmlns_to_package('http://jaymes.biz/derp')

def test_map_tag_to_module_name():
    assert Model.map_tag_to_module_name('fixtures.test', '{http://jaymes.biz/test}RootFixture') == 'RootFixture'

    with pytest.raises(ImportError):
        Model.map_tag_to_module_name('scap.model.derp', '{http://jaymes.biz/test}Derp')

    # TODO test missing TAG_MAP

    with pytest.raises(TagMappingException):
        Model.map_tag_to_module_name('fixtures.test', '{http://jaymes.biz/test}Derp')

def test_load_root_model():
    root = Model.load(None, ET.fromstring('<test:RootFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(root, RootFixture)

    with pytest.raises(UnregisteredNamespaceException):
        Model.load(None, ET.fromstring('<test:RootFixture xmlns:test="http://jaymes.biz/derp" />'))

    with pytest.raises(TagMappingException):
        Model.load(None, ET.fromstring('<test:Derp xmlns:test="http://jaymes.biz/test" />'))

def test_load_enclosed_model():
    root = RootFixture()
    el = Model.load(root, ET.fromstring('<test:EnclosedFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(el, EnclosedFixture)

    el = Model.load(root, ET.fromstring('<EnclosedFixture />'))
    assert isinstance(el, EnclosedFixture)

    with pytest.raises(UnregisteredNamespaceException):
        Model.load(root, ET.fromstring('<test:EnclosedFixture xmlns:test="http://jaymes.biz/derp" />'))
    with pytest.raises(UnregisteredNamespaceException):
        Model.load(None, ET.fromstring('<EnclosedFixture />'))
    with pytest.raises(TagMappingException):
        Model.load(root, ET.fromstring('<Derp />'))

def test_load_attribute_required():
    attr = Model.load(None, ET.fromstring('<test:RequiredAttributeFixture xmlns:test="http://jaymes.biz/test" required_attribute="test" />'))
    assert isinstance(attr, RequiredAttributeFixture)
    assert hasattr(attr, 'required_attribute')
    assert attr.required_attribute == 'test'

    with pytest.raises(RequiredAttributeException):
        attr = Model.load(None, ET.fromstring('<test:RequiredAttributeFixture xmlns:test="http://jaymes.biz/test" />'))

def test_load_attribute_in():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" in_attribute="test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'in_test')
    assert attr.in_test == 'test'

def test_load_attribute_dash():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" dash-attribute="test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'dash_attribute')
    assert attr.dash_attribute == 'test'

def test_load_attribute_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'default_attribute')
    assert attr.default_attribute == 'test'

def test_load_attribute_no_default():
    attr = Model.load(None, ET.fromstring('<test:AttributeFixture xmlns:test="http://jaymes.biz/test" />'))
    assert isinstance(attr, AttributeFixture)
    assert hasattr(attr, 'in_test')
    assert attr.in_test is None

def test_load_element_min():
    el = Model.load(None, ET.fromstring('''
        <test:MinMaxElementFixture xmlns:test="http://jaymes.biz/test">
        <test:min>test1</test:min>
        <test:min>test2</test:min>
        <test:min>test3</test:min>
        <test:max>test4</test:max>
        <test:max>test5</test:max>
        </test:MinMaxElementFixture>
        '''))
    assert isinstance(el, MinMaxElementFixture)

    assert hasattr(el, 'min')
    assert isinstance(el.min, list)
    assert len(el.min) == 3
    assert el.min[0].text == 'test1'
    assert el.min[1].text == 'test2'
    assert el.min[2].text == 'test3'

    assert hasattr(el, 'max')
    assert isinstance(el.max, list)
    assert len(el.max) == 2
    assert el.max[0].text == 'test4'
    assert el.max[1].text == 'test5'

    with pytest.raises(MinimumElementException):
        el = Model.load(None, ET.fromstring('''
            <test:MinMaxElementFixture xmlns:test="http://jaymes.biz/test">
            <test:min>test1</test:min>
            <test:max>test4</test:max>
            <test:max>test5</test:max>
            </test:MinMaxElementFixture>
            '''))

    with pytest.raises(MaximumElementException):
        el = Model.load(None, ET.fromstring('''
            <test:MinMaxElementFixture xmlns:test="http://jaymes.biz/test">
            <test:min>test1</test:min>
            <test:min>test2</test:min>
            <test:min>test3</test:min>
            <test:max>test4</test:max>
            <test:max>test5</test:max>
            <test:max>test6</test:max>
            </test:MinMaxElementFixture>
            '''))

def test_load_element_wildcard_not_in():
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

def test_load_element_wildcard_in():
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

def test_load_element_append_nil():
    el = Model.load(None, ET.fromstring('''
        <test:AppendElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:append_nil xsi:nil="true" />
        <test:append_nil>test2</test:append_nil>
        </test:AppendElementFixture>
        '''))

    assert isinstance(el, AppendElementFixture)

    assert hasattr(el, 'append_nil')
    assert isinstance(el.append_nil, list)
    assert len(el.append_nil) == 2

    assert el.append_nil[0] is None

    assert isinstance(el.append_nil[1], EnclosedFixture)
    assert el.append_nil[1].text == 'test2'

def test_load_element_append_type():
    el = Model.load(None, ET.fromstring('''
        <test:AppendElementFixture xmlns:test="http://jaymes.biz/test">
        <test:append_type>1.1</test:append_type>
        <test:append_type>1.2</test:append_type>
        </test:AppendElementFixture>
        '''))

    assert isinstance(el, AppendElementFixture)

    assert hasattr(el, 'append_type')
    assert isinstance(el.append_type, list)
    assert len(el.append_type) == 2

    assert isinstance(el.append_type[0], float)
    assert el.append_type[0] == 1.1

    assert isinstance(el.append_type[1], float)
    assert el.append_type[1] == 1.2

def test_load_element_append_class():
    el = Model.load(None, ET.fromstring('''
        <test:AppendElementFixture xmlns:test="http://jaymes.biz/test">
        <test:append_class>test1</test:append_class>
        <test:append_class>test2</test:append_class>
        </test:AppendElementFixture>
        '''))

    assert isinstance(el, AppendElementFixture)

    assert hasattr(el, 'append_class')
    assert isinstance(el.append_class, list)
    assert len(el.append_class) == 2

    assert isinstance(el.append_class[0], EnclosedFixture)
    assert el.append_class[0].text == 'test1'

    assert isinstance(el.append_class[1], EnclosedFixture)
    assert el.append_class[1].text == 'test2'

def test_load_element_map_key_explicit():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_explicit_key key="test1">test1</test:map_explicit_key>
        <test:map_explicit_key key="test2">test2</test:map_explicit_key>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_explicit_key')
    assert len(el.map_explicit_key) == 2

    assert 'test1' in el.map_explicit_key
    assert el.map_explicit_key['test1'] == 'test1'

    assert 'test2' in el.map_explicit_key
    assert el.map_explicit_key['test2'] == 'test2'

def test_load_element_map_key_implicit():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_implicit_key id="test1">test1</test:map_implicit_key>
        <test:map_implicit_key id="test2">test2</test:map_implicit_key>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_implicit_key')
    assert len(el.map_implicit_key) == 2

    assert 'test1' in el.map_implicit_key
    assert el.map_implicit_key['test1'] == 'test1'

    assert 'test2' in el.map_implicit_key
    assert el.map_implicit_key['test2'] == 'test2'

def test_load_element_map_value_nil():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_value_nil id="test1" xsi:nil="true"/>
        <test:map_value_nil id="test2">test2</test:map_value_nil>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_value_nil')
    assert len(el.map_value_nil) == 2

    assert 'test1' in el.map_value_nil
    assert el.map_value_nil['test1'] == None

    assert 'test2' in el.map_value_nil
    assert el.map_value_nil['test2'] == 'test2'

def test_load_element_map_value_attr():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_value_attr id="test1" value="test1"/>
        <test:map_value_attr id="test2" value="test2"/>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_value_attr')
    assert len(el.map_value_attr) == 2

    assert 'test1' in el.map_value_attr
    assert el.map_value_attr['test1'] == 'test1'

    assert 'test2' in el.map_value_attr
    assert el.map_value_attr['test2'] == 'test2'

def test_load_element_map_value_type():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_value_type id="test1">test1</test:map_value_type>
        <test:map_value_type id="test2">test2</test:map_value_type>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_value_type')
    assert len(el.map_value_type) == 2

    assert 'test1' in el.map_value_type
    assert el.map_value_type['test1'] == 'test1'

    assert 'test2' in el.map_value_type
    assert el.map_value_type['test2'] == 'test2'

def test_load_element_map_value_class():
    el = Model.load(None, ET.fromstring('''
        <test:MapElementFixture xmlns:test="http://jaymes.biz/test" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <test:map_value_class id="test1" tag="blue">text1</test:map_value_class>
        <test:map_value_class id="test2" tag="red">text2</test:map_value_class>
        </test:MapElementFixture>
        '''))

    assert isinstance(el, MapElementFixture)

    assert hasattr(el, 'map_value_class')
    assert len(el.map_value_class) == 2

    assert 'test1' in el.map_value_class
    assert isinstance(el.map_value_class['test1'], MappableElementFixture)
    assert el.map_value_class['test1'].id == 'test1'
    assert el.map_value_class['test1'].tag == 'blue'
    assert el.map_value_class['test1'].text == 'text1'

    assert 'test2' in el.map_value_class
    assert isinstance(el.map_value_class['test2'], MappableElementFixture)
    assert el.map_value_class['test2'].id == 'test2'
    assert el.map_value_class['test2'].tag == 'red'
    assert el.map_value_class['test2'].text == 'text2'

def test_init_value():
    root = RootFixture(value='test')
    assert root.text == 'test'

def test_init_tag_name():
    root = RootFixture(tag_name='test')
    assert root.to_xml().tag == '{http://jaymes.biz/test}test'

def test_initialization():
    init = InitFixture()

    assert isinstance(init, InitFixture)
    assert hasattr(init, 'attr')
    assert init.attr is None

    assert not hasattr(init, 'in_attr')
    assert hasattr(init, 'test_attr')
    assert init.test_attr is None

    assert hasattr(init, 'dash_attr')
    assert init.dash_attr is None

    assert hasattr(init, 'default_attr')
    assert init.default_attr == 'Default'

    assert hasattr(init, 'list_')
    assert isinstance(init.list_, list)
    assert len(init.list_) == 0

    assert hasattr(init, 'dict_')
    assert isinstance(init.dict_, dict)
    assert len(init.dict_.keys()) == 0

    assert not hasattr(init, 'in_test')
    assert hasattr(init, 'test_in')
    assert init.test_in is None

    assert hasattr(init, 'dash_test')
    assert init.dash_test is None

    assert hasattr(init, 'test2_elements')
    assert isinstance(init.test2_elements, list)
    assert len(init.test2_elements) == 0

    assert hasattr(init, '_elements')
    assert isinstance(init._elements, list)
    assert len(init._elements) == 0

def test_get_package():
    root = RootFixture()
    assert root.get_package() == 'fixtures.test'

def test_str_id_func():
    root = RootFixture()
    assert str(root) == ('fixtures.test.RootFixture.RootFixture # ' + str(id(root)))

def test_str_id():
    root = RootFixture()
    root.id = 'test'
    assert str(root) == ('fixtures.test.RootFixture.RootFixture id: test')

def test_str_Id():
    root = RootFixture()
    root.Id = 'test'
    assert str(root) == ('fixtures.test.RootFixture.RootFixture Id: test')

def test_str_name():
    root = RootFixture()
    root.name = 'test'
    assert str(root) == ('fixtures.test.RootFixture.RootFixture name: test')

def test_references():
    root = RootFixture()
    enc = EnclosedFixture()
    enc.parent = root
    enc.id = 'reftest1'
    assert root.find_reference('reftest1') == enc

    with pytest.raises(ReferenceException):
        root.find_reference('test1')

def test_get_tag_name_implicit():
    root = RootFixture()
    assert root.get_tag_name() == 'RootFixture'

def test_get_tag_name_explicit():
    root = RootFixture()
    root.tag_name = 'test'
    assert root.get_tag_name() == 'test'

def test_get_xmlns():
    root = RootFixture()
    assert root.get_xmlns() == 'http://jaymes.biz/test'

# NOTE: from_xml is tested via Model.load

def test_to_xml_root_enclosed():
    el = RootFixture()
    el.EnclosedFixture = EnclosedFixture()
    assert ET.tostring(el.to_xml()) == \
        b'<test:RootFixture xmlns:test="http://jaymes.biz/test"><test:EnclosedFixture /></test:RootFixture>'

def test_to_xml_required_attribute():
    el = RequiredAttributeFixture()
    with pytest.raises(RequiredAttributeException):
        el.to_xml()
    el.required_attribute = 'test'
    assert ET.tostring(el.to_xml()) == \
        b'<test:RequiredAttributeFixture xmlns:test="http://jaymes.biz/test" required_attribute="test" />'

def test_to_xml_attributes():
    el = AttributeFixture()
    el.in_test = 'test'
    el.dash_attribute = 'test'
    el.default_attribute = 'not default'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:AttributeFixture xmlns:test="http://jaymes.biz/test"')
    assert b'dash-attribute="test" ' in xml
    assert b'default_attribute="not default" ' in xml
    assert b'in_attribute="test" ' in xml

    el.in_test = None
    xml = ET.tostring(el.to_xml())
    assert b'in_attribute=' not in xml

    el.default_attribute = 'test'
    xml = ET.tostring(el.to_xml())
    assert b'default_attribute="test" ' not in xml

def test_to_xml_min_max():
    el = MinMaxElementFixture()
    for i in range(0, 3):
        el.min.append(EnclosedFixture(tag_name='min'))
    for i in range(0, 2):
        el.max.append(EnclosedFixture(tag_name='max'))

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MinMaxElementFixture xmlns:test="http://jaymes.biz/test"')
    assert xml.count(b'<test:min') == 3
    assert xml.count(b'<test:max') == 2

    del el.min[0]
    with pytest.raises(MinimumElementException):
        el.to_xml()

    el.min.append(EnclosedFixture())
    el.max.append(EnclosedFixture())
    with pytest.raises(MaximumElementException):
        el.to_xml()

def test_to_xml_wildcard_not_in():
    el = WildcardElementNotInFixture()
    el._elements.append(EnclosedFixture(tag_name='wildcard_element'))
    el._elements.append(EnclosedFixture2(tag_name='wildcard_element'))

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:WildcardElementNotInFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'xmlns:test2="http://jaymes.biz/test2"' in xml
    assert b'<test:wildcard_element' in xml
    assert b'<test2:wildcard_element' in xml

def test_to_xml_wildcard_in():
    el = WildcardElementInFixture()
    el.test_elements.append(EnclosedFixture(tag_name='wildcard_element'))
    el.elements.append(EnclosedFixture2(tag_name='wildcard_element'))

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:WildcardElementInFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'xmlns:test2="http://jaymes.biz/test2"' in xml
    assert b'<test:wildcard_element' in xml
    assert b'<test2:wildcard_element' in xml

def test_to_xml_append_nil():
    el = AppendElementFixture()
    el.append_nil.append(None)
    el.append_nil.append(EnclosedFixture(value='test', tag_name='append_nil'))

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:AppendElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' in xml
    assert b'<test:append_nil xsi:nil="true" />' in xml
    assert b'<test:append_nil>test</test:append_nil>' in xml

def test_to_xml_append_type():
    el = AppendElementFixture()
    el.append_type.append(1.1)
    el.append_type.append(1.2)

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:AppendElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:append_type>1.1</test:append_type>' in xml
    assert b'<test:append_type>1.2</test:append_type>' in xml

def test_to_xml_append_class():
    el = AppendElementFixture()
    el.append_class.append(EnclosedFixture(value='test1', tag_name='append_class'))
    el.append_class.append(EnclosedFixture(value='test2', tag_name='append_class'))

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:AppendElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:append_class>test1</test:append_class>' in xml
    assert b'<test:append_class>test2</test:append_class>' in xml

def test_to_xml_map_key_explicit():
    el = MapElementFixture()
    el.map_explicit_key['test1'] = 'test1'
    el.map_explicit_key['test2'] = 'test2'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:map_explicit_key key="test1">test1</test:map_explicit_key>' in xml
    assert b'<test:map_explicit_key key="test2">test2</test:map_explicit_key>' in xml

def test_to_xml_map_key_implicit():
    el = MapElementFixture()
    el.map_implicit_key['test1'] = 'test1'
    el.map_implicit_key['test2'] = 'test2'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:map_implicit_key id="test1">test1</test:map_implicit_key>' in xml
    assert b'<test:map_implicit_key id="test2">test2</test:map_implicit_key>' in xml

def test_to_xml_map_value_nil():
    el = MapElementFixture()
    el.map_value_nil['test1'] = None
    el.map_value_nil['test2'] = 'test2'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' in xml
    assert b'<test:map_value_nil id="test1" xsi:nil="true" />' in xml
    assert b'<test:map_value_nil id="test2">test2</test:map_value_nil>' in xml

def test_to_xml_map_value_attr():
    el = MapElementFixture()
    el.map_value_attr['test1'] = 'test1'
    el.map_value_attr['test2'] = 'test2'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:map_value_attr id="test1" value="test1" />' in xml
    assert b'<test:map_value_attr id="test2" value="test2" />' in xml

def test_to_xml_map_value_type():
    el = MapElementFixture()
    el.map_value_type['test1'] = 'test1'
    el.map_value_type['test2'] = 'test2'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:map_value_type id="test1">test1</test:map_value_type>' in xml
    assert b'<test:map_value_type id="test2">test2</test:map_value_type>' in xml

def test_to_xml_map_value_class():
    el = MapElementFixture()
    el.map_value_class['test1'] = MappableElementFixture(value='text1', tag_name='map_value_class')
    el.map_value_class['test1'].tag = 'blue'
    el.map_value_class['test2'] = MappableElementFixture(value='text2', tag_name='map_value_class')
    el.map_value_class['test2'].tag = 'red'

    xml = ET.tostring(el.to_xml())
    assert xml.startswith(b'<test:MapElementFixture')
    assert b'xmlns:test="http://jaymes.biz/test"' in xml
    assert b'<test:map_value_class id="test1" tag="blue">text1</test:map_value_class>' in xml
    assert b'<test:map_value_class id="test2" tag="red">text2</test:map_value_class>' in xml
