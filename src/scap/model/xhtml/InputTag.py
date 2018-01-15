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

from expatriate.model.Model import Model
from expatriate.model.decorators import *
from expatriate.model.xs.IdType import IdType
from expatriate.model.xs.NMTokensType import NMTokensType
from expatriate.model.xs.StringType import StringType

from . import INPUT_TYPE_ENUMERATION

logger = logging.getLogger(__name__)

@attribute(local_name='type', enum=INPUT_TYPE_ENUMERATION, default='text')
@attribute(local_name='name', type=StringType)
@attribute(local_name='value', type=StringType)
@attribute(local_name='checked', enum=['checked'])
@attribute(local_name='disabled', enum=['disabled'])
@attribute(local_name='readonly', enum=['readonly'])
@attribute(local_name='size', type=StringType)
@attribute(local_name='maxlength', type=('scap.model.xhtml.NumberType', 'NumberType'))
@attribute(local_name='src', type=('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='alt', type=StringType)
@attribute(local_name='usemap', type=('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='onselect', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onchange', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='accept', type=('scap.model.xhtml.ContentTypesType', 'ContentTypesType'))
@attribute(local_name='id', type=IdType)
@attribute(local_name='class', type=NMTokensType)
@attribute(local_name='style', type=('scap.model.xhtml.StyleSheetType', 'StyleSheetType'))
@attribute(local_name='title', type=('scap.model.xhtml.TextType', 'TextType'))
@attribute(local_name='lang', type=('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
@attribute(local_name='onclick', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='ondblclick', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousedown', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseup', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseover', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousemove', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseout', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeypress', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeydown', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeyup', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='accesskey', type=('scap.model.xhtml.CharacterType', 'CharacterType'))
@attribute(local_name='tabindex', type=('scap.model.xhtml.TabIndexNumberType', 'TabIndexNumberType'))
@attribute(local_name='onfocus', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onblur', type=('scap.model.xhtml.ScriptType', 'ScriptType'))
class InputTag(Model):
    pass
