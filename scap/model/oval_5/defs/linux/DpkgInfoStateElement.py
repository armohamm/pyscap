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

from scap.model.oval_5 import *
from scap.model.oval_5.defs import *
from scap.model.oval_5.defs.linux import *
from scap.model.oval_5.defs.linux.StateType import StateType

logger = logging.getLogger(__name__)
class DpkgInfoStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'dpkginfo_state',
        'elements': [
            {'tag_name': 'name', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': None},
            {'tag_name': 'arch', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': None},
            {'tag_name': 'epoch', 'class': 'EpochElement', 'min': 0, 'max': None},
            {'tag_name': 'release', 'class': 'ReleaseElement', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionElement', 'min': 0, 'max': None},
            {'tag_name': 'evr', 'class': 'DpkgInfoStateEvrElement', 'min': 0, 'max': None},
        ],
    }
