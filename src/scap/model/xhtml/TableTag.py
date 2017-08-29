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

from . import T_FRAME_ENUMERATION
from . import T_RULES_ENUMERATION

logger = logging.getLogger(__name__)

@attribute(local_name='summary', type=defer_class_load('scap.model.xhtml.TextType', 'TextType'))
@attribute(local_name='width', type=defer_class_load('scap.model.xhtml.LengthType', 'LengthType'))
@attribute(local_name='border', type=defer_class_load('scap.model.xhtml.PixelsType', 'PixelsType'))
@attribute(local_name='frame', enum=T_FRAME_ENUMERATION)
@attribute(local_name='rules', enum=T_RULES_ENUMERATION)
@attribute(local_name='cellspacing', type=defer_class_load('scap.model.xhtml.LengthType', 'LengthType'))
@attribute(local_name='cellpadding', type=defer_class_load('scap.model.xhtml.LengthType', 'LengthType'))
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
@element(local_name='caption', type=defer_class_load('scap.model.xhtml.CaptionTag', 'CaptionTag'), min=0)
@element(local_name='col', type=defer_class_load('scap.model.xhtml.ColTag', 'ColTag'), min=0, max=None)
@element(local_name='colgroup', type=defer_class_load('scap.model.xhtml.ColGroupTag', 'ColGroupTag'), min=0, max=None)
@element(local_name='thead', type=defer_class_load('scap.model.xhtml.THeadTag', 'THeadTag'), min=0)
@element(local_name='tfoot', type=defer_class_load('scap.model.xhtml.TFootTag', 'TFootTag'), min=0)
@element(local_name='tbody', type=defer_class_load('scap.model.xhtml.TBodyTag', 'TBodyTag'), min=0, max=None)
@element(local_name='tr', type=defer_class_load('scap.model.xhtml.TRTag', 'TRTag'), min=0, max=None)
class TableTag(Model):
    pass
