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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class FileEffectiveRightsStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'fileeffectiverights_state',
        'elements': [
            {'tag_name': 'path', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'filename', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'trustee_name', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'standard_delete', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_read_control', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_write_dac', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_write_owner', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'standard_synchronize', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_system_security', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_read', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_write', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_execute', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'generic_all', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_read_data', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_write_data', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_append_data', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_read_ea', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_write_ea', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_execute', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_delete_child', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_read_attributes', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'file_write_attributes', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'windows_view', 'class': 'EntityStateWindowsViewType', 'min': 0},
        ],
    }
