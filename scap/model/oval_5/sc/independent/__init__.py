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

from scap.model.oval_5.sc import *

TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}family_item': 'FamilyItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}filehash_item': 'FileHashItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}filehash58_item': 'FileHash58ItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}environmentvariable_item': 'EnvironmentVariableItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}environmentvariable58_item': 'EnvironmentVariable58ItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}ldap_item': 'LdapItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}ldap57_item': 'Ldap57ItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}sql_item': 'SqlItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}sql57_item': 'Sql57ItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}textfilecontent_item': 'TextFileContentItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}variable_item': 'VariableItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent}xmlfilecontent_item': 'XmlFileContentItemElement',
}
