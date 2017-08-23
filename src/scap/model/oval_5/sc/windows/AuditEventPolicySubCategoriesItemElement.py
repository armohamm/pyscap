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

logger = logging.getLogger(__name__)

class AuditEventPolicySubCategoriesItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'credential_validation', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'kerberos_authentication_service', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'kerberos_service_ticket_operations', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'kerberos_ticket_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_account_logon_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'application_group_management', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'computer_account_management', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'distribution_group_management', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_account_management_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'security_group_management', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'user_account_management', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'dpapi_activity', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'process_creation', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'process_termination', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'rpc_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'directory_service_access', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'directory_service_changes', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'directory_service_replication', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'detailed_directory_service_replication', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'account_lockout', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'ipsec_extended_mode', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'ipsec_main_mode', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'ipsec_quick_mode', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'logoff', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'logon', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'network_policy_server', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_logon_logoff_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'special_logon', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'logon_claims', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'application_generated', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'certification_services', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'detailed_file_share', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'file_share', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'file_system', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'filtering_platform_connection', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'filtering_platform_packet_drop', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'handle_manipulation', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'kernel_object', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_object_access_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'registry', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'sam', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'removable_storage', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'central_access_policy_staging', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'audit_policy_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'authentication_policy_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'authorization_policy_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'filtering_platform_policy_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'mpssvc_rule_level_policy_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_policy_change_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'non_sensitive_privilege_use', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_privilege_use_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'sensitive_privilege_use', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'ipsec_driver', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'other_system_events', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'security_state_change', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'security_system_extension', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
            {'tag_name': 'system_integrity', 'max': 1, 'min': 0, 'class': 'EntityItemAuditType'},
        ],
        'attributes': {
        },
    }
