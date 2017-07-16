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
doc.parse('''<?xml version='1.0' encoding='utf-8'?>
<Root xmlns="http://jaymes.biz">
    <Element id="element1">
    </Element>
    <Element id="element2"/>
    <Element id="element3">
        <SubEl id="subel1">
            <KalEl id="kalel1">
                Superman's dad
            </KalEl>
        </SubEl>
    </Element>
</Root>
''')

@pytest.mark.parametrize(
    "expr, tokens",
    (
        ('"test"', ['"test"']),
        ('"test test\t test\n test"', ['"test test\t test\n test"']),
        ('3', ['3']),
        ('42', ['42']),
        ('true', ['true']),
        ('true or false', ['true', 'or', 'false']),
        ('5 mod 2', ['5', 'mod', '2']),
        ('-5 mod -2', ['-', '5', 'mod', '-', '2']),
        ('child::para', ['child', '::', 'para']),
        ('child::*', ['child', '::', '*']),
        ('child::text()', ['child', '::', 'text', '(', ')']),
        ('child::para[@id]', ['child', '::', 'para', '[', '@', 'id', ']']),
        ('descendant-or-self::para[@id]', ['descendant-or-self', '::', 'para', '[', '@', 'id', ']']),
        ('child::*/child::para', ['child', '::', '*', '/', 'child', '::', 'para']),
        ('/descendant::para', ['/', 'descendant', '::', 'para']),
        ('child::para[position()=1]', ['child', '::', 'para', '[', 'position', '(', ')', '=', '1', ']']),
        ('child::para[position()>1]', ['child', '::', 'para', '[', 'position', '(', ')', '>', '1', ']']),
        ('child::para[attribute::type="warning"]', ['child', '::', 'para', '[', 'attribute', '::', 'type', '=', '"warning"', ']']),
        ('para', ['para']),
        ('*', ['*']),
        ('@name', ['@', 'name']),
        ('*/para', ['*', '/', 'para']),
        ('/doc/chapter[5]/section[2]', ['/', 'doc', '/', 'chapter', '[', '5', ']', '/', 'section', '[', '2', ']']),
        ('employee[@secretary and @assistant]', ['employee', '[', '@', 'secretary', 'and', '@', 'assistant', ']']),
        ('$test', ['$test']),
    )
)
def test_tokenization(expr, tokens):
    assert doc._tokenize(expr) == tokens

def test_string_literal():
    assert doc.xpath('"test"') == 'test'

def test_string_literal_ws():
    assert doc.xpath('"test test\t test\n test"') == 'test test\t test\n test'

def test_number_literal():
    assert doc.xpath('3') == 3

def test_number_literal2():
    assert doc.xpath('42') == 42

def test_number_literal3():
    assert doc.xpath('4.2') == 4.2

def test_true():
    assert doc.xpath('true') == True

def test_false():
    assert doc.xpath('false') == False

def test_op_mult():
    assert doc.xpath('2 * 4') == 8

def test_op_add():
    assert doc.xpath('2 + 4') == 6

def test_op_sub1():
    assert doc.xpath('2 - 4') == -2

def test_op_sub2():
    assert doc.xpath('4 - 2') == 2

def test_op_eq():
    assert doc.xpath('4 = 4') == True

def test_op_eq2():
    assert doc.xpath('4 = 2') == False

def test_op_ne():
    assert doc.xpath('4 != 4') == False

def test_op_ne2():
    assert doc.xpath('4 != 2') == True

def test_op_lt():
    assert doc.xpath('4 < 4') == False

def test_op_lt2():
    assert doc.xpath('2 < 4') == True

def test_op_le():
    assert doc.xpath('4 <= 3') == False

def test_op_le2():
    assert doc.xpath('2 <= 4') == True

def test_op_gt():
    assert doc.xpath('4 > 5') == False

def test_op_gt2():
    assert doc.xpath('4 > 2') == True

def test_op_ge():
    assert doc.xpath('4 >= 5') == False

def test_op_ge2():
    assert doc.xpath('5 >= 4') == True

def test_op_and():
    assert doc.xpath('true and true') == True

def test_op_and2():
    assert doc.xpath('true and false') == False

def test_op_or():
    assert doc.xpath('true or false') == True

def test_op_or2():
    assert doc.xpath('false or false') == False

def test_op_mod0():
    assert doc.xpath('5 mod 2') == 1

def test_op_mod1():
    assert doc.xpath('5 mod -2') == 1

def test_op_mod2():
    assert doc.xpath('-5 mod 2') == -1

def test_op_mod3():
    assert doc.xpath('-5 mod -2') == -1

def test_op_div0():
    assert doc.xpath('5 div 2') == 2

def test_op_negate():
    assert doc.xpath('-42') == -42

def test_subexpr():
    assert doc.xpath('(2+3)+2') == 7

# def test_and_presides_or():
#     pytest.fail()
#
# def test_equality_presides_and():
#     pytest.fail()
#
# def test_comparison_presides_equality():
#     pytest.fail()
#
# def test_left_association():
#     assert doc.xpath('3 > 2 > 1') == doc.xpath('(3 > 2) > 1')
#
# def test_context_node():
#     assert doc.xpath('.') == doc
#
# def test_context_node():
#     assert doc.root_element.xpath('..') == doc
#
# def test_predicate():
#     assert doc.xpath('.[@id="element1"]') == doc.root_element.children[0]
