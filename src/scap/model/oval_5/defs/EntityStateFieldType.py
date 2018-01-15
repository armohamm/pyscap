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

from expatriate.model.decorators import *
from expatriate.model.xs.AnySimpleType import AnySimpleType
from expatriate.model.xs.BooleanType import BooleanType
from expatriate.model.xs.StringType import StringType

from .. import CHECK_ENUMERATION
from .. import DATATYPE_ENUMERATION
from .. import OPERATION_ENUMERATION
from ..VariableIdPattern import VariableIdPattern

logger = logging.getLogger(__name__)

@attribute(local_name='name', required=True, type=StringType, pattern=r'[^A-Z]+')
@attribute(local_name='datatype', enum=DATATYPE_ENUMERATION, default='string')
@attribute(local_name='operation', enum=OPERATION_ENUMERATION, default='equals')
@attribute(local_name='mask', type=BooleanType, default=False)
@attribute(local_name='var_ref', type=VariableIdPattern)
@attribute(local_name='var_check', enum=CHECK_ENUMERATION)
@attribute(local_name='entity_check', enum=CHECK_ENUMERATION, default='all')
class EntityStateFieldType(AnySimpleType):
    pass
