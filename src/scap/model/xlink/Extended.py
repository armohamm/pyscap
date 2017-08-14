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

from scap.model.xlink.Model import Model

logger = logging.getLogger(__name__)
class Extended(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'title', 'list': 'titles', 'class': 'TitleEltType', 'min': 0, 'max': None},
            {'tag_name': 'resource', 'list': 'resources', 'class': 'ResourceType', 'min': 0, 'max': None},
            {'tag_name': 'locator', 'list': 'locators', 'class': 'LocatorType', 'min': 0, 'max': None},
            {'tag_name': 'arc', 'list': 'arcs', 'class': 'ArcType', 'min': 0, 'max': None},
            {'tag_name': '*', 'min': 0},
        ],
        'attributes': {
            '{http://www.w3.org/1999/xlink}type': {'enum': ['extended'], 'required': True},
        },
    }
