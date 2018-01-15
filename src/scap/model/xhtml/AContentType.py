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

logger = logging.getLogger(__name__)

@element(local_name='br', list='_elements', cls=defer_class_load('scap.model.xhtml.BrTag', 'BrTag'), min=0, max=None)
@element(local_name='span', list='_elements', cls=defer_class_load('scap.model.xhtml.SpanTag', 'SpanTag'), min=0, max=None)
@element(local_name='bdo', list='_elements', cls=defer_class_load('scap.model.xhtml.BdoTag', 'BdoTag'), min=0, max=None)
@element(local_name='map', list='_elements', cls=defer_class_load('scap.model.xhtml.MapTag', 'MapTag'), min=0, max=None)
@element(local_name='object', list='_elements', cls=defer_class_load('scap.model.xhtml.ObjectTag', 'ObjectTag'), min=0, max=None)
@element(local_name='img', list='_elements', cls=defer_class_load('scap.model.xhtml.ImgTag', 'ImgTag'), min=0, max=None)
@element(local_name='tt', list='_elements', cls=defer_class_load('scap.model.xhtml.TtTag', 'TtTag'), min=0, max=None)
@element(local_name='i', list='_elements', cls=defer_class_load('scap.model.xhtml.ITag', 'ITag'), min=0, max=None)
@element(local_name='b', list='_elements', cls=defer_class_load('scap.model.xhtml.BTag', 'BTag'), min=0, max=None)
@element(local_name='big', list='_elements', cls=defer_class_load('scap.model.xhtml.BigTag', 'BigTag'), min=0, max=None)
@element(local_name='small', list='_elements', cls=defer_class_load('scap.model.xhtml.SmallTag', 'SmallTag'), min=0, max=None)
@element(local_name='em', list='_elements', cls=defer_class_load('scap.model.xhtml.EmTag', 'EmTag'), min=0, max=None)
@element(local_name='strong', list='_elements', cls=defer_class_load('scap.model.xhtml.StrongTag', 'StrongTag'), min=0, max=None)
@element(local_name='dfn', list='_elements', cls=defer_class_load('scap.model.xhtml.DfnTag', 'DfnTag'), min=0, max=None)
@element(local_name='code', list='_elements', cls=defer_class_load('scap.model.xhtml.CodeTag', 'CodeTag'), min=0, max=None)
@element(local_name='q', list='_elements', cls=defer_class_load('scap.model.xhtml.QTag', 'QTag'), min=0, max=None)
@element(local_name='samp', list='_elements', cls=defer_class_load('scap.model.xhtml.SampTag', 'SampTag'), min=0, max=None)
@element(local_name='kbd', list='_elements', cls=defer_class_load('scap.model.xhtml.KbdTag', 'KbdTag'), min=0, max=None)
@element(local_name='var', list='_elements', cls=defer_class_load('scap.model.xhtml.VarTag', 'VarTag'), min=0, max=None)
@element(local_name='cite', list='_elements', cls=defer_class_load('scap.model.xhtml.CiteTag', 'CiteTag'), min=0, max=None)
@element(local_name='abbr', list='_elements', cls=defer_class_load('scap.model.xhtml.AbbrTag', 'AbbrTag'), min=0, max=None)
@element(local_name='acronym', list='_elements', cls=defer_class_load('scap.model.xhtml.AcronymTag', 'AcronymTag'), min=0, max=None)
@element(local_name='sub', list='_elements', cls=defer_class_load('scap.model.xhtml.SubTag', 'SubTag'), min=0, max=None)
@element(local_name='sup', list='_elements', cls=defer_class_load('scap.model.xhtml.SupTag', 'SupTag'), min=0, max=None)
@element(local_name='input', list='_elements', cls=defer_class_load('scap.model.xhtml.InputTag', 'InputTag'), min=0, max=None)
@element(local_name='select', list='_elements', cls=defer_class_load('scap.model.xhtml.SelectTag', 'SelectTag'), min=0, max=None)
@element(local_name='textarea', list='_elements', cls=defer_class_load('scap.model.xhtml.TextAreaTag', 'TextAreaTag'), min=0, max=None)
@element(local_name='label', list='_elements', cls=defer_class_load('scap.model.xhtml.LabelTag', 'LabelTag'), min=0, max=None)
@element(local_name='button', list='_elements', cls=defer_class_load('scap.model.xhtml.ButtonTag', 'ButtonTag'), min=0, max=None)
@element(local_name='noscript', list='_elements', cls=defer_class_load('scap.model.xhtml.NoScriptTag', 'NoScriptTag'), min=0, max=None)
@element(local_name='ins', list='_elements', cls=defer_class_load('scap.model.xhtml.InsTag', 'InsTag'), min=0, max=None)
@element(local_name='del', list='_elements', cls=defer_class_load('scap.model.xhtml.DelTag', 'DelTag'), min=0, max=None)
@element(local_name='script', list='_elements', cls=defer_class_load('scap.model.xhtml.ScriptTag', 'ScriptTag'), min=0, max=None)
class AContentType(Model):
    pass
