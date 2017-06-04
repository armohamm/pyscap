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
TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_test': 'AccessTokenTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_object': 'AccessTokenObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_state': 'AccessTokenStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_test': 'ActiveDirectoryTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_object': 'ActiveDirectoryObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_state': 'ActiveDirectoryStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_test': 'AuditEventPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_object': 'AuditEventPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_state': 'AuditEventPolicyStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_testpolicy_test': 'AuditEventPolicySubcategoriesTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_object': 'AuditEventPolicySubcategoriesObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_state': 'AuditEventPolicySubcategoriesStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_test': 'FileTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_object': 'FileObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_state': 'FileStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_test': 'FileAuditedPermissions53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_object': 'FileAuditedPermissions53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_state': 'FileAuditedPermissions53StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_test': 'FileAuditedPermissionsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_object': 'FileAuditedpermissionsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_state': 'FileAuditedpermissionsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_test': 'FileEffectiveRights53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_object': 'FileEffectiveRights53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_state': 'FileEffectiveRights53StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_test': 'FileEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_object': 'FileEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_state': 'FileEffectiveRightsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_test': 'GroupTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_object': 'GroupObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_state': 'GroupStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_test': 'InterfaceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_object': 'InterfaceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_state': 'InterfaceStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_test': 'LockoutPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_object': 'LockoutPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_state': 'LockoutPolicyStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_test': 'MetabaseTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_object': 'MetabaseObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_state': 'MetabaseStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_test': 'PasswordPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_object': 'PasswordPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_state': 'PasswordPolicyStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_test': 'PortTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_object': 'PortObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_state': 'PortStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_test': 'PrinterEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_object': 'PrinterEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_state': 'PrinterEffectiveRightsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_test': 'ProcessTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_object': 'ProcessObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_state': 'ProcessStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_test': 'RegistryTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_object': 'RegistryObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_state': 'RegistryStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_test': 'RegKeyAuditedPermissions53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_object': 'RegKeyAuditedPermissions53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_state': 'RegKeyAuditedPermissions53StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_test': 'RegKeyAuditedPermissionsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_object': 'RegKeyAuditedPermissionsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_state': 'RegKeyAuditedPermissionsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_test': 'RegKeyEffectiveRights53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_object': 'RegKeyEffectiveRights53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_state': 'RegKeyEffectiveRights53StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_test': 'RegKeyEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_object': 'RegKeyEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_state': 'RegKeyEffectiveRightsStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_test': 'SharedResourceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_object': 'SharedResourceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_state': 'SharedResourceStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_test': 'SidTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_object': 'SidObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_state': 'SidStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_test': 'UacTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_object': 'UacObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_state': 'UacStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_test': 'UserTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_object': 'UserObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_state': 'UserStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_test': 'VolumeTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_object': 'VolumeObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_state': 'VolumeStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_test': 'WmiTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_object': 'WmiObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_state': 'WmiStateElement',
}

ADDR_TYPE_ENUMERATION = [
    'MIB_IPADDR_DELETED',
    'MIB_IPADDR_DISCONNECTED',
    'MIB_IPADDR_DYNAMIC',
    'MIB_IPADDR_PRIMARY',
    'MIB_IPADDR_TRANSIENT',
    '',
]

ADSTYPE_ENUMERATION = [
    'ADSTYPE_INVALID',
    'ADSTYPE_DN_STRING',
    'ADSTYPE_CASE_EXACT_STRING',
    'ADSTYPE_CASE_IGNORE_STRING',
    'ADSTYPE_PRINTABLE_STRING',
    'ADSTYPE_NUMERIC_STRING',
    'ADSTYPE_BOOLEAN',
    'ADSTYPE_INTEGER',
    'ADSTYPE_OCTET_STRING',
    'ADSTYPE_UTC_TIME',
    'ADSTYPE_LARGE_INTEGER',
    'ADSTYPE_PROV_SPECIFIC',
    'ADSTYPE_OBJECT_CLASS',
    'ADSTYPE_CASEIGNORE_LIST',
    'ADSTYPE_OCTET_LIST',
    'ADSTYPE_PATH',
    'ADSTYPE_POSTALADDRESS',
    'ADSTYPE_TIMESTAMP',
    'ADSTYPE_BACKLINK',
    'ADSTYPE_TYPEDNAME',
    'ADSTYPE_HOLD',
    'ADSTYPE_NETADDRESS',
    'ADSTYPE_REPLICAPOINTER',
    'ADSTYPE_FAXNUMBER',
    'ADSTYPE_EMAIL',
    'ADSTYPE_NT_SECURITY_DESCRIPTOR',
    'ADSTYPE_UNKNOWN',
    'ADSTYPE_DN_WITH_BINARY',
    'ADSTYPE_DN_WITH_STRING',
    '',
]

AUDIT_ENUMERATION = [
    'AUDIT_FAILURE',
    'AUDIT_NONE',
    'AUDIT_SUCCESS',
    'AUDIT_SUCCESS_FAILURE',
    '',
]

INTERFACE_TYPE_ENUMERATION = [
    'MIB_IF_TYPE_ETHERNET',
    'MIB_IF_TYPE_FDDI',
    'MIB_IF_TYPE_LOOPBACK',
    'MIB_IF_TYPE_OTHER',
    'MIB_IF_TYPE_PPP',
    'MIB_IF_TYPE_SLIP',
    'MIB_IF_TYPE_TOKENRING',
    '',
]

FILE_TYPE_ENUMERATION = [
    'FILE_ATTRIBUTE_DIRECTORY',
    'FILE_TYPE_CHAR',
    'FILE_TYPE_DISK',
    'FILE_TYPE_PIPE',
    'FILE_TYPE_REMOTE',
    'FILE_TYPE_UNKNOWN',
    '',
]

NAMING_CONTEXT_ENUMERATION = [
    'domain',
    'configuration',
    'schema',
    '',
]

NTUSER_ACCOUNT_TYPE_ENUMERATION = [
    'local',
    'domain',
    '',
]

PROTOCOL_ENUMERATION = [
    'TCP',
    'UDP',
    '',
]

REGISTRY_HIVE_ENUMERATION = [
    'HKEY_CLASSES_ROOT',
    'HKEY_CURRENT_CONFIG',
    'HKEY_CURRENT_USER',
    'HKEY_LOCAL_MACHINE',
    'HKEY_USERS',
    '',
]

REGISTRY_TYPE_ENUMERATION = [
    'reg_binary',
    'reg_dword',
    'reg_dword_little_endian',
    'reg_dword_big_endian',
    'reg_expand_sz',
    'reg_link',
    'reg_multi_sz',
    'reg_none',
    'reg_qword',
    'reg_qword_little_endian',
    'reg_sz',
    'reg_resource_list',
    'reg_full_resource_descriptor',
    'reg_resource_requirements_list',
    '',
]

SHARED_RESOURCE_TYPE_ENUMERATION = [
    'STYPE_DISKTREE',
    'STYPE_DISKTREE_SPECIAL',
    'STYPE_DISKTREE_TEMPORARY',
    'STYPE_DISKTREE_SPECIAL_TEMPORARY',
    'STYPE_PRINTQ',
    'STYPE_PRINTQ_SPECIAL',
    'STYPE_PRINTQ_TEMPORARY',
    'STYPE_PRINTQ_SPECIAL_TEMPORARY',
    'STYPE_DEVICE',
    'STYPE_DEVICE_SPECIAL',
    'STYPE_DEVICE_TEMPORARY',
    'STYPE_DEVICE_SPECIAL_TEMPORARY',
    'STYPE_IPC',
    'STYPE_IPC_SPECIAL',
    'STYPE_IPC_TEMPORARY',
    'STYPE_IPC_SPECIAL_TEMPORARY',
    'STYPE_SPECIAL',
    'STYPE_TEMPORARY',
    '',
]

RECURSE_DIRECTION = ['none', 'up', 'down']
