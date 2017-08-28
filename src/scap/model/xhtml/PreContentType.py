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

from scap.model.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)

@element(local_name='a', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.ATag', 'ATag'))
@element(local_name='tt', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.TtTag', 'TtTag'))
@element(local_name='i', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.ITag', 'ITag'))
@element(local_name='b', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.BTag', 'BTag'))
@element(local_name='big', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.BigTag', 'BigTag'))
@element(local_name='small', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SmallTag', 'SmallTag'))
@element(local_name='em', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.EmTag', 'EmTag'))
@element(local_name='strong', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.StrongTag', 'StrongTag'))
@element(local_name='dfn', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.DfnTag', 'DfnTag'))
@element(local_name='code', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.CodeTag', 'CodeTag'))
@element(local_name='q', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.QTag', 'QTag'))
@element(local_name='samp', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SampTag', 'SampTag'))
@element(local_name='kbd', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.KbdTag', 'KbdTag'))
@element(local_name='var', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.VarTag', 'VarTag'))
@element(local_name='cite', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.CiteTag', 'CiteTag'))
@element(local_name='abbr', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.AbbrTag', 'AbbrTag'))
@element(local_name='acronym', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.AcronymTag', 'AcronymTag'))
@element(local_name='sub', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SubTag', 'SubTag'))
@element(local_name='sup', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SupTag', 'SupTag'))
@element(local_name='br', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.BrTag', 'BrTag'))
@element(local_name='span', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SpanTag', 'SpanTag'))
@element(local_name='bdo', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.BdoTag', 'BdoTag'))
@element(local_name='map', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.MapTag', 'MapTag'))
# TODO ELEMENT_GROUP_misc_inline
@element(local_name='input', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.InputTag', 'InputTag'))
@element(local_name='select', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.SelectTag', 'SelectTag'))
@element(local_name='textarea', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.TextAreaTag', 'TextAreaTag'))
@element(local_name='label', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.LabelTag', 'LabelTag'))
@element(local_name='button', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.ButtonTag', 'ButtonTag'))
class PreContentType(Model):
    pass
