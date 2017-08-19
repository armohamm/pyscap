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
from scap.model.rep_core_1_1.RelationshipsContainerType import RelationshipsContainerType

logger = logging.getLogger(__name__)

@attribute(None, 'id', type='NCNameType', required=True)
@attribute('*', '*')
@element(None, 'report-requests', cls='ReportRequestsType', min=0)
@element(None, 'assets', cls='AssetsType', min=0)
@element(None, 'reports', cls='ReportsType')
@element(None, 'extended-infos', cls='ExtendedInfosType', min=0)
class AssetReportCollectionElement(RelationshipsContainerType):
    pass
