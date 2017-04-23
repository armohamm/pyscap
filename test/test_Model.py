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

import pytest, logging
from scap.Model import Model, UnsupportedNamespaceException

logging.basicConfig(level=logging.DEBUG)

def test_parse_tag_supported():
    assert Model.parse_tag('{http://www.w3.org/XML/1998/namespace}test') == ('http://www.w3.org/XML/1998/namespace', 'test')
    assert Model.parse_tag('test') == (None, 'test')

def test_parse_tag_unsupported():
    with pytest.raises(UnsupportedNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')
