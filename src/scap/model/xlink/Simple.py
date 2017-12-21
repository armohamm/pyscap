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
import sys
import urllib.request
import expatriate

from scap.model.decorators import *

from .Base import Base

logger = logging.getLogger(__name__)

@attribute(local_name='type', enum=['simple'])
@element(local_name='*', min=0)
class Simple(Base):
    def from_xml(self, parent, el):
        super(Model, self).from_xml(parent, el)

        try:
            with urllib.request.urlopen(self.href) as r:
                # TODO
                doc = expatriate.Document()
                doc.parse(r.read())
                sub_el = doc.root_element
                self._parse_element(sub_el)
        except:
            logger.warning('Could not retrieve link ' + self.href + ' for ' + str(self) + ': ' + str(sys.exc_info()[1]))
