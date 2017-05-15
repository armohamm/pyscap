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
import pytest

import scap.model.scap_source_1_2

logging.basicConfig(level=logging.DEBUG)

def test_importable():
    for m in pkgutil.iter_modules(path=scap.model.scap_source_1_2.__path__):
        importlib.import_module('scap.model.scap_source_1_2.' + m.name, 'scap.model.scap_source_1_2')
