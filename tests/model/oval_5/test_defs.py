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
import pkgutil

import expatriate
import pytest
# import all the classes in the package
import scap.model.oval_5 as pkg
from expatriate.model.Model import Model
from scap.model.oval_5.defs.SetElement import SetElement

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

logging.basicConfig(level=logging.DEBUG)

def test_oval_5_3_detected():
    test_xml = '<oval_definitions ' + \
        'xmlns="http://oval.mitre.org/XMLSchema/oval-definitions-5" ' + \
        'xmlns:oval="http://oval.mitre.org/XMLSchema/oval-common-5" ' + \
        'xmlns:oval-def="http://oval.mitre.org/XMLSchema/oval-definitions-5">' + \
        '<generator>' + \
        '<oval:product_name>The OVAL Repository</oval:product_name>' + \
        '<oval:schema_version>5.3</oval:schema_version>' + \
        '<oval:timestamp>2008-04-10T09:00:10.653-04:00</oval:timestamp>' + \
      '</generator>' + \
      '</oval_definitions>'
    doc = expatriate.Document()
    doc.parse(test_xml)
    model = Model.load(None, doc.root_element)
    from scap.model.oval_5.defs.OvalDefinitionsElement import OvalDefinitionsElement
    assert isinstance(model, OvalDefinitionsElement)

def test_oval_set_complement():
    set_ = SetElement()
    assert set_.set_operator_complement([[1,2,3], [2,4]]) == [1,3]

def test_oval_set_intersection():
    set_ = SetElement()
    assert set_.set_operator_intersection([[1,2,3], [2,4]]) == [2]

def test_oval_set_union():
    set_ = SetElement()
    assert set_.set_operator_union([[1,2,3], [2,4]]) == [1,2,3,4]
