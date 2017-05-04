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

from scap.Model import Model
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Simple(Model):
    def parse_value(self, value):
        return value

    def produce_value(self, value):
        return str(value)

    def is_none(self):
        return self.text is None

    def __str__(self):
        s = super(Simple, self).__str__()
        if self.text is not None:
            s = s + ' == ' + str(self.text)
        return s

    def from_xml(self, parent, sub_el):
        super(Simple, self).from_xml(parent, sub_el)

        if sub_el.text is not None:
            self.text = self.parse_value(sub_el.text)

    def to_xml(self):
        self.text = self.produce_value(self.text)
        return super(Simple, self).to_xml()
