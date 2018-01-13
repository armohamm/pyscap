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

from . import VALUE_TYPE_ENUMERATION
from . import VALUE_OPERATOR_ENUMERATION
from . import INTERFACE_HINT_ENUMERATION
from .ItemType import ItemType
from scap.model.decorators import *
from .ValueIdPattern import ValueIdPattern
from scap.model.xs.BooleanType import BooleanType
from .SelStringType import SelStringType
from .SelComplexValueType import SelComplexValueType
from .SelNumType import SelNumType
from .SelChoicesType import SelChoicesType
from .UriRefType import UriRefType
from .SignatureType import SignatureType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=ValueIdPattern, required=True)
@attribute(local_name='type', enum=VALUE_TYPE_ENUMERATION, default='string')
@attribute(local_name='operator', enum=VALUE_OPERATOR_ENUMERATION, default='equals')
@attribute(local_name='interactive', type=BooleanType)
@attribute(local_name='interfaceHint', enum=INTERFACE_HINT_ENUMERATION)
@element(local_name='value', cls=SelStringType, dict='values', dict_key='selector', min=0, max=None)
@element(local_name='complex-value', cls=SelComplexValueType, dict='complex_values', dict_key='selector', min=0, max=None)
@element(local_name='default', cls=SelStringType, min=0, max=None, dict='defaults', dict_key='selector')
@element(local_name='complex-default', cls=SelComplexValueType, min=0, max=None, dict='complex_defaults', dict_key='selector')
@element(local_name='match', cls=SelStringType, dict='matches', dict_key='selector', min=0, max=None)
@element(local_name='lower-bound', cls=SelNumType, dict='lower_bounds', dict_key='selector', min=0, max=None)
@element(local_name='upper-bound', cls=SelNumType, dict='upper_bounds', dict_key='selector', min=0, max=None)
@element(local_name='choices', cls=SelChoicesType, dict='choices', dict_key='selector', min=0, max=None)
@element(local_name='source', cls=UriRefType, list='sources', min=0, max=None)
@element(local_name='signature', cls=SignatureType, min=0, max=None)
class ValueType(ItemType):
    def __init__(self, *args, **kwargs):
        super(ValueType, self).__init__(*args, **kwargs)

        self.default = None
        self.value = None
        self.match = None
        self.lower_bound = None
        self.upper_bound = None
        self.choices = None

        self.default_selector = None
        self.value_selector = None
        self.match_selector = None
        self.lower_bound_selector = None
        self.upper_bound_selector = None
        self.choices_selector = None

    def process(self, host, benchmark, profile_id):
        ### Value.Content

        # If the Item is a Value, then process the properties of the Value.

        # default
        if self.default_selector is not None and self.default_selector in self.defaults:
            self.default = self.defaults[self.default_selector]
        elif '' in self.defaults:
            self.default = self.defaults['']

        # value
        if self.value_selector is not None and self.value_selector in self.values:
            self.value = self.values[self.value_selector]
        elif self.default is not None:
            self.value = self.default
        elif '' in self.values:
            self.value = self.values['']

        # match
        if self.match_selector is not None and self.match_selector in self.matches:
            self.match = self.matches[self.match_selector]
        elif '' in self.matches:
            self.match = self.matches['']

        # lower_bound
        if self.lower_bound_selector is not None and self.lower_bound_selector in self.lower_bounds:
            self.lower_bound = self.lower_bounds[self.lower_bound_selector]
        elif '' in self.lower_bounds:
            self.lower_bound = self.lower_bounds['']

        # upper_bound
        if self.upper_bound_selector is not None and self.upper_bound_selector in self.upper_bounds:
            self.upper_bound = self.upper_bounds[self.upper_bound_selector]
        elif '' in self.upper_bounds:
            self.upper_bound = self.upper_bounds['']

        # choices
        if self.choices_selector is not None and self.choices_selector in self.choice_selections:
            self.choices = self.choice_selections[self.choice_selector]
        elif '' in self.choice_selections:
            self.choices = self.choice_selections['']

        host.facts['checklist'][benchmark.id]['profile'][profile_id]['value'][self.id] = {
            'default': self.default,
            'value': self.value,
            'match': self.match,
            'lower_bound': self.lower_bound,
            'upper_bound': self.upper_bound,
            'choices': self.choices,
        }
