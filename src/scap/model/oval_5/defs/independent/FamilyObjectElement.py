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
from scap.model.oval_5.defs.independent.ObjectType import ObjectType
from scap.model.oval_5.sc.independent.FamilyItemElement import FamilyItemElement
from scap.model.oval_5.sc.independent.EntityItemFamilyType import EntityItemFamilyType

logger = logging.getLogger(__name__)

class FamilyObjectElement(ObjectType):
    def evaluate(self, host, content, imports, export_names):
        if 'oval_family' not in host.facts:
            if 'cpe' not in host.facts or 'os' not in host.facts['cpe'] or len(host.facts['cpe']['os']) <= 0:
                raise ValueError('Need a defined OS CPE to determine family')

            for cpe in host.facts['cpe']['os']:
                logger.debug('Checking ' + str(cpe) + ' for family match')
                if CPE(part='o', vendor='linux').matches(cpe):
                    host.facts['oval_family'] = 'linux'
                elif CPE(part='o', vendor='microsoft').matches(cpe):
                    host.facts['oval_family'] = 'windows'

            if 'oval_family' not in host.facts:
                raise ValueError('Unable to determine family from discovered CPEs')

        item = FamilyItemElement(self, {})
        item.family = EntityItemFamilyType(value=host.facts['oval_family'])
        return [item]
