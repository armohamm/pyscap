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
import pytest
import xml.etree.ElementTree as ET

from scap.Model import Model

Model.register_namespace('scap.model.oval', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')

logging.basicConfig(level=logging.DEBUG)

def test_oval_5_3_detected():
    test_xml = '<oval_definitions ' + \
        'xmlns="http://oval.mitre.org/XMLSchema/oval-definitions-5" ' + \
        'xmlns:oval="http://oval.mitre.org/XMLSchema/oval-common-5" ' + \
        'xmlns:oval-def="http://oval.mitre.org/XMLSchema/oval-definitions-5">' + \
        '<generator>' + \
        '<oval:product_name>The OVAL Repository</oval:product_name>' + \
        '<oval:schema_version>5.3</oval:schema_version>' + \
        '<oval:timestamp>2008-04-10T09:00:10.653-04:00</oval:timestamp>' + \
      '</generator>' + \
      '</oval_definitions>'
    model = Model.load(None, ET.fromstring(test_xml))
    from scap.model.oval.oval_5_3.defs.OvalDefinitionsElement import OvalDefinitionsElement
    assert isinstance(model, OvalDefinitionsElement)
