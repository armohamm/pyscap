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

ELEMENT_MAP = {
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'accesstoken_item'): 'AccessTokenItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'activedirectory57_item'): 'ActiveDirectory57ItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'activedirectory_item'): 'ActiveDirectoryItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'auditeventpolicy_item'): 'AuditEventPolicyItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'auditeventpolicysubcategories_item'): 'AuditEventPolicySubCategoriesItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'cmdlet_item'): 'CmdletItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'dnscache_item'): 'DnsCacheItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'file_item'): 'FileItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'fileauditedpermissions_item'): 'FileAuditedPermissionsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'fileeffectiverights_item'): 'FileEffectiveRightsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'group_item'): 'GroupItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'group_sid_item'): 'GroupSidItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'interface_item'): 'InterfaceItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'license_item'): 'LicenseItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'lockoutpolicy_item'): 'LockoutPolicyItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'metabase_item'): 'MetabaseItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'ntuser_item'): 'NtUserItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'passwordpolicy_item'): 'PasswordPolicyItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'peheader_item'): 'PeHeaderItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'port_item'): 'PortItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'printereffectiverights_item'): 'PrinterEffectiveRightsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'process_item'): 'ProcessItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'registry_item'): 'RegistryItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'regkeyauditedpermissions_item'): 'RegKeyAuditedPermissionsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'regkeyeffectiverights_item'): 'RegKeyEffectiveRightsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'service_item'): 'ServiceItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'serviceeffectiverights_item'): 'ServiceEffectiveRightsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'sharedresource_item'): 'SharedResourceItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'sharedresourceauditedpermissions_item'): 'SharedResourceAuditedPermissionsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'sharedresourceeffectiverights_item'): 'SharedResourceEffectiveRightsItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'sid_item'): 'SidItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'sid_sid_item'): 'SidSidItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'systemmetric_item'): 'SystemMetricItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'uac_item'): 'UacItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'user_item'): 'UserItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'user_sid_item'): 'UserSidItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'userright_item'): 'UserRightItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'volume_item'): 'VolumeItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'wmi57_item'): 'Wmi57ItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'wmi_item'): 'WmiItemElement',
    ('http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#windows', 'wuaupdatesearcher_item'): 'WuaUpdateSearcherItemElement',
}
