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

from scap.model.oval_5.defs.windows.ObjectType import ObjectType

logger = logging.getLogger(__name__)
class ServiceEffectiveRightsObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'serviceeffectiverights_object',
        'elements': [
            {'tag_name': 'service_name', 'class': 'scap.model.oval_5.defs.EntityObjectStringType', 'min': 0},
            {'tag_name': 'trustee_sid', 'class': 'scap.model.oval_5.defs.EntityObjectStringType', 'min': 0},
        ],
    }
