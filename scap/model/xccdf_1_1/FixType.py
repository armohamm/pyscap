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

from scap.Model import Model
from scap.model.xccdf_1_1 import *

logger = logging.getLogger(__name__)
class FixType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'sub', 'list': 'subs', 'min': 0, 'max': None, 'class': 'IdrefType'},
            {'tag_name': 'instance', 'list': 'instance', 'min': 0, 'max': None, 'class': 'InstanceFixType'},
        ],
        'attributes': {
            'id': {'type': 'NCNameType'},
            'reboot': {'type': 'BooleanType'},
            'strategy': {'enum': FIX_STRATEGY_ENUMERATION, 'default': 'unknown'},
            'disruption': {'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'complexity': {'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'system': {'type': 'AnyURI'},
            'platform': {'type': 'AnyURI'},
        },
    }

    def __str__(self):
        s = 'FixType '
        if self.system is not None:
            s += self.system + ':'

        if self.id is not None:
            s += self.id + ':'

        if self.platform is not None:
            s += ' on ' + self.platform
        return s

    def fix(self, benchmark, host):
        # TODO check platform applies

        if self.system not in FIX_SYSTEM_ENUMERATION:
            return False

        # TODO confirm, if reboot needed

        # TODO strategy?

        raise NotImplementedError('fixing is not yet implemented')
