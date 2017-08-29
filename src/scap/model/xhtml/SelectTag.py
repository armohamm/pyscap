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

from scap.Model import Model
from scap.model.decorators import *
from scap.model.xs.IdType import IdType
from scap.model.xs.NMTokensType import NMTokensType
from scap.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='name', type=StringType)
@attribute(local_name='size', type=defer_class_load('scap.model.xhtml.NumberType', 'NumberType'))
@attribute(local_name='multiple', enum=['multiple'])
@attribute(local_name='disabled', enum=['disabled'])
@attribute(local_name='tabindex', type=defer_class_load('scap.model.xhtml.TabIndexNumberType', 'TabIndexNumberType'))
@attribute(local_name='onfocus', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onblur', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onchange', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='id', type=IdType)
@attribute(local_name='class', type=NMTokensType)
@attribute(local_name='style', type=defer_class_load('scap.model.xhtml.StyleSheetType', 'StyleSheetType'))
@attribute(local_name='title', type=defer_class_load('scap.model.xhtml.TextType', 'TextType'))
@attribute(local_name='lang', type=defer_class_load('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
@attribute(local_name='onclick', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='ondblclick', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousedown', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseup', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseover', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousemove', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseout', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeypress', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeydown', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeyup', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@element(local_name='optgroup', list='_elements', cls=defer_class_load('scap.model.xhtml.OptGroupTag', 'OptGroupTag'), max=None)
@element(local_name='option', list='_elements', cls=defer_class_load('scap.model.xhtml.OptionTag', 'OptionTag'), max=None)
class SelectTag(Model):
    pass
