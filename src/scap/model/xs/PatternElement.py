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
from scap.model.types import *

from .AnnotationElement import AnnotationElement
from .FacetType import FacetType

logger = logging.getLogger(__name__)

@attribute(local_name='value', type=StringType, required=True)
@attribute(local_name='*', )
@element(local_name='annotation', list='tags', cls=AnnotationElement, min=0)
class PatternElement(FacetType):
    def get_defs(self, schema, top_level):
        top_level.set_value_pattern(self.value)

        return super(FacetType, self).get_defs(schema, top_level)
