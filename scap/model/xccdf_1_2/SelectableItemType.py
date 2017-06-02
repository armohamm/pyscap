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

from scap.model.xccdf_1_2 import *
from scap.model.xccdf_1_2.ItemType import ItemType

logger = logging.getLogger(__name__)
class SelectableItemType(ItemType):
    MODEL_MAP = {
        'attributes': {
            'selected': {'type': 'Boolean', 'default': True},
            'weight': {'type': 'Weight', 'default': 1.0},
        },
        'elements': [
            {'tag_name': 'rationale', 'list': 'rationales', 'min': 0, 'max': None, 'class': 'HtmlTextWithSubType'},
            {'tag_name': 'platform', 'list': 'platforms', 'min': 0, 'max': None, 'class': 'OverrideableCPE2IDRefType'},
            {'tag_name': 'requires', 'list': 'requires', 'min': 0, 'max': None, 'class': 'IDRefListType'},
            {'tag_name': 'conflicts', 'list': 'conflicts', 'min': 0, 'max': None, 'class': 'IDRefType'},
        ],
    }
    # abstract
