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
class State(Model):
    @staticmethod
    def load(parent, state_el):
        if state_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_state':
            from scap.model.oval_defs_5_windows.RegistryState import RegistryState
            state = RegistryState()
        elif state_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_state':
            from scap.model.oval_defs_5_windows.WUAUpdateSearcherState import WUAUpdateSearcherState
            state = WUAUpdateSearcherState()
        else:
            logger.critical('Unknown state tag: ' + state_el.tag)
            import sys
            sys.exit()
        state.from_xml(parent, state_el)
        return state

    # abstract
    def __init__(self, tag_name=None):
        super(State, self).__init__(tag_name)

        self.operator = 'AND'

        self.ignore_attributes.extend([
            'version',
            'comment',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated state ' + self.id)
        elif name == 'operator':
            self.operator = value
        else:
            return super(State, self).parse_attribute(name, value)
        return True
