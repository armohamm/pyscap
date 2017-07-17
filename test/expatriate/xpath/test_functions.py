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

# # Node Set Functions

# 'last': None,
# 'position': : None,
# 'count': None,
# 'id': None,
# 'local-name': None,
# 'namespace-uri': None,
# 'name': None,

# # String Functions

def test_string_int():
    assert doc.xpath('string(3)') == '3'

def test_string_float():
    assert doc.xpath('string(3.3)') == '3.3'

def test_string_bool():
    assert doc.xpath('string(true)') == 'true'

def test_string_str():
    assert doc.xpath('string("test")') == 'test'

def test_string_expr():
    assert doc.xpath('string(2+2)') == '4'

# TODO string() edge cases

def test_concat1():
    assert doc.xpath('concat("a")') == 'a'

def test_concat2():
    assert doc.xpath('concat("a", "b")') == 'ab'

def test_concat3():
    assert doc.xpath('concat("a", "b", "c")') == 'abc'

def test_starts_with1():
    assert doc.xpath('starts-with("a", "b")') == False

def test_starts_with2():
    assert doc.xpath('starts-with("apple", "a")') == True

def test_starts_with_empty():
    assert doc.xpath('starts-with("a", "")') == True

def test_contains1():
    assert doc.xpath('contains("apple", "a")') == True

def test_contains2():
    assert doc.xpath('contains("apple", "b")') == False

def test_contains_empty():
    assert doc.xpath('contains("a", "")') == True

def test_substring_before():
    assert doc.xpath('substring-before("1999/04/01","/")') == '1999'

def test_substring_before():
    assert doc.xpath('substring-after("1999/04/01","/")') == '04/01'

@pytest.mark.parametrize(
    "expr, result",
    (
        ('substring("12345",2,3)', '234'),
        ('substring("12345",2)', '2345'),
        ('substring("12345", 1.5, 2.6)', '234'),
        ('substring("12345", 0, 3)', '12'),
        ('substring("12345", 0 div 0, 3)', ''),
        ('substring("12345", 1, 0 div 0)', ''),
        ('substring("12345", -42, 1 div 0)', "12345"),
        ('substring("12345", -1 div 0, 1 div 0)', ""),
    )
)
def test_substring(expr, result):
    assert doc.xpath(expr) == result

@pytest.mark.parametrize(
    "expr, result",
    (
        ('string-length("12345")', 5),
        ('string-length("")', 0),
    )
)
def test_string_length(expr, result):
    assert doc.xpath(expr) == result

@pytest.mark.parametrize(
    "expr, result",
    (
        ('normalize-space("  12345")', '12345'),
        ('normalize-space("12345  ")', '12345'),
        ('normalize-space("123  45")', '123 45'),
        ('normalize-space("123\x0A\x0A45")', '123 45'),
        ('normalize-space("123\x09\x0945")', '123 45'),
        ('normalize-space("123\x0D\x0D45")', '123 45'),
    )
)
def test_normalize_space(expr, result):
    assert doc.xpath(expr) == result

@pytest.mark.parametrize(
    "expr, result",
    (
        ('translate("bar","abc","ABC")', 'BAr'),
        ('translate("--aaa--","abc-","ABC")', 'AAA'),
        ('translate("--aaa--","abc","ABC-")', '--AAA--'),
    )
)
def test_translate(expr, result):
    assert doc.xpath(expr) == result

# # Boolean Functions

@pytest.mark.parametrize(
    "expr, result",
    (
        ('boolean(0)', False),
        ('boolean(1)', True),
        ('boolean(3)', True),
        # TODO nodeset
        ('boolean("")', False),
        ('boolean("test")', True),
        ('boolean(true)', True),
        ('boolean(false)', False),
    )
)
def test_boolean(expr, result):
    assert doc.xpath(expr) == result


@pytest.mark.parametrize(
    "expr, result",
    (
        ('not(true)', False),
        ('not(false)', True),
    )
)
def test_not(expr, result):
    assert doc.xpath(expr) == result

def test_true():
    assert doc.xpath('true()') == True

def test_false():
    assert doc.xpath('false()') == False

# TODO 'lang': None,

# # Number Functions

@pytest.mark.parametrize(
    "expr, result",
    (
        ('floor(1.1)', 1),
        ('floor(2.6)', 2),
    )
)
def test_floor(expr, result):
    assert doc.xpath(expr) == result

# 'sum': None,

@pytest.mark.parametrize(
    "expr, result",
    (
        ('ceiling(1.1)', 2),
        ('ceiling(2.6)', 3),
    )
)
def test_ceiling(expr, result):
    assert doc.xpath(expr) == result

@pytest.mark.parametrize(
    "expr, result",
    (
        ('number(1)', 1),
        ('number(2.6)', 2.6),
        ('number(true)', 1),
        ('number(false)', 0),
        ('number("3")', 3),
        ('number("3.1")', 3.1),
        ('number(concat("4", "2"))', 42),
    )
)
def test_number(expr, result):
    assert doc.xpath(expr) == result

@pytest.mark.parametrize(
    "expr, result",
    (
        ('round(1.5)', 2),
        ('round(2.6)', 3),
    )
)
def test_round(expr, result):
    assert doc.xpath(expr) == result
