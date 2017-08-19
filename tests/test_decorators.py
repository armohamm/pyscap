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

from scap.decorators import *

logging.basicConfig(level=logging.DEBUG)

def test_attribute():
    @model_attribute(None, 'local_name', type='type1')
    @model_attribute('http://jaymes.biz', 'xmlns_name', type='type2')
    class AttrClass(object):
        pass

    assert hasattr(AttrClass, '_model_attributes')

    assert (None, 'local_name') in AttrClass._model_attributes
    assert AttrClass._model_attributes[(None, 'local_name')]['type'] == 'type1'

    assert ('http://jaymes.biz', 'xmlns_name') in AttrClass._model_attributes
    assert AttrClass._model_attributes[('http://jaymes.biz', 'xmlns_name')]['type'] == 'type2'

def test_element():
    @model_element(None, 'local_name', type='type1')
    @model_element('http://jaymes.biz', 'xmlns_name', type='type2')
    class ElClass(object):
        pass

    assert hasattr(ElClass, '_model_element_definitions')

    assert (None, 'local_name') in ElClass._model_element_definitions
    assert ElClass._model_element_definitions[(None, 'local_name')]['type'] == 'type1'

    assert ('http://jaymes.biz', 'xmlns_name') in ElClass._model_element_definitions
    assert ElClass._model_element_definitions[('http://jaymes.biz', 'xmlns_name')]['type'] == 'type2'

    assert ElClass._model_element_order[0] == (None, 'local_name')
    assert ElClass._model_element_order[1] == ('http://jaymes.biz', 'xmlns_name')

def test_name_implicit_ns():
    @model_name(None, 'local_name')
    class NameClass(object):
        pass

    assert hasattr(NameClass, '_model_name')
    assert NameClass._model_name == (None, 'local_name')

def test_name_explicit_ns():
    @model_name('http://jaymes.biz', 'local_name')
    class NameClass(object):
        pass

    assert hasattr(NameClass, '_model_name')
    assert NameClass._model_name == ('http://jaymes.biz', 'local_name')
