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
from expatriate.model.xs.NMTokenType import NMTokenType
from expatriate.model.xs.NMTokensType import NMTokensType

logger = logging.getLogger(__name__)

@attribute(local_name='declare', enum=['declare'])
@attribute(local_name='classid', type=defer_class_load('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='codebase', type=defer_class_load('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='data', type=defer_class_load('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='type', type=defer_class_load('scap.model.xhtml.ContentTypeType', 'ContentTypeType'))
@attribute(local_name='codetype', type=defer_class_load('scap.model.xhtml.ContentTypeType', 'ContentTypeType'))
@attribute(local_name='archive', type=defer_class_load('scap.model.xhtml.UriListType', 'UriListType'))
@attribute(local_name='standby', type=defer_class_load('scap.model.xhtml.TextType', 'TextType'))
@attribute(local_name='height', type=defer_class_load('scap.model.xhtml.LengthType', 'LengthType'))
@attribute(local_name='width', type=defer_class_load('scap.model.xhtml.LengthType', 'LengthType'))
@attribute(local_name='usemap', type=defer_class_load('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='name', type=NMTokenType)
@attribute(local_name='tabindex', type=defer_class_load('scap.model.xhtml.TabIndexNumberType', 'TabIndexNumberType'))
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
@element(local_name='param', list='_elements', cls=defer_class_load('scap.model.xhtml.ParamType', 'ParamType'), min=0, max=None)
@element(local_name='p', list='_elements', cls=defer_class_load('scap.model.xhtml.PTag', 'PTag'))
@element(local_name='h1', list='_elements', cls=defer_class_load('scap.model.xhtml.H1Tag', 'H1Tag'))
@element(local_name='h2', list='_elements', cls=defer_class_load('scap.model.xhtml.H2Tag', 'H2Tag'))
@element(local_name='h3', list='_elements', cls=defer_class_load('scap.model.xhtml.H3Tag', 'H3Tag'))
@element(local_name='h4', list='_elements', cls=defer_class_load('scap.model.xhtml.H4Tag', 'H4Tag'))
@element(local_name='h5', list='_elements', cls=defer_class_load('scap.model.xhtml.H5Tag', 'H5Tag'))
@element(local_name='h6', list='_elements', cls=defer_class_load('scap.model.xhtml.H6Tag', 'H6Tag'))
@element(local_name='div', list='_elements', cls=defer_class_load('scap.model.xhtml.DivTag', 'DivTag'))
@element(local_name='ul', list='_elements', cls=defer_class_load('scap.model.xhtml.UlTag', 'UlTag'))
@element(local_name='ol', list='_elements', cls=defer_class_load('scap.model.xhtml.OlTag', 'OlTag'))
@element(local_name='dl', list='_elements', cls=defer_class_load('scap.model.xhtml.DlTag', 'DlTag'))
@element(local_name='pre', list='_elements', cls=defer_class_load('scap.model.xhtml.PreTag', 'PreTag'))
@element(local_name='hr', list='_elements', cls=defer_class_load('scap.model.xhtml.HrTag', 'HrTag'))
@element(local_name='blockquote', list='_elements', cls=defer_class_load('scap.model.xhtml.BlockQuoteTag', 'BlockQuoteTag'))
@element(local_name='address', list='_elements', cls=defer_class_load('scap.model.xhtml.AddressTag', 'AddressTag'))
@element(local_name='fieldset', list='_elements', cls=defer_class_load('scap.model.xhtml.FieldSetTag', 'FieldSetTag'))
@element(local_name='table', list='_elements', cls=defer_class_load('scap.model.xhtml.TableTag', 'TableTag'))
@element(local_name='form', list='_elements', cls=defer_class_load('scap.model.xhtml.FormType', 'FormType'), min=0, max=None)
@element(local_name='a', list='_elements', cls=defer_class_load('scap.model.xhtml.ATag', 'ATag'))
@element(local_name='br', list='_elements', cls=defer_class_load('scap.model.xhtml.BrTag', 'BrTag'))
@element(local_name='span', list='_elements', cls=defer_class_load('scap.model.xhtml.SpanTag', 'SpanTag'))
@element(local_name='bdo', list='_elements', cls=defer_class_load('scap.model.xhtml.BdoTag', 'BdoTag'))
@element(local_name='map', list='_elements', cls=defer_class_load('scap.model.xhtml.MapTag', 'MapTag'))
@element(local_name='object', list='_elements', cls=defer_class_load('scap.model.xhtml.ObjectTag', 'ObjectTag'))
@element(local_name='img', list='_elements', cls=defer_class_load('scap.model.xhtml.ImgTag', 'ImgTag'))
@element(local_name='tt', list='_elements', cls=defer_class_load('scap.model.xhtml.TtTag', 'TtTag'))
@element(local_name='i', list='_elements', cls=defer_class_load('scap.model.xhtml.ITag', 'ITag'))
@element(local_name='b', list='_elements', cls=defer_class_load('scap.model.xhtml.BTag', 'BTag'))
@element(local_name='big', list='_elements', cls=defer_class_load('scap.model.xhtml.BigTag', 'BigTag'))
@element(local_name='small', list='_elements', cls=defer_class_load('scap.model.xhtml.SmallTag', 'SmallTag'))
@element(local_name='em', list='_elements', cls=defer_class_load('scap.model.xhtml.EmTag', 'EmTag'))
@element(local_name='strong', list='_elements', cls=defer_class_load('scap.model.xhtml.StrongTag', 'StrongTag'))
@element(local_name='dfn', list='_elements', cls=defer_class_load('scap.model.xhtml.DfnTag', 'DfnTag'))
@element(local_name='code', list='_elements', cls=defer_class_load('scap.model.xhtml.CodeTag', 'CodeTag'))
@element(local_name='q', list='_elements', cls=defer_class_load('scap.model.xhtml.QTag', 'QTag'))
@element(local_name='samp', list='_elements', cls=defer_class_load('scap.model.xhtml.SampTag', 'SampTag'))
@element(local_name='kbd', list='_elements', cls=defer_class_load('scap.model.xhtml.KbdTag', 'KbdTag'))
@element(local_name='var', list='_elements', cls=defer_class_load('scap.model.xhtml.VarTag', 'VarTag'))
@element(local_name='cite', list='_elements', cls=defer_class_load('scap.model.xhtml.CiteTag', 'CiteTag'))
@element(local_name='abbr', list='_elements', cls=defer_class_load('scap.model.xhtml.AbbrTag', 'AbbrTag'))
@element(local_name='acronym', list='_elements', cls=defer_class_load('scap.model.xhtml.AcronymTag', 'AcronymTag'))
@element(local_name='sub', list='_elements', cls=defer_class_load('scap.model.xhtml.SubTag', 'SubTag'))
@element(local_name='sup', list='_elements', cls=defer_class_load('scap.model.xhtml.SupTag', 'SupTag'))
@element(local_name='input', list='_elements', cls=defer_class_load('scap.model.xhtml.InputTag', 'InputTag'))
@element(local_name='select', list='_elements', cls=defer_class_load('scap.model.xhtml.SelectTag', 'SelectTag'))
@element(local_name='textarea', list='_elements', cls=defer_class_load('scap.model.xhtml.TextAreaTag', 'TextAreaTag'))
@element(local_name='label', list='_elements', cls=defer_class_load('scap.model.xhtml.LabelTag', 'LabelTag'))
@element(local_name='button', list='_elements', cls=defer_class_load('scap.model.xhtml.ButtonTag', 'ButtonTag'))
@element(local_name='noscript', list='_elements', cls=defer_class_load('scap.model.xhtml.NoScriptTag', 'NoScriptTag'))
@element(local_name='ins', list='_elements', cls=defer_class_load('scap.model.xhtml.InsTag', 'InsTag'))
@element(local_name='del', list='_elements', cls=defer_class_load('scap.model.xhtml.DelTag', 'DelTag'))
@element(local_name='script', list='_elements', cls=defer_class_load('scap.model.xhtml.ScriptTag', 'ScriptTag'))
class ObjectTag(Model):
    pass
