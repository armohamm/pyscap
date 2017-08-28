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

@attribute(local_name='id', type=IdType)
@attribute(local_name='type', type=defer_class_load('scap.model.xhtml.ContentTypeType', 'ContentTypeType'), required=True)
@attribute(local_name='media', type=defer_class_load('scap.model.xhtml.MediaDescType', 'MediaDescType'))
@attribute(local_name='title', type=defer_class_load('scap.model.xhtml.TextType', 'TextType'))
@attribute(namespace='http://www.w3.org/XML/1998/namespace', local_name='space', enum=['preserve'])
@attribute(local_name='lang', type=defer_class_load('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
class StyleTag(Model):
    pass
