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
import logging
import pytest
import pkgutil
import xml.etree.ElementTree as ET

from scap.Model import Model

# import all the classes in the package
import scap.model.oval_5.defs.independent as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
Model.register_namespace('scap.model.oval_5.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
Model.register_namespace('scap.model.oval_5.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
Model.register_namespace('scap.model.oval_5.defs.unix', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#unix')

logging.basicConfig(level=logging.DEBUG)

def test_EntityObjectEngineType_parse():
    assert EntityObjectEngineType().parse_value('ingres') == 'ingres'

def test_EntityObjectHashTypeType_parse():
    assert EntityObjectHashTypeType().parse_value('SHA-256') == 'SHA-256'

def test_EntityStateLdaptypeType_parse():
    assert EntityStateLdaptypeType().parse_value('LDAPTYPE_CERTIFICATE') == 'LDAPTYPE_CERTIFICATE'

def test_EntityStateVariableRefType_parse():
    assert EntityStateVariableRefType().parse_value('oval:biz.jaymes:var:12345') == 'oval:biz.jaymes:var:12345'

def test_EntityStateWindowsViewType_parse():
    assert EntityStateWindowsViewType().parse_value('32_bit') == '32_bit'
