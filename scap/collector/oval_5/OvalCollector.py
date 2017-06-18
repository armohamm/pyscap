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

from scap.Collector import Collector

logger = logging.getLogger(__name__)
class OvalCollector(Collector):
    def __init__(self, host, args):
        super(OvalCollector, self).__init__(host, args)

        if 'object' not in self.args:
            raise ValueError('OVAL collector requires an OVAL object as an argument')

        if self.args['object'].deprecated:
            logger.warning('Deprecated object ' + self.args['object'].id + ' is being referenced')
