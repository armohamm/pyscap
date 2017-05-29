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
class PeHeaderStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'peheader_state',
        'elements': [
            {'tag_name': 'filepath', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'filename', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'header_signature', 'class': 'scap.model.oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'target_machine_type', 'class': 'EntityStatePeTargetMachineType', 'min': 0, 'max': 1},
            {'tag_name': 'number_of_sections', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'time_date_stamp', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'pointer_to_symbol_table', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'number_of_symbols', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_optional_header', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'image_file_relocs_stripped', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_executable_image', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_line_nums_stripped', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_local_syms_stripped', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_aggresive_ws_trim', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_large_address_aware', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_16bit_machine', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_bytes_reversed_lo', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_32bit_machine', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_debug_stripped', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_removable_run_from_swap', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_system', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_dll', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_up_system_only', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'image_file_bytes_reveresed_hi', 'class': 'scap.model.oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'tag_name': 'magic_number', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'major_linker_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'minor_linker_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_code', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_initialized_data', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_uninitialized_data', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'address_of_entry_point', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'base_of_code', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'base_of_data', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'image_base_address', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'section_alignment', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'file_alignment', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'major_operating_system_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'major_image_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'minor_operating_system_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'minor_image_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'major_subsystem_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'minor_susbsystem_version', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_image', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_headers', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'checksum', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'subsystem', 'class': 'EntityStatePeSubsystemType', 'min': 0, 'max': 1},
            {'tag_name': 'dll_characteristics', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_stack_reserve', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_stack_commit', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_heap_reserve', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'size_of_heap_commit', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'loader_flags', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'number_of_rva_and_sizes', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'real_number_of_directory_entries', 'class': 'scap.model.oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
        ],
    }
