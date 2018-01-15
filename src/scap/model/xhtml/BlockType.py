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

@element(local_name='p', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.PTag', 'PTag'))
@element(local_name='h1', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H1Tag', 'H1Tag'))
@element(local_name='h2', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H2Tag', 'H2Tag'))
@element(local_name='h3', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H3Tag', 'H3Tag'))
@element(local_name='h4', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H4Tag', 'H4Tag'))
@element(local_name='h5', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H5Tag', 'H5Tag'))
@element(local_name='h6', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.H6Tag', 'H6Tag'))
@element(local_name='div', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.DivTag', 'DivTag'))
@element(local_name='ul', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.UlTag', 'UlTag'))
@element(local_name='ol', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.OlTag', 'OlTag'))
@element(local_name='dl', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.DlTag', 'DlTag'))
@element(local_name='pre', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.PreTag', 'PreTag'))
@element(local_name='hr', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.HrTag', 'HrTag'))
@element(local_name='blockquote', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.BlockQuoteTag', 'BlockQuoteTag'))
@element(local_name='address', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.AddressTag', 'AddressTag'))
@element(local_name='fieldset', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.FieldSetTag', 'FieldSetTag'))
@element(local_name='table', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.TableTag', 'TableTag'))
@element(local_name='form', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.FormTag', 'FormTag'))
@element(local_name='noscript', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.NoScriptTag', 'NoScriptTag'))
@element(local_name='ins', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.InsTag', 'InsTag'))
@element(local_name='del', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.DelTag', 'DelTag'))
@element(local_name='script', list='_elements', min=0, max=None, cls=defer_class_load('scap.model.xhtml.ScriptTag', 'ScriptTag'))
class BlockType(Model):
    pass
