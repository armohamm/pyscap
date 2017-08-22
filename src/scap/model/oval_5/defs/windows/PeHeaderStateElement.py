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

from scap.model.oval_5.defs.windows.StateType import StateType

logger = logging.getLogger(__name__)
class PeHeaderStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'peheader_state',
        'elements': [
@element(local_name='filepath', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='path', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='filename', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='header_signature', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='target_machine_type', cls=EntityStatePeTargetMachineType, min=0, max=1)
@element(local_name='number_of_sections', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='time_date_stamp', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='pointer_to_symbol_table', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='number_of_symbols', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_optional_header', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='image_file_relocs_stripped', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_executable_image', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_line_nums_stripped', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_local_syms_stripped', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_aggresive_ws_trim', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_large_address_aware', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_16bit_machine', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_bytes_reversed_lo', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_32bit_machine', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_debug_stripped', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_removable_run_from_swap', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_system', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_dll', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_up_system_only', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='image_file_bytes_reveresed_hi', cls=scap.model.oval_5.defs.EntityStateType, default=False, min=0, max=1)
@element(local_name='magic_number', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='major_linker_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='minor_linker_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_code', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_initialized_data', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_uninitialized_data', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='address_of_entry_point', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='base_of_code', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='base_of_data', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='image_base_address', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='section_alignment', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='file_alignment', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='major_operating_system_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='major_image_version', cls=scap.model.oval_5.defs.EntityStateType, min=0)
@element(local_name='minor_operating_system_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='minor_image_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='major_subsystem_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='minor_susbsystem_version', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_image', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_headers', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='checksum', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='subsystem', cls=EntityStatePeSubsystemType, min=0, max=1)
@element(local_name='dll_characteristics', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_stack_reserve', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_stack_commit', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_heap_reserve', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='size_of_heap_commit', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='loader_flags', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='number_of_rva_and_sizes', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
@element(local_name='real_number_of_directory_entries', cls=scap.model.oval_5.defs.EntityStateType, min=0, max=1)
        ],
    }
