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

import importlib

from scap.Model import Model

def remap_element_package(el):
    if el.tag.startswith('{http://oval.mitre.org/XMLSchema/oval-definitions-5}'):
        schema_versions = el.findall('{http://oval.mitre.org/XMLSchema/oval-definitions-5}generator/{http://oval.mitre.org/XMLSchema/oval-common-5}schema_version')
        schema_versions = [x.text for x in schema_versions]
        if len(schema_versions) < 1:
            raise NotImplementedError('Unable to determine OVAL schema version')

        for schema_version in schema_versions:
            if schema_version == '5.3':
                Model.register_namespace('scap.model.oval.oval_5_3', 'http://oval.mitre.org/XMLSchema/oval-common-5')
                Model.register_namespace('scap.model.oval.oval_5_3.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
                Model.register_namespace('scap.model.oval.oval_5_3.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
                Model.register_namespace('scap.model.oval.oval_5_3.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
                Model.register_namespace('scap.model.oval.oval_5_3.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
                return importlib.import_module('scap.model.oval.oval_5_3.defs')

            if schema_version == '5.11.1':
                Model.register_namespace('scap.model.oval.oval_5_11_1', 'http://oval.mitre.org/XMLSchema/oval-common-5')
                Model.register_namespace('scap.model.oval.oval_5_11_1.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
                Model.register_namespace('scap.model.oval.oval_5_11_1.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
                Model.register_namespace('scap.model.oval.oval_5_11_1.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
                Model.register_namespace('scap.model.oval.oval_5_11_1.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
                return importlib.import_module('scap.model.oval.oval_5_11_1.defs')

        raise NotImplementedError('OVAL schema version is not supported: ' + str(schema_versions))

    raise NotImplementedError('OVAL schema is not supported: ' + el.tag)
