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

logger = logging.getLogger(__name__)
class ocil(Model):
    def __init__(self):
        super(ocil, self).__init__()    # {http://scap.nist.gov/schema/ocil/2.0}ocil

        self.document = None
        self.questionnaires = {}
        self.test_actions = {}
        self.questions = {}
        self.artifacts = {}
        self.variables = {}
        self.results = None

        self.ignore_sub_elements.extend([
            '{http://scap.nist.gov/schema/ocil/2.0}generator',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}document':
            self.document = Model.load(self, sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}questionnaires':
            for sub_sub_el in sub_el:
                self.questionnaires[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}test_actions':
            for sub_sub_el in sub_el:
                self.test_actions[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}questions':
            for sub_sub_el in sub_el:
                self.questions[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}artifacts':
            for sub_sub_el in sub_el:
                self.artifacts[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}variables':
            for sub_sub_el in sub_el:
                self.variables[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}results':
            self.results = Model.load(self, sub_el)
        else:
            return super(ocil, self).parse_sub_el(sub_el)
        return True
