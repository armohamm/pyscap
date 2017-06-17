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

from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class SharedResourceItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'netname', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'shared_type', 'max': 1, 'min': 0, 'class': 'EntityItemSharedResourceTypeType'},
            {'tag_name': 'max_uses', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType'},
            {'tag_name': 'current_uses', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType'},
            {'tag_name': 'local_path', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'access_read_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_write_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_create_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_exec_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_delete_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_atrib_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_perm_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_all_permission', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
        ],
        'attributes': {
        },
    }
