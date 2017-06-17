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
class FileEffectiveRightsItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'filepath', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'path', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'filename', 'max': 1, 'nillable': True, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'trustee_sid', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'trustee_name', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType'},
            {'tag_name': 'standard_delete', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'standard_read_control', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'standard_write_dac', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'standard_write_owner', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'standard_synchronize', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'access_system_security', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'generic_read', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'generic_write', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'generic_execute', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'generic_all', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_read_data', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_write_data', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_append_data', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_read_ea', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_write_ea', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_execute', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_delete_child', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_read_attributes', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'file_write_attributes', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType'},
            {'tag_name': 'windows_view', 'max': 1, 'min': 0, 'class': 'EntityItemWindowsViewType'},
        ],
        'attributes': {
        },
    }
