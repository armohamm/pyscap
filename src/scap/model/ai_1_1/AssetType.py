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

logger = logging.getLogger(__name__)

@attribute(None, 'timestamp', type='Timestamp')
@element(None, 'synthetic-id', class='SyntheticIDType', list='synthetic_ids', min=0, max=None),
@element(None, 'locations', class='LocationsType', min=0),
@element(None, 'extended-information', class='ExtendedInformationType', min=0),
@element('*', '*'),
class AssetType(Model):
    pass
