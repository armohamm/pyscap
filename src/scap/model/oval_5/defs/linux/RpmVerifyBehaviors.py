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

from scap.model.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)
class RpmVerifyBehaviors(Model):
    MODEL_MAP = {
        'attributes': {
            'nodeps': {'type': 'BooleanType', 'default': False},
            'nodigest': {'type': 'BooleanType', 'default': False},
            'nofiles': {'type': 'BooleanType', 'default': False},
            'noscripts': {'type': 'BooleanType', 'default': False},
            'nosignature': {'type': 'BooleanType', 'default': False},
            'nolinkto': {'type': 'BooleanType', 'default': False},
            'nomd5': {'type': 'BooleanType', 'default': False},
            'nosize': {'type': 'BooleanType', 'default': False},
            'nouser': {'type': 'BooleanType', 'default': False},
            'nogroup': {'type': 'BooleanType', 'default': False},
            'nomtime': {'type': 'BooleanType', 'default': False},
            'nomode': {'type': 'BooleanType', 'default': False},
            'nordev': {'type': 'BooleanType', 'default': False},
            'noconfigfiles': {'type': 'BooleanType', 'default': False},
            'noghostfiles': {'type': 'BooleanType', 'default': False},
        }
    }
