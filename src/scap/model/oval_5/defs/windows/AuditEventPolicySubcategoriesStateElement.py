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

from .StateType import StateType
from .EntityStateAuditType import EntityStateAuditType

logger = logging.getLogger(__name__)

@element(local_name='credential_validation', cls=EntityStateAuditType, min=0)
@element(local_name='kerberos_authentication_service', cls=EntityStateAuditType, min=0)
@element(local_name='kerberos_service_ticket_operations', cls=EntityStateAuditType, min=0)
@element(local_name='kerberos_ticket_events', cls=EntityStateAuditType, min=0)
@element(local_name='other_account_logon_events', cls=EntityStateAuditType, min=0)
@element(local_name='application_group_management', cls=EntityStateAuditType, min=0)
@element(local_name='computer_account_management', cls=EntityStateAuditType, min=0)
@element(local_name='distribution_group_management', cls=EntityStateAuditType, min=0)
@element(local_name='other_account_management_events', cls=EntityStateAuditType, min=0)
@element(local_name='security_group_management', cls=EntityStateAuditType, min=0)
@element(local_name='user_account_management', cls=EntityStateAuditType, min=0)
@element(local_name='dpapi_activity', cls=EntityStateAuditType, min=0)
@element(local_name='process_creation', cls=EntityStateAuditType, min=0)
@element(local_name='process_termination', cls=EntityStateAuditType, min=0)
@element(local_name='rpc_events', cls=EntityStateAuditType, min=0)
@element(local_name='directory_service_access', cls=EntityStateAuditType, min=0)
@element(local_name='directory_service_changes', cls=EntityStateAuditType, min=0)
@element(local_name='directory_service_replication', cls=EntityStateAuditType, min=0)
@element(local_name='detailed_directory_service_replication', cls=EntityStateAuditType, min=0)
@element(local_name='account_lockout', cls=EntityStateAuditType, min=0)
@element(local_name='ipsec_extended_mode', cls=EntityStateAuditType, min=0)
@element(local_name='ipsec_main_mode', cls=EntityStateAuditType, min=0)
@element(local_name='ipsec_quick_mode', cls=EntityStateAuditType, min=0)
@element(local_name='logoff', cls=EntityStateAuditType, min=0)
@element(local_name='logon', cls=EntityStateAuditType, min=0)
@element(local_name='network_policy_server', cls=EntityStateAuditType, min=0)
@element(local_name='other_logon_logoff_events', cls=EntityStateAuditType, min=0)
@element(local_name='special_logon', cls=EntityStateAuditType, min=0)
@element(local_name='logon_claims', cls=EntityStateAuditType, min=0)
@element(local_name='application_generated', cls=EntityStateAuditType, min=0)
@element(local_name='certification_services', cls=EntityStateAuditType, min=0)
@element(local_name='detailed_file_share', cls=EntityStateAuditType, min=0)
@element(local_name='file_share', cls=EntityStateAuditType, min=0)
@element(local_name='file_system', cls=EntityStateAuditType, min=0)
@element(local_name='filtering_platform_connection', cls=EntityStateAuditType, min=0)
@element(local_name='filtering_platform_packet_drop', cls=EntityStateAuditType, min=0)
@element(local_name='handle_manipulation', cls=EntityStateAuditType, min=0)
@element(local_name='kernel_object', cls=EntityStateAuditType, min=0)
@element(local_name='other_object_access_events', cls=EntityStateAuditType, min=0)
@element(local_name='registry', cls=EntityStateAuditType, min=0)
@element(local_name='sam', cls=EntityStateAuditType, min=0)
@element(local_name='removable_storage', cls=EntityStateAuditType, min=0)
@element(local_name='central_access_policy_staging', cls=EntityStateAuditType, min=0)
@element(local_name='audit_policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='authentication_policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='authorization_policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='filtering_platform_policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='mpssvc_rule_level_policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='other_policy_change_events', cls=EntityStateAuditType, min=0)
@element(local_name='non_sensitive_privilege_use', cls=EntityStateAuditType, min=0)
@element(local_name='other_privilege_use_events', cls=EntityStateAuditType, min=0)
@element(local_name='sensitive_privilege_use', cls=EntityStateAuditType, min=0)
@element(local_name='ipsec_driver', cls=EntityStateAuditType, min=0)
@element(local_name='other_system_events', cls=EntityStateAuditType, min=0)
@element(local_name='security_state_change', cls=EntityStateAuditType, min=0)
@element(local_name='security_system_extension', cls=EntityStateAuditType, min=0)
@element(local_name='system_integrity', cls=EntityStateAuditType, min=0)
class AuditEventPolicySubcategoriesStateElement(StateType):
    pass
