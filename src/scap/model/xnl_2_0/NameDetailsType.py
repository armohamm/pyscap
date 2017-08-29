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

from .JointPersonNameElement import JointPersonNameElement
from .NameLineType import NameLineType
from .OrganisationNameDetailsElement import OrganisationNameDetailsElement
from .PersonNameElement import PersonNameElement

logger = logging.getLogger(__name__)

@attribute(local_name='PartyType', )
@attribute(local_name='Code', )
@attribute(local_name='*', )
@element(local_name='NameLine', list='name_lines', cls=NameLineType)
@element(local_name='PersonName', into='person_name', cls=PersonNameElement)
@element(local_name='JointPersonName', into='joint_person_name', cls=JointPersonNameElement)
@element(local_name='OrganisationNameDetails', into='organisation_name_details', cls=OrganisationNameDetailsElement)
class NameDetailsType(Model):
    pass
