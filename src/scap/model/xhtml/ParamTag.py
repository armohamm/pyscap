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
from scap.model.xs.IdType import IdType
from scap.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=IdType)
@attribute(local_name='name', type=StringType)
@attribute(local_name='value', type=StringType)
@attribute(local_name='valuetype', enum=['data', 'ref', 'object'], default='data')
@attribute(local_name='type', type=defer_class_load('scap.model.xhtml.ContentTypeType', 'ContentTypeType'))
class ParamTag(Model):
    pass
