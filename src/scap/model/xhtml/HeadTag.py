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

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=IdType)
@attribute(local_name='profile', type=('scap.model.xhtml.UriType', 'UriType'))
@attribute(local_name='lang', type=('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
@element(local_name='script', list='_elements', cls=('scap.model.xhtml.ScriptTag', 'ScriptTag'))
@element(local_name='style', list='_elements', min=0, cls=('scap.model.xhtml.StyleTag', 'StyleTag'))
@element(local_name='meta', list='_elements', min=0, cls=('scap.model.xhtml.MetaTag', 'MetaTag'))
@element(local_name='link', list='_elements', min=0, cls=('scap.model.xhtml.LinkTag', 'LinkTag'))
@element(local_name='object', list='_elements', min=0, cls=('scap.model.xhtml.ObjectTag', 'ObjectTag'))
@element(local_name='base', list='_elements', min=0, cls=('scap.model.xhtml.BaseTag', 'BaseTag'))
@element(local_name='title', list='_elements', cls=('scap.model.xhtml.TitleTag', 'TitleTag'))
class HeadTag(Model):
    pass
