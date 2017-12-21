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
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'dnscache_test'): 'DnsCacheTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'dnscache_object'): 'DnsCacheObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'dnscache_state'): 'DnsCacheStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'file_test'): 'FileTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'file_object'): 'FileObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'file_state'): 'FileStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'fileextendedattribute_test'): 'FileExtendedAttributeTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'fileextendedattribute_object'): 'FileExtendedAttributeObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'fileextendedattribute_state'): 'FileExtendedAttributeStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'gconf_test'): 'GconfTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'gconf_object'): 'GconfObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'gconf_state'): 'GconfStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'inetd_test'): 'InetdTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'inetd_object'): 'InetdObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'inetd_state'): 'InetdStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'interface_test'): 'InterfaceTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'interface_object'): 'InterfaceObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'interface_state'): 'InterfaceStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'password_test'): 'PasswordTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'password_object'): 'PasswordObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'password_state'): 'PasswordStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process_test'): 'ProcessTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process_object'): 'ProcessObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process_state'): 'ProcessStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process58_test'): 'Process58TestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process58_object'): 'Process58ObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'process58_state'): 'Process58StateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'routingtable_test'): 'RoutingTableTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'routingtable_object'): 'RoutingTableObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'routingtable_state'): 'RoutingTableStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'runlevel_test'): 'RunLevelTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'runlevel_object'): 'RunLevelObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'runlevel_state'): 'RunLevelStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sccs_test'): 'SccsTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sccs_object'): 'SccsObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sccs_state'): 'SccsStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'shadow_test'): 'ShadowTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'shadow_object'): 'ShadowObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'shadow_state'): 'ShadowStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'symlink_test'): 'SymlinkTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'symlink_object'): 'SymlinkObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'symlink_state'): 'SymlinkStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sysctl_test'): 'SysctlTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sysctl_object'): 'SysctlObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'sysctl_state'): 'SysctlStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'uname_test'): 'UnameTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'uname_object'): 'UnameObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'uname_state'): 'UnameStateElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'xinetd_test'): 'XinetdTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'xinetd_object'): 'XinetdObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#unix', 'xinetd_state'): 'XinetdStateElement',
}
