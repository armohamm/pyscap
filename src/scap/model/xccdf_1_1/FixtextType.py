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

from . import FIX_STRATEGY_ENUMERATION
from . import RATING_ENUMERATION
from .HtmlTextWithSubType import HtmlTextWithSubType
from scap.model.decorators import *
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.BooleanType import BooleanType

logger = logging.getLogger(__name__)

@attribute(local_name='fixref', type=NCNameType)
@attribute(local_name='reboot', type=BooleanType, default=False)
@attribute(local_name='strategy', enum=FIX_STRATEGY_ENUMERATION, default='unknown')
@attribute(local_name='disruption', enum=RATING_ENUMERATION, default='unknown')
@attribute(local_name='complexity', enum=RATING_ENUMERATION, default='unknown')
class FixtextType(HtmlTextWithSubType):
    pass
