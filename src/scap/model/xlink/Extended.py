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

from .Base import Base
from scap.model.decorators import *
from .TitleEltType import TitleEltType
from .ResourceType import ResourceType
from .LocatorType import LocatorType
from .ArcType import ArcType

logger = logging.getLogger(__name__)

@attribute(local_name='type', enum=['extended'], required=True)
@element(local_name='title', list='titles', cls=TitleEltType, min=0, max=None)
@element(local_name='resource', list='resources', cls=ResourceType, min=0, max=None)
@element(local_name='locator', list='locators', cls=LocatorType, min=0, max=None)
@element(local_name='arc', list='arcs', cls=ArcType, min=0, max=None)
@element(local_name='*', min=0)
class Extended(Base):
    pass
