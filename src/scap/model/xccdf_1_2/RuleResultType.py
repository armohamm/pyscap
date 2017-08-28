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
from . import ROLE_ENUMERATION, SEVERITY_ENUMERATION, RESULT_ENUMERATION
from scap.model.decorators import *

logger = logging.getLogger(__name__)

@attribute(local_name='idref', type=NCNameType, required=True)
@attribute(local_name='role', enum=ROLE_ENUMERATION)
@attribute(local_name='severity', enum=SEVERITY_ENUMERATION)
@attribute(local_name='time', type=DateTimeType)
@attribute(local_name='version', type=StringType)
@attribute(local_name='weight', type=Weight)
@element(local_name='result', enum=RESULT_ENUMERATION, min=1, max=1)
@element(local_name='override', cls=OverrideType, list='overrides', min=0, max=None)
@element(local_name='ident', cls=IdentType, list='idents', min=0, max=None)
@element(local_name='metadata', cls=MetadataType, list='metadata', min=0, max=None)
@element(local_name='message', cls=MessageType, list='messages', min=0, max=None)
@element(local_name='instance', cls=InstanceResultType, list='instances', min=0, max=None)
@element(local_name='fix', cls=FixType, list='fixes', min=0, max=None)
@element(local_name='check', cls=CheckType, list='checks', min=0, max=None)
@element(local_name='complex-check', cls=ComplexCheckType, min=0, max=1)
class RuleResultType(Model):
    pass
