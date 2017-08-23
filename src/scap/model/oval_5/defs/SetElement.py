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

from .SetElement import SetElement
from .FilterElement import FilterElement
from .. import SET_OPERATOR_ENUMERATION
from ..ObjectIdPattern import ObjectIdPattern

logger = logging.getLogger(__name__)

@attribute(local_name='set_operator', enum=SET_OPERATOR_ENUMERATION, default='UNION')
@element(local_name='set', list='sets', cls=SetElement, min=0, max=2)
@element(local_name='object_reference', list='object_references', type=ObjectIdPattern, min=0, max=2)
@element(local_name='filter', list='filters', cls=FilterElement, min=0, max=None)
class SetElement(Model):
    def set_operator_complement(self, item_sets):
        ''' include only the elements from the first set that are not found in the second. '''
        items = item_sets[0].copy()
        for s in range(1, len(item_sets)):
            new_items = []
            for i in items:
                if i not in item_sets[s]:
                    new_items.append(i)
            items = new_items
        return items

    def set_operator_intersection(self, item_sets):
        ''' include all of the values common to both sets. '''
        items = item_sets[0].copy()
        for s in range(1, len(item_sets)):
            new_items = []
            for i in items:
                if i in item_sets[s]:
                    new_items.append(i)
            items = new_items
        return items

    def set_operator_union(self, item_sets):
        ''' all values found in either of the sets '''
        items = item_sets[0].copy()
        for s in range(1, len(item_sets)):
            for i in item_sets[s]:
                if i not in items:
                    items.append(i)
        return items

    def evaluate(self, host, content, imports, export_names):
        item_sets = []
        for s in self.set:
            item_sets.append(s.evaluate(host, content, imports, export_names))

        # 1. Identify the OVAL Objects that are part of the set by examining
        # the object_references associated with the set. Each
        # object_reference will refer to an OVAL Object that describes a
        # unique set of collected OVAL Items.
        for o in self.object_references:
            obj = self.args['content'].find_reference(o)
            if not isinstance(obj, self.__class__):
                raise ValueError('Set members must match parent element class: ' + self.__class__.__name__)
            item_sets.append(obj.evaluate(host, content, imports, export_names))

        # 2. For every defined filter (See Section 5.3.3.4.2 filter), apply
        # the associated filter to each OVAL Item.
        for f in self.filters:
            for i in range(len(item_sets)):
                item_sets[i] = f.filter(item_sets[i])

        # 3. Apply the set operator to all OVAL Items remaining in the set.
        if self.set_operator == 'COMPLEMENT':
            items = self.set_operator_complement(item_sets)
        elif self.set_operator == 'INTERSECTION':
            items = self.set_operator_intersection(item_sets)
        elif self.set_operator == 'UNION':
            items = self.set_operator_union(item_sets)
        else:
            raise ValueError('Unknown set_operator: ' + self.set_operator)

        # 4. The resulting OVAL Items will be the unique set of OVAL Items
        # referenced by the OVAL Object that contains the set.

        return items, variable_values
