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
from scap.model.xs.DateTimeType import DateTimeType
from scap.model.xs.DecimalType import DecimalType
from scap.model.xs.NormalizedStringType import NormalizedStringType

from .ExtensionContainerType import ExtensionContainerType
from .UserType import UserType

logger = logging.getLogger(__name__)

@element(local_name='product_name', type=NormalizedStringType, min=0, max=1)
@element(local_name='product_version', type=NormalizedStringType, min=0, max=1)
@element(local_name='author', list='authors', cls=UserType, min=0, max=None)
@element(local_name='schema_version', type=DecimalType, min=1, max=1)
@element(local_name='timestamp', type=DateTimeType, min=1, max=1)
@element(local_name='additional_data', cls=ExtensionContainerType, min=0)
class GeneratorType(Model):
    pass
