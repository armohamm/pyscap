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
from scap.model.xs.BooleanType import BooleanType

logger = logging.getLogger(__name__)

@attribute(local_name='nolinkto', type=BooleanType, default=False)
@attribute(local_name='nomd5', type=BooleanType, default=False)
@attribute(local_name='nosize', type=BooleanType, default=False)
@attribute(local_name='nouser', type=BooleanType, default=False)
@attribute(local_name='nogroup', type=BooleanType, default=False)
@attribute(local_name='nomtime', type=BooleanType, default=False)
@attribute(local_name='nomode', type=BooleanType, default=False)
@attribute(local_name='nordev', type=BooleanType, default=False)
@attribute(local_name='noconfigfiles', type=BooleanType, default=False)
@attribute(local_name='noghostfiles', type=BooleanType, default=False)
@attribute(local_name='nofiledigest', type=BooleanType, default=False)
@attribute(local_name='nocaps', type=BooleanType, default=False)
class RpmVerifyFileBehaviors(Model):
    pass
