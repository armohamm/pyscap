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

def test_context_node():
    assert doc.xpath('.') == doc

# def test_context_node():
#     assert doc.root_element.xpath('..') == doc
#
# def test_predicate():
#     assert doc.xpath('.[@id="element1"]') == doc.root_element.children[0]
