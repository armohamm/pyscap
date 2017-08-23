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
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

class FileItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='filepath', max=1, min=0, cls=EntityItemType)
@element(local_name='path', max=1, min=0, cls=EntityItemType)
@element(local_name='filename', max=1, 'nillable': True, min=0, cls=EntityItemType)
@element(local_name='owner', max=1, min=0, cls=EntityItemType)
@element(local_name='size', max=1, min=0, cls=EntityItemType)
@element(local_name='a_time', max=1, min=0, cls=EntityItemType)
@element(local_name='c_time', max=1, min=0, cls=EntityItemType)
@element(local_name='m_time', max=1, min=0, cls=EntityItemType)
@element(local_name='ms_checksum', max=1, min=0, cls=EntityItemType)
@element(local_name='version', max=1, min=0, cls=EntityItemType)
@element(local_name='type', max=1, min=0, cls=EntityItemFileTypeType)
@element(local_name='development_class', max=1, min=0, cls=EntityItemType)
@element(local_name='company', max=1, min=0, cls=EntityItemType)
@element(local_name='internal_name', max=1, min=0, cls=EntityItemType)
@element(local_name='language', max=1, min=0, cls=EntityItemType)
@element(local_name='original_filename', max=1, min=0, cls=EntityItemType)
@element(local_name='product_name', max=1, min=0, cls=EntityItemType)
@element(local_name='product_version', max=1, min=0, cls=EntityItemType)
@element(local_name='windows_view', max=1, min=0, cls=EntityItemWindowsViewType)
        ],
        'attributes': {
        },
    }
