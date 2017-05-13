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
    '{http://www.w3.org/1999/xhtml}html': 'HtmlTag',
    '{http://www.w3.org/1999/xhtml}i': 'ITag',
    '{http://www.w3.org/1999/xhtml}p': 'PTag',
}

ATTRIBUTE_GROUP_coreattrs = {
    'id': {'type': 'ID'},
    'class': {'type': 'NMTokens'},
    'style': {'type': 'StyleSheetType'},
    'title': {'type': 'TextType'},
}

ATTRIBUTE_GROUP_i18n = {
    'lang': {'type': 'LanguageCodeType'},
    # xml:lang is defined in scap.model.Model
    'dir': {'enum': ['ltr', 'rtl']},
}

ATTRIBUTE_GROUP_events = {
    'onclick': {'type': 'ScriptType'},
    'ondblclick': {'type': 'ScriptType'},
    'onmousedown': {'type': 'ScriptType'},
    'onmouseup': {'type': 'ScriptType'},
    'onmouseover': {'type': 'ScriptType'},
    'onmousemove': {'type': 'ScriptType'},
    'onmouseout': {'type': 'ScriptType'},
    'onkeypress': {'type': 'ScriptType'},
    'onkeydown': {'type': 'ScriptType'},
    'onkeyup': {'type': 'ScriptType'},
}

ATTRIBUTE_GROUP_focus = {
    'accesskey': {'type': 'CharacterType'},
    'tabindex': {'type': 'TabIndexNumberType'},
    'onfocus': {'type': 'ScriptType'},
    'onblur': {'type': 'ScriptType'},
}

ATTRIBUTE_GROUP_attrs = {}
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_coreattrs)
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_i18n)
ATTRIBUTE_GROUP_attrs.update(ATTRIBUTE_GROUP_events)

ELEMENT_GROUP_special_pre = [
    {'tag_name': 'br', 'list': '_elements', 'class': 'BrTag'},
    {'tag_name': 'span', 'list': '_elements', 'class': 'SpanTag'},
    {'tag_name': 'bdo', 'list': '_elements', 'class': 'BdoTag'},
    {'tag_name': 'map', 'list': '_elements', 'class': 'MapTag'},
]

ELEMENT_GROUP_special = ELEMENT_GROUP_special_pre.copy()
ELEMENT_GROUP_special.extend([
    {'tag_name': 'object', 'list': '_elements', 'class': 'ObjectTag'},
    {'tag_name': 'img', 'list': '_elements', 'class': 'ImgTag'},
])

ELEMENT_GROUP_fontstyle = [
    {'tag_name': 'tt', 'list': '_elements', 'class': 'TtTag'},
    {'tag_name': 'i', 'list': '_elements', 'class': 'ITag'},
    {'tag_name': 'b', 'list': '_elements', 'class': 'BTag'},
    {'tag_name': 'big', 'list': '_elements', 'class': 'BigTag'},
    {'tag_name': 'small', 'list': '_elements', 'class': 'SmallTag'},
]

ELEMENT_GROUP_phrase = [
    {'tag_name': 'em', 'list': '_elements', 'class': 'EmTag'},
    {'tag_name': 'strong', 'list': '_elements', 'class': 'StrongTag'},
    {'tag_name': 'dfn', 'list': '_elements', 'class': 'DfnTag'},
    {'tag_name': 'code', 'list': '_elements', 'class': 'CodeTag'},
    {'tag_name': 'q', 'list': '_elements', 'class': 'QTag'},
    {'tag_name': 'samp', 'list': '_elements', 'class': 'SampTag'},
    {'tag_name': 'kbd', 'list': '_elements', 'class': 'KbdTag'},
    {'tag_name': 'var', 'list': '_elements', 'class': 'VarTag'},
    {'tag_name': 'cite', 'list': '_elements', 'class': 'CiteTag'},
    {'tag_name': 'abbr', 'list': '_elements', 'class': 'AbbrTag'},
    {'tag_name': 'acronym', 'list': '_elements', 'class': 'AcronymTag'},
    {'tag_name': 'sub', 'list': '_elements', 'class': 'SubTag'},
    {'tag_name': 'sup', 'list': '_elements', 'class': 'SupTag'},
]

ELEMENT_GROUP_inline_forms = [
    {'tag_name': 'input', 'list': '_elements', 'class': 'InputTag'},
    {'tag_name': 'select', 'list': '_elements', 'class': 'SelectTag'},
    {'tag_name': 'textarea', 'list': '_elements', 'class': 'TextAreaTag'},
    {'tag_name': 'label', 'list': '_elements', 'class': 'LabelTag'},
    {'tag_name': 'button', 'list': '_elements', 'class': 'ButtonTag'},
]

ELEMENT_GROUP_misc_inline = [
    {'tag_name': 'ins', 'list': '_elements', 'class': 'InsTag'},
    {'tag_name': 'del', 'list': '_elements', 'class': 'DelTag'},
    {'tag_name': 'script', 'list': '_elements', 'class': 'ScriptTag'},
]

ELEMENT_GROUP_misc = [
    {'tag_name': 'noscript', 'list': '_elements', 'class': 'NoScriptTag'},
]
ELEMENT_GROUP_misc.extend(ELEMENT_GROUP_misc_inline)

ELEMENT_GROUP_inline = [
    {'tag_name': 'a', 'list': '_elements', 'class': 'ATag'},
]
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_special)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_fontstyle)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_phrase)
ELEMENT_GROUP_inline.extend(ELEMENT_GROUP_inline_forms)

ELEMENT_GROUP_heading = [
    {'tag_name': 'h1', 'list': '_elements', 'class': 'H1Tag'},
    {'tag_name': 'h2', 'list': '_elements', 'class': 'H2Tag'},
    {'tag_name': 'h3', 'list': '_elements', 'class': 'H3Tag'},
    {'tag_name': 'h4', 'list': '_elements', 'class': 'H4Tag'},
    {'tag_name': 'h5', 'list': '_elements', 'class': 'H5Tag'},
    {'tag_name': 'h6', 'list': '_elements', 'class': 'H6Tag'},
]

ELEMENT_GROUP_lists = [
    {'tag_name': 'ul', 'list': '_elements', 'class': 'UlTag'},
    {'tag_name': 'ol', 'list': '_elements', 'class': 'OlTag'},
    {'tag_name': 'dl', 'list': '_elements', 'class': 'DlTag'},
]

ELEMENT_GROUP_blocktext = [
    {'tag_name': 'pre', 'list': '_elements', 'class': 'PreTag'},
    {'tag_name': 'hr', 'list': '_elements', 'class': 'HrTag'},
    {'tag_name': 'blockquote', 'list': '_elements', 'class': 'BlockQuoteTag'},
    {'tag_name': 'address', 'list': '_elements', 'class': 'AddressTag'},
]

ELEMENT_GROUP_block = [
    {'tag_name': 'p', 'list': '_elements', 'class': 'PTag'},
]
ELEMENT_GROUP_block.extend(ELEMENT_GROUP_heading)
ELEMENT_GROUP_block.append({'tag_name': 'div', 'list': '_elements', 'class': 'DivTag'})
ELEMENT_GROUP_block.extend(ELEMENT_GROUP_lists)
ELEMENT_GROUP_block.extend(ELEMENT_GROUP_blocktext)
ELEMENT_GROUP_block.append({'tag_name': 'fieldset', 'list': '_elements', 'class': 'FieldSetTag'})
ELEMENT_GROUP_block.append({'tag_name': 'table', 'list': '_elements', 'class': 'TableTag'})

ELEMENT_GROUP_head_misc = [
    {'tag_name': 'script', 'list': '_elements', 'class': 'ScriptTag'},
    {'tag_name': 'style', 'list': '_elements', 'class': 'StyleTag'},
    {'tag_name': 'meta', 'list': '_elements', 'class': 'MetaTag'},
    {'tag_name': 'link', 'list': '_elements', 'class': 'LinkTag'},
    {'tag_name': 'object', 'list': '_elements', 'class': 'ObjectTag'},
]
