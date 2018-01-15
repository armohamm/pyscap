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

from expatriate.model.Model import Model
from expatriate.model.decorators import *

from .NameLineType import NameLineType
from .OrganisationNameElement import OrganisationNameElement
from .OrganisationTypeElement import OrganisationTypeElement

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='NameDetailsKeyRef', ) # from grKeyRefs
@attribute(local_name='*', )
@element(local_name='NameLine', list='name_lines', cls=NameLineType)
@element(local_name='OrganisationName', list='organisation_name', cls=OrganisationNameElement)
@element(local_name='OrganisationType', list='organisation_type', cls=OrganisationTypeElement)
class OrganisationNameDetailsType(Model):
    pass
