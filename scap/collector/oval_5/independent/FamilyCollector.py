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

from scap.collector.oval_5.OvalCollector import OvalCollector
from scap.model.cpe_matching_2_3.CPE import CPE
from scap.model.oval_5.sc.independent.FamilyItemElement import FamilyItemElement
from scap.model.oval_5.sc.independent.EntityItemFamilyType import EntityItemFamilyType

logger = logging.getLogger(__name__)
class FamilyCollector(OvalCollector):
    def __init__(self, host, args):
        super(FamilyCollector, self).__init__(host, args)

        # FamilyCollector is one of the few that DOESN'T need an actual object
        # if 'object' not in self.args:
        #     raise ValueError('OVAL collector requires an OVAL object as an argument')

        if self.args['object'].deprecated:
            logger.warning('Deprecated object ' + self.args['object'].id + ' is being referenced')

    def collect(self):
        obj = self.args['object']

        if 'cpe' not in self.host.facts or 'os' not in self.host.facts['cpe'] or len(self.host.facts['cpe']['os']) <= 0:
            raise ValueError('Need a defined OS CPE to determine family')

        if 'oval_family' not in self.host.facts:
            for cpe in self.host.facts['cpe']['os']:
                logger.debug('Checking ' + str(cpe) + ' for family match')
                if CPE(part='o', vendor='linux').matches(cpe):
                    self.host.facts['oval_family'] = 'linux'
                elif CPE(part='o', vendor='microsoft').matches(cpe):
                    self.host.facts['oval_family'] = 'windows'

        item = FamilyItemElement()
        item.family = EntityItemFamilyType(value=self.host.facts['oval_family'])
        return [item]

        raise ValueError('Unable to determine family from discovered CPEs')
