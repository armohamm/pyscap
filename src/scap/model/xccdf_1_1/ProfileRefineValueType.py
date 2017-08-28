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

from scap.Model import Model
from . import VALUE_OPERATOR_ENUMERATION
from scap.model.decorators import *
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.StringType import StringType
from .TextType import TextType

logger = logging.getLogger(__name__)

@attribute(local_name='idref', type=NCNameType, required=True)
@attribute(local_name='selector', type=StringType)
@attribute(local_name='operator', enum=VALUE_OPERATOR_ENUMERATION)
@element(local_name='remark', type=TextType, list='remarks', min=0, max=None)
class ProfileRefineValueType(Model):
    def apply(self, item):
        from .ValueType import ValueType
        if not isinstance(item, ValueType):
            raise ValueError('Trying to set value (' + self.idref + ') on an item of the wrong type: ' + item.__class__.__name__)

        if self.selector:
            if self.selector in item.values:
                logger.debug('Refining value ' + item.id + ' selected value to ' + self.selector)
                self.value_selector = self.selector
            elif self.selector in item.defaults:
                logger.debug('Refining value ' + item.id + ' selected default to ' + self.selector)
                self.default_selector = self.selector
            elif self.selector in item.matches:
                logger.debug('Refining value ' + item.id + ' selected match to ' + self.selector)
                self.match_selector = self.selector
            elif self.selector in item.lower_bounds:
                logger.debug('Refining value ' + item.id + ' selected lower bound to ' + self.selector)
                self.lower_bound_selector = self.selector
            elif self.selector in item.upper_bounds:
                logger.debug('Refining value ' + item.id + ' selected upper bound to ' + self.selector)
                self.upper_bound_selector = self.selector
            elif self.selector in item.choices:
                logger.debug('Refining value ' + item.id + ' selected choice to ' + self.selector)
                self.choice_selector = self.selector
            else:
                raise ValueError('Did not find selector ' + self.selector + ' on ' + item.__class__.__name__ + ' ' + item.id)

        if self.operator:
            logger.debug('Refining value ' + item.id + ' operator to ' + self.operator)
            item.operator = self.operator
