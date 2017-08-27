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

from . import SCAP_VERSION_ENUMERATION
from . import USE_CASE_ENUMERATION
from .DataStreamIDPattern import DataStreamIDPattern
from .RefListType import RefListType

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=DataStreamIDPattern)
@attribute(local_name='use-case', required=True, enum=USE_CASE_ENUMERATION) # TODO: spec also allows Token
@attribute(local_name='scap-version', required=True, enum=SCAP_VERSION_ENUMERATION) # TODO: spec also allows Token
@attribute(local_name='timestamp', required=True, type=DateTimeType)
@element(local_name='dictionaries',  cls=RefListType, min=0 )
@element(local_name='checklists',  cls=RefListType, min=0 )
@element(local_name='checks',  cls=RefListType )
@element(local_name='extended-components', min=0, cls=RefListType )
class DataStreamElement(Model):
    pass
