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
from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)

class RpmVerifyFileItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'name', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'epoch', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'version', 'class': 'EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'release', 'class': 'EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'arch', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'extended_name', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'size_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'mode_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'md5_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'filedigest_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'device_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'link_mismatch', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'ownership_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'group_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'mtime_differs', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'capabilities_differ', 'class': 'EntityItemRpmVerifyResultType', 'min': 0, 'max': 1},
            {'tag_name': 'configuration_file', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'documentation_file', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'ghost_file', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'license_file', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
            {'tag_name': 'readme_file', 'class': 'scap.model.oval_5.sc.EntityItemType', 'min': 0, 'max': 1},
        ],
    }
