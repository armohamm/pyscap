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

def test_string():
    assert doc.xpath('"test"') == 'test'

def test_string_ws():
    assert doc.xpath('"test test\t test\n test"') == 'test test\t test\n test'

def test_number():
    assert doc.xpath('3') == 3

def test_number2():
    assert doc.xpath('42') == 42

def test_number3():
    assert doc.xpath('4.2') == 4.2

def test_true():
    assert doc.xpath('true') == True

def test_false():
    assert doc.xpath('false') == False
