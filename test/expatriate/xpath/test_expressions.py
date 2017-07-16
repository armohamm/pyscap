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

doc = Document()

def test_subexpr1():
    assert doc.xpath('(2)') == 2

def test_subexpr2():
    assert doc.xpath('(2+3)+2') == 7

def test_left_association():
    assert doc.xpath('3 > 2 > 1') == doc.xpath('(3 > 2) > 1')

def test_tuple2():
    assert doc.xpath('(2,3)') == (2,3)

def test_tuple3():
    assert doc.xpath('(2,3,4)') == (2,3,4)

def test_tuple_embedded_op():
    assert doc.xpath('(2+2,3,5)') == (4,3,5)

def test_tuple_embedded_sub1():
    assert doc.xpath('((2,3),5,4)') == ((2,3),5,4)

def test_tuple_embedded_sub2():
    assert doc.xpath('(3,4,(2,5))') == (3,4,(2,5))
