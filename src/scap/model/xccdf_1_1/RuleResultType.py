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
from . import RESULT_ENUMERATION
from . import ROLE_ENUMERATION
from . import SEVERITY_ENUMERATION
from scap.model.decorators import *
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.DateTimeType import DateTimeType
from scap.model.xs.StringType import StringType
from .WeightType import WeightType
from .OverrideType import OverrideType
from .IdentType import IdentType
from .MessageType import MessageType
from .InstanceResultType import InstanceResultType
from .FixType import FixType
from .CheckType import CheckType

logger = logging.getLogger(__name__)

@attribute(local_name='idref', type=NCNameType, required=True)
@attribute(local_name='role', enum=ROLE_ENUMERATION)
@attribute(local_name='severity', enum=SEVERITY_ENUMERATION)
@attribute(local_name='time', type=DateTimeType)
@attribute(local_name='version', type=StringType)
@attribute(local_name='weight', type=WeightType)
@element(local_name='result', enum=RESULT_ENUMERATION, min=1, max=1)
@element(local_name='override', list='overrides', cls=OverrideType, min=0, max=None)
@element(local_name='ident', list='idents', cls=IdentType, min=0, max=None)
@element(local_name='message', list='messages', cls=MessageType, min=0, max=None)
@element(local_name='instance', list='instances', cls=InstanceResultType, min=0, max=None)
@element(local_name='fix', list='fixes', cls=FixType, min=0, max=None)
@element(local_name='check', list='checks', cls=CheckType, min=0, max=None)
class RuleResultType(Model):
    pass
