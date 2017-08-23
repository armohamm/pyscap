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
from scap.model.xs.BooleanType import BooleanType
from scap.model.xs.FloatType import FloatType
from scap.model.xs.HexBinaryType import HexBinaryType
from scap.model.xs.IntegerType import IntegerType
from scap.model.xs.StringType import StringType

from .EntityObjectFieldType import EntityObjectFieldType
from .. import CHECK_ENUMERATION
from .. import DATATYPE_ENUMERATION
from .. import EXISTENCE_ENUMERATION
from .. import OPERATION_ENUMERATION
from ..VariableIdPattern import VariableIdPattern

logger = logging.getLogger(__name__)

@attribute(local_name='datatype', enum=DATATYPE_ENUMERATION, default='string')
@attribute(local_name='operation', enum=OPERATION_ENUMERATION, default='equals')
@attribute(local_name='mask', type=BooleanType, default=False)
@attribute(local_name='var_ref', type=VariableIdPattern)
@attribute(local_name='var_check', enum=CHECK_ENUMERATION)
@attribute(local_name='entity_check', enum=CHECK_ENUMERATION, default='all')
@attribute(local_name='check_existence', enum=EXISTENCE_ENUMERATION, default='at_least_one_exists')
@element(local_name='field', list='fields', cls=EntityObjectFieldType, min=0, max=None)
class EntityStateType(Model):
    def __str__(self):
        return super(EntityStateType, self).__str__() + ' = ' + str(self.get_value())

    DATATYPE_CLASS_MAPPING = {
        'binary': HexBinaryType,
        'boolean': BooleanType,
        'evr_string': StringType,
        'debian_evr_string': StringType,
        'fileset_revision': StringType,
        'float': FloatType,
        'ios_version': StringType,
        'int': IntegerType,
        'ipv4_address': StringType,
        'ipv6_address': StringType,
        'string': StringType,
        'version': StringType,
    }

    def from_xml(self, parent, sub_el):
        super(EntityStateType, self).from_xml(parent, sub_el)

        if sub_el.text is not None:
            if sub_el.text == '':
                self.set_value('')
            elif self.datatype in EntityStateType.DATATYPE_CLASS_MAPPING:
                self.set_value(EntityStateType.DATATYPE_CLASS_MAPPING[self.datatype]().parse_value(sub_el.text))

                # allow StringType-like enums & patterns
                if hasattr(self, 'get_value_enum') and self.get_value() not in self.get_value_enum():
                    raise ValueError(self.__class__.__name__ + ' requires a value in ' + str(self.get_value_enum()))
                if hasattr(self, 'get_value_pattern') and not re.fullmatch(self.get_value_pattern(), self.get_value()):
                    raise ValueError(self.__class__.__name__ + ' requires a value matching ' + self.get_value_pattern())

    def to_xml(self):
        el = super(EntityStateType, self).to_xml()
        if self.datatype in EntityStateType.DATATYPE_CLASS_MAPPING:
            el.text = EntityStateType.DATATYPE_CLASS_MAPPING[self.datatype]().produce_value(self.get_value())

        return el
