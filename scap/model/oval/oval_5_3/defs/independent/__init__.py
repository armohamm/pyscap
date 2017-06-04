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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_test': 'FamilyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_object': 'FamilyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_state': 'FamilyStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filemd5_test': 'FileMd5TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filemd5_object': 'FileMd5ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_state': 'FileMd5StateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_test': 'FileHashTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_object': 'FileHashObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_state': 'FileHashStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_test': 'EnvironmentVariableTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_object': 'EnvironmentVariableObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_state': 'EnvironmentVariableStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_test': 'SqlTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_object': 'SqlObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_state': 'SqlStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_test': 'TextFileContentTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_object': 'TextFileContentObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_state': 'TextFileContentStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}unknown_test': 'UnknownTestElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_test': 'VariableTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_object': 'VariableObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_state': 'VariableStateElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_test': 'XmlFileContentTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_object': 'XmlFileContentObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_state': 'XmlFileContentStateElement',
}

RECURSE_DIRECTION = [
    'none',
    'up',
    'down',
]

ENGINE_ENUMERATION = [
    'access',
    'db2',
    'cache',
    'firebird',
    'firstsql',
    'foxpro',
    'informix',
    'ingres',
    'interbase',
    'lightbase',
    'maxdb',
    'monetdb',
    'mimer',
    'oracle',
    'paradox',
    'pervasive',
    'postgre',
    'sqlbase',
    'sqlite',
    'sqlserver',
    'sybase',
    '',
]

from scap.model.oval.oval_5_3 import FAMILY_ENUMERATION
