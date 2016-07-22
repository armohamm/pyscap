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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class ComponentReference(Simple):
    def __init__(self):
        super(ComponentReference, self).__init__()

        self.href = None
        self.ref_mapping = {}

    def parse_attrib(self, name, value):
        if name == '{http://www.w3.org/1999/xlink}href':
            self.href = value
        else:
            return super(ComponentReference, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog':
            logger.debug('Loading catalog for ' + self.href)
            from scap.model.xml_cat.Catalog import Catalog
            cat = Catalog()
            cat.from_xml(self, sub_el)
            self.ref_mapping = cat.to_dict()
        else:
            return super(ComponentReference, self).parse_sub_el(sub_el)
        return True

    def resolve(self):
        component = self.resolve_reference(self.href)
        if component.content.tag == '{http://checklists.nist.gov/xccdf/1.2}Benchmark':
            from scap.model.xccdf_1_2.Benchmark import Benchmark
            comp = Benchmark()
        elif component.content.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil':
            from scap.model.ocil_2_0.OCIL import OCIL
            comp = OCIL()
        elif component.content.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions':
            from scap.model.oval_defs_5.OVALDefinitions import OVALDefinitions
            comp = OVALDefinitions()
        comp.from_xml(self, component.content)
        comp.set_ref_mapping(self.ref_mapping)
        return comp
