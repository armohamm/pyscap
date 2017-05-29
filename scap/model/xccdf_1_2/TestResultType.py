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

from scap.Model import Model
from scap.model.xccdf_1_2 import *

logger = logging.getLogger(__name__)
class TestResultType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'TestResultIDPattern'},
            'start-time': {'type': 'DateTime'},
            'end-time': {'type': 'DateTime'},
            'test-system': {'type': 'String'},
            'version': {'type': 'String'},
            'Id': {'type': 'ID'},
        },
        'elements': [
            {'tag_name': 'benchmark', 'class': 'BenchmarkReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'tailoring-file', 'class': 'TailoringReferenceType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'class': 'TextType', 'list': 'titles', 'min': 0, 'max': None},
            {'tag_name': 'remark', 'class': 'TextType', 'list': 'remarks', 'min': 0, 'max': None},
            {'tag_name': 'organization', 'type': 'String', 'list': 'organizations', 'min': 0, 'max': None},
            {'tag_name': 'identity', 'class': 'IdentityType', 'min': 0, 'max': 1},
            {'tag_name': 'profile', 'class': 'IDRefType', 'min': 0, 'max': 1},
            {'tag_name': 'target', 'type': 'String', 'list': 'targets', 'min': 1, 'max': None},
            {'tag_name': 'target-address', 'type': 'String', 'list': 'target_addresses', 'min': 0, 'max': None},
            {'tag_name': 'target-facts', 'class': 'TargetFactsType', 'list': 'target_facts', 'min': 0, 'max': None},
            {'tag_name': 'target-id-ref', 'class': 'TargetIDRefType', 'list': 'target_id_refs', 'min': 0, 'max': None},{'tag_name': '*', 'min': 0, 'max': None},
            {'tag_name': 'platform', 'class': 'CPE2IDRefType', 'list': 'platforms', 'min': 0, 'max': None},
            {'tag_name': 'set-value', 'class': 'ProfileSetValueType', 'dict': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-complex-value', 'class': 'ProfileSetComplexValueType', 'dict': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'rule-result', 'class': 'RuleResultType', 'dict': 'rule_results', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'score', 'class': 'ScoreType', 'list': 'scores', 'min': 1, 'max': None},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'list': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
    }
    # urn:xccdf:fact:asset:identifier:mac Ethernet media access control address (SHOULD be sent as a pair with the IPv4 or IPv6 address to ensure uniqueness)
    # urn:xccdf:fact:asset:identifier:ipv4 IPv4 address
    # urn:xccdf:fact:asset:identifier:ipv6 IPv6 address
    # urn:xccdf:fact:asset:identifier:host_name Host name of the asset, if assigned
    # urn:xccdf:fact:asset:identifier:fqdn Fully qualified domain name
    # urn:xccdf:fact:asset:identifier:ein Equipment identification number or other inventory tag number
    # urn:xccdf:fact:asset:identifier:pki: X.509 PKI certificate for the asset (encoded in Base-64)
    # urn:xccdf:fact:asset:identifier:pki:thumbprint SHA-1 hash of the PKI certification for the asset (encoded in Base-64)
    # urn:xccdf:fact:asset:identifier:guid Globally unique identifier for the asset
    # urn:xccdf:fact:asset:identifier:ldap LDAP directory string (distinguished name) of the asset, if assigned
    # urn:xccdf:fact:asset:identifier:active_directory Active Directory realm to which the asset belongs, if assigned
    # urn:xccdf:fact:asset:identifier:nis_domain NIS domain of the asset, if assigned
    # urn:xccdf:fact:asset:environmental_information: owning_organization Organization that tracks the asset on its inventory
    # urn:xccdf:fact:asset:environmental_information: current_region Geographic region where the asset is located
    # urn:xccdf:fact:asset:environmental_information: administration_unit Name of the organization that does system administration for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:title Title (e.g., Mr, Ms, Col) of the system administrator for an asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:e-mail E-mail address of the system administrator for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:first_name First name of the system administrator for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:last_name Last name of the system administrator for the asset
