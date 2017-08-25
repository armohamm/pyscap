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
from scap.model.xlink.Simple import Simple

from .ComponentRefIDPattern import ComponentRefIDPattern

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=ComponentRefIDPattern)
@element(namespace='urn:oasis:names:tc:entity:xmlns:xml:catalog', local_name='catalog', min=0)
class ComponentRefElement(Simple):
    pass
