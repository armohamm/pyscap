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
<doc xmlns="http://jaymes.biz">
    <chapter name="ch1">
        <title>Figures</title>
        <figure name="fig01"/>
        <figure name="fig02"/>
        <figure name="fig03"/>
        <figure name="fig04"/>
        <figure name="fig05"/>
        <figure name="fig06"/>
        <figure name="fig07"/>
        <figure name="fig08"/>
        <figure name="fig09"/>
        <figure name="fig10"/>
        <figure name="fig11"/>
        <figure name="fig12"/>
        <figure name="fig13"/>
        <figure name="fig14"/>
        <figure name="fig15"/>
        <figure name="fig16"/>
        <figure name="fig17"/>
        <figure name="fig18"/>
        <figure name="fig19"/>
    </chapter>
    <chapter name="ch2">
        <title>Introduction</title>
        text node
        <div name="ch2_div1">
            <div name="ch2_div1_div2">
                <para name="ch2_div1_div2_p1" type="warning">Context para 1</para>
                <para name="ch2_div1_div2_p2">Context para 2</para>
                <para name="ch2_div1_div2_p3">Context para 3</para>
            </div>
            <para name="ch2_div1_p1">Context para 3</para>
            <figure name="fig20"/>
            <figure name="fig21"/>
            <figure name="fig22"/>
            <figure name="fig23"/>
            <figure name="fig24"/>
            <figure name="fig25"/>
            <figure name="fig26"/>
            <figure name="fig27"/>
            <figure name="fig28"/>
            <figure name="fig29"/>
        </div>
        <para name="ch2_p1">Context para 1</para>
        <para name="ch2_p2">Context para 2</para>
    </chapter>
    <chapter name="ch3">
        <title>Paras and Figures</title>
        <para name="ch3_p1" type="warning">Chapter para 1</para>
        <para name="ch3_p2" type="warning">Chapter para 2</para>
        <figure name="fig30"/>
        <figure name="fig31"/>
        <figure name="fig32"/>
        <figure name="fig33"/>
        <figure name="fig34"/>
        <figure name="fig35"/>
        <figure name="fig36"/>
        <figure name="fig37"/>
        <figure name="fig38"/>
        <figure name="fig39"/>
    </chapter>
    <chapter name="ch4">
        <title>Introduction</title>
        <para name="ch4_p1" type="warning">Chapter para 1</para>
        <para name="ch4_p2" type="warning">Chapter para 2</para>
        <olist name="ch4_ol1">
            <item name="ch4_ol1_i1">Item 1</item>
            <item name="ch4_ol1_i1">Item 2</item>
        </olist>
        <para name="ch4_p3" type="warning">Chapter para 3</para>
        <para name="ch4_p4" type="warning">Chapter para 4</para>
        <figure name="fig40"/>
        <figure name="fig41"/>
        <figure name="fig42"/>
    </chapter>
    <chapter name="ch5">
        <title>Summary</title>
        <section name="ch5_sec1">
        </section>
        <section name="ch5_sec2">
        </section>
    </chapter>
    <appendix name="a1">
        <title>Appendix 1</title>
        <employee secretary="Jane">John</employee>
        <employee>Jane</employee>
        <employee secretary="Charles" assistant="Cecil">Charleen</employee>
        <employee>Charles</employee>
        <employee assistant="Chuck">Cecil</employee>
    </appendix>
    <appendix name="a2">
    </appendix>
    <appendix name="a3">
    </appendix>
</doc>
''')

@pytest.mark.parametrize(
    "test, result",
    (
        (doc.root_element.children[1].xpath('child::para'), [
            doc.root_element.children[1].children[3],
            doc.root_element.children[1].children[4],
        ]),
        (doc.root_element.children[1].xpath('child::*'), [
            doc.root_element.children[1].children[0],
            doc.root_element.children[1].children[2],
            doc.root_element.children[1].children[3],
            doc.root_element.children[1].children[4],
        ]),
        (doc.root_element.children[1].xpath('child::text()'), [
            doc.root_element.children[1].children[1],
        ]),
        (doc.root_element.children[1].xpath('child::node()'), [
            doc.root_element.children[1].children[0],
            doc.root_element.children[1].children[1],
            doc.root_element.children[1].children[2],
            doc.root_element.children[1].children[3],
            doc.root_element.children[1].children[4],
        ]),
    )
)
def test_xpath(test, result):
    assert test == result
