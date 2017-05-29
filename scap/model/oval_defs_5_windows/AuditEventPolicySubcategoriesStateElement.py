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

from scap.model.oval_common_5 import *
from scap.model.oval_defs_5 import *
from scap.model.oval_defs_5_windows import *
from scap.model.oval_defs_5_windows.StateType import StateType

logger = logging.getLogger(__name__)

class AuditEventPolicySubcategoriesStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'auditeventpolicysubcategories_state',
        'elements': [
            {'tag_name': 'credential_validation', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'kerberos_authentication_service', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'kerberos_service_ticket_operations', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'kerberos_ticket_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_account_logon_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'application_group_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'computer_account_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'distribution_group_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_account_management_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'security_group_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'user_account_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'dpapi_activity', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'process_creation', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'process_termination', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'rpc_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'directory_service_access', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'directory_service_changes', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'directory_service_replication', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'detailed_directory_service_replication', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'account_lockout', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'ipsec_extended_mode', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'ipsec_main_mode', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'ipsec_quick_mode', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'logoff', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'logon', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'network_policy_server', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_logon_logoff_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'special_logon', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'logon_claims', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'application_generated', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'certification_services', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'detailed_file_share', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_share', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'file_system', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'filtering_platform_connection', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'filtering_platform_packet_drop', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'handle_manipulation', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'kernel_object', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_object_access_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'registry', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'sam', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'removable_storage', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'central_access_policy_staging', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'audit_policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'authentication_policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'authorization_policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'filtering_platform_policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'mpssvc_rule_level_policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_policy_change_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'non_sensitive_privilege_use', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_privilege_use_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'sensitive_privilege_use', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'ipsec_driver', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'other_system_events', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'security_state_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'security_system_extension', 'class': 'EntityStateAuditType', 'min': 0},
            {'tag_name': 'system_integrity', 'class': 'EntityStateAuditType', 'min': 0},
        ],
    }
