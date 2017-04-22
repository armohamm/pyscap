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
TEST_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable_test', 'map': 'tests', 'class': 'EnvironmentVariableTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable58_test', 'map': 'tests', 'class': 'EnvironmentVariable58TestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'family_test', 'map': 'tests', 'class': 'FamilyTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash58_test', 'map': 'tests', 'class': 'FileHash58TestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash_test', 'map': 'tests', 'class': 'FileHashTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap57_test', 'map': 'tests', 'class': 'LDAP57TestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap_test', 'map': 'tests', 'class': 'LDAPTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql57_test', 'map': 'tests', 'class': 'SQL57TestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql_test', 'map': 'tests', 'class': 'SQLTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent54_test', 'map': 'tests', 'class': 'TextFileContent54TestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent_test', 'map': 'tests', 'class': 'TextFileContentTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'unknown_test', 'map': 'tests', 'class': 'UnknownTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'variable_test', 'map': 'tests', 'class': 'VariableTestElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'xmlfilecontent_test', 'map': 'tests', 'class': 'XMLFileContentTestElement', 'min': 0, 'max': None},
}
OBJECT_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable_object', 'map': 'objects', 'class': 'EnvironmentVariableObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable58_object', 'map': 'objects', 'class': 'EnvironmentVariable58ObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'family_object', 'map': 'objects', 'class': 'FamilyObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash58_object', 'map': 'objects', 'class': 'FileHash58ObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash_object', 'map': 'objects', 'class': 'FileHashObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap57_object', 'map': 'objects', 'class': 'LDAP57ObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap_object', 'map': 'objects', 'class': 'LDAPObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql57_object', 'map': 'objects', 'class': 'SQL57ObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql_object', 'map': 'objects', 'class': 'SQLObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent54_object', 'map': 'objects', 'class': 'TextFileContent54ObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent_object', 'map': 'objects', 'class': 'TextFileContentObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'variable_object', 'map': 'objects', 'class': 'VariableObjectElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'xmlfilecontent_object', 'map': 'objects', 'class': 'XMLFileContentObjectElement', 'min': 0, 'max': None},}
STATE_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable_state', 'map': 'states', 'class': 'EnvironmentVariableStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'environmentvariable58_state', 'map': 'states', 'class': 'EnvironmentVariable58StateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'family_state', 'map': 'states', 'class': 'FamilyStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash58_state', 'map': 'states', 'class': 'FileHash58StateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'filehash_state', 'map': 'states', 'class': 'FileHashStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap57_state', 'map': 'states', 'class': 'LDAP57StateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'ldap_state', 'map': 'states', 'class': 'LDAPStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql57_state', 'map': 'states', 'class': 'SQL57StateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'sql_state', 'map': 'states', 'class': 'SQLStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent54_state', 'map': 'states', 'class': 'TextFileContent54StateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'textfilecontent_state', 'map': 'states', 'class': 'TextFileContentStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'variable_state', 'map': 'states', 'class': 'VariableStateElement', 'min': 0, 'max': None},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent', 'tag_name': 'xmlfilecontent_state', 'map': 'states', 'class': 'XMLFileContentStateElement', 'min': 0, 'max': None},}
