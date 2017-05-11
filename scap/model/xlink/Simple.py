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
import requests
import xml.etree.ElementTree as ET

from scap.model.xlink.Model import Model

logger = logging.getLogger(__name__)
class Simple(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': '*', 'min': 0},
        ],
        'attributes': {
            '{http://www.w3.org/1999/xlink}type': {'enum': ['simple']},
        },
    }

    def from_xml(self, parent, el):
        super(Model, self).from_xml(parent, el)

        try:
            r = requests.get(self.href, stream=True)
        except:
            return

        sub_el = ET.parse(r.raw).getroot()
        self._parse_element(sub_el)
