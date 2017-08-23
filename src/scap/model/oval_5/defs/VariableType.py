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

import logging

from scap.model.decorators import *
from scap.Model import Model
from scap.model.xs.NonNegativeIntegerType import NonNegativeIntegerType
from scap.model.xs.BooleanType import BooleanType

from .NotesType import NotesType
from .. import SIMPLE_DATATYPE_ENUMERATION
from ..VariableIdPattern import VariableIdPattern
from ..NonEmptyString import NonEmptyString

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=VariableIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='datatype', enum=SIMPLE_DATATYPE_ENUMERATION, required=True)
@attribute(local_name='comment', type=NonEmptyString) # required in the spec
@attribute(local_name='deprecated', type=BooleanType, default=False)
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', min=0, max=1)
@element(namespace='http://oval.mitre.org/XMLSchema/oval-common-5', local_name='notes', cls=NotesType, min=0, max=1)
class VariableType(Model):
    def resolve_values(self, content, imports, export_names, var_check):
        raise NotImplementedError('not implemented')
        # values, datatype, operation, mask
