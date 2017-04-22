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
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'filepath', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'path', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'filename', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'header_signature', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'target_machine_type', 'class': 'EntityStatePeTargetMachineType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'number_of_sections', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'time_date_stamp', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'pointer_to_symbol_table', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'number_of_symbols', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_optional_header', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_relocs_stripped', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_executable_image', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_line_nums_stripped', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_local_syms_stripped', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_aggresive_ws_trim', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_large_address_aware', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_16bit_machine', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_bytes_reversed_lo', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_32bit_machine', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_debug_stripped', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_removable_run_from_swap', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_system', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_dll', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_up_system_only', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_file_bytes_reveresed_hi', 'class': 'oval_defs_5.EntityStateBoolType', 'default': False, 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'magic_number', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'major_linker_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'minor_linker_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_code', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_initialized_data', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_uninitialized_data', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'address_of_entry_point', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'base_of_code', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'base_of_data', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'image_base_address', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'section_alignment', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'file_alignment', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'major_operating_system_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'major_image_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'minor_operating_system_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'minor_image_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'major_subsystem_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'minor_susbsystem_version', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_image', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_headers', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'checksum', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'subsystem', 'class': 'EntityStatePeSubsystemType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'dll_characteristics', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_stack_reserve', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_stack_commit', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_heap_reserve', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'size_of_heap_commit', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'loader_flags', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'number_of_rva_and_sizes', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'real_number_of_directory_entries', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
        ],
    }
