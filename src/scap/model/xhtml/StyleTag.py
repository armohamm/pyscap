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
@attribute(local_name='type', type=('scap.model.xhtml.ContentTypeType', 'ContentTypeType'), required=True)
@attribute(local_name='media', type=('scap.model.xhtml.MediaDescType', 'MediaDescType'))
@attribute(local_name='title', type=('scap.model.xhtml.TextType', 'TextType'))
@attribute(namespace='http://www.w3.org/XML/1998/namespace', local_name='space', enum=['preserve'])
@attribute(local_name='lang', type=('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
class StyleTag(Model):
    pass
