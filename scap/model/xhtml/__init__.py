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

TAG_MAP = {
    '{http://www.w3.org/1999/xhtml}html': 'Html',
    '{http://www.w3.org/1999/xhtml}i': 'I',
    '{http://www.w3.org/1999/xhtml}p': 'P',
}

ATTRIBUTE_GROUP_coreattrs = {
    'id': {'type': 'ID'},
    'class': {'type': 'NMTokens'},
    'style': {'type': 'StyleSheet'},
    'title': {'type': 'Text'},
}

ATTRIBUTE_GROUP_i18n = {
    'lang': {'type': 'LanguageCode'},
    # xml:lang is defined in scap.model.Model
    'dir': {'enum': ['ltr', 'rtl']},
}

ATTRIBUTE_GROUP_events = {
    'onclick': {'type': 'Script'},
    'ondblclick': {'type': 'Script'},
    'onmousedown': {'type': 'Script'},
    'onmouseup': {'type': 'Script'},
    'onmouseover': {'type': 'Script'},
    'onmousemove': {'type': 'Script'},
    'onmouseout': {'type': 'Script'},
    'onkeypress': {'type': 'Script'},
    'onkeydown': {'type': 'Script'},
    'onkeyup': {'type': 'Script'},
}

ATTRIBUTE_GROUP_focus = {
    'accesskey': {'type': 'Character'},
    'tabindex': {'type': 'TabIndexNumber'},
    'onfocus': {'type': 'Script'},
    'onblur': {'type': 'Script'},
}

ATTRIBUTE_GROUP_attrs = {}
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_coreattrs)
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_i18n)
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_events)

ELEMENT_GROUP_special_pre = [
    {'tag_name': 'br'},
    {'tag_name': 'span'},
    {'tag_name': 'bdo'},
    {'tag_name': 'map'},
]

ELEMENT_GROUP_special = ELEMENT_GROUP_special_pre.copy()
ELEMENT_GROUP_special.extend([
    {'tag_name': 'object'},
    {'tag_name': 'img'},
])

ELEMENT_GROUP_fontstyle = [
    {'tag_name': 'tt'},
    {'tag_name': 'i'},
    {'tag_name': 'b'},
    {'tag_name': 'big'},
    {'tag_name': 'small'},
]

ELEMENT_GROUP_phrase = [
    {'tag_name': 'em'},
    {'tag_name': 'strong'},
    {'tag_name': 'dfn'},
    {'tag_name': 'code'},
    {'tag_name': 'q'},
    {'tag_name': 'samp'},
    {'tag_name': 'kbd'},
    {'tag_name': 'var'},
    {'tag_name': 'cite'},
    {'tag_name': 'abbr'},
    {'tag_name': 'acronym'},
    {'tag_name': 'sub'},
    {'tag_name': 'sup'},
]

ELEMENT_GROUP_inline_forms = [
    {'tag_name': 'input'},
    {'tag_name': 'select'},
    {'tag_name': 'textarea'},
    {'tag_name': 'label'},
    {'tag_name': 'button'},
]

ELEMENT_GROUP_misc_inline = [
    {'tag_name': 'ins'},
    {'tag_name': 'del'},
    {'tag_name': 'script'},
]

ELEMENT_GROUP_misc = [
    {'tag_name': 'noscript'},
]
ELEMENT_GROUP_misc.extend(ELEMENT_GROUP_misc_inline)

ELEMENT_GROUP_inline = [
    {'tag_name': 'a'},
]
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_special)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_fontstyle)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_phrase)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_inline_forms)
