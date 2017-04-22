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

class AuditEventPolicyStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'auditeventpolicy_state',
        'elements': [
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'account_logon', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'account_management', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'detailed_tracking', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'directory_service_access', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'logon', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'object_access', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'policy_change', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'privilege_use', 'class': 'EntityStateAuditType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'system', 'class': 'EntityStateAuditType', 'min': 0},
        ],
    }
