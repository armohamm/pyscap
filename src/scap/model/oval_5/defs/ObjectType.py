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

from .EntityObjectType import EntityObjectType
from .SetElement import SetElement
from .FilterElement import FilterElement
from ..ObjectIdPattern import ObjectIdPattern
from ..NonEmptyString  import NonEmptyString
from ..NotesType import NotesType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@attribute(local_name='id', type=ObjectIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='comment', type=NonEmptyString) # required in the spec, not always seen in the wild
@attribute(local_name='deprecated', type=BooleanType, default=False)
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', min=0, max=1)
@element(local_name='notes', cls=NotesType, min=0, max=1)
@element(local_name='set', cls=SetElement, min=0)
@element(local_name='filter', list='filters', cls=FilterElement, min=0, max=None)
class ObjectType(Model):
    def _iter_arg(self, arg, values, counters, arg_order):
        argsets = []
        i = arg_order.index(arg)
        logger.debug('Iterating arg ' + arg)
        for j in range(len(values[arg])):
            logger.debug('Arg ' + arg + ' iteration ' + str(values[arg][j]))
            counters[arg] = j
            if i == len(arg_order) - 1:
                argsets.append({a: values[a][counters[a]] for a in arg_order})
            else:
                argsets.extend(self._iter_arg(arg_order[i+1], values, counters, arg_order))
        return argsets

    def evaluate(self, host, content, imports, export_names):
        if self.deprecated:
            logger.warning('Deprecated object ' + self.id + ' is being evaluated')

        items = []
        if self.set is not None:
            items = self.set.evaluate(host, content, imports, export_names)
        else:
            values = {}
            value_datatypes = {}
            value_operations = {}
            value_masks = {}
            for element_def in self._model_map['elements']:
                if element_def['tag_name'].endswith('*'):
                    # entity object should be defined explicitly
                    raise NotImplementedError('wildcard EntityObjectTypes are unsupported')

                if element_def['tag_name'] in ('set', 'filter', 'notes', 'Signature'):
                    # skip object elements
                    continue

                # otherwise, resolve the entity_object
                elif 'list' in element_def:
                    arg_name = element_def['list']
                    values[arg_name] = []
                    lst = getattr(self, arg_name)
                    for v in lst:
                        if isinstance(v, EntityObjectType):
                            r = v.resolve_values(host, content, imports, export_names)
                            vals = r[0]
                            value_datatypes[arg_name] = r[1]
                            value_operations[arg_name] = r[2]
                            value_masks[arg_name] = r[3]

                            values[arg_name].extend(vals)
                        else:
                            values[arg_name].append(v)

                elif 'dict' in element_def:
                    raise NotImplementedError('dict EntityObjectTypes are not supported')

                elif 'class' in element_def:
                    if 'in' in element_def:
                        arg_name = element_def['in']
                    else:
                        arg_name = element_def['tag_name'].replace('-', '_')

                    v = getattr(self, arg_name)
                    if isinstance(v, EntityObjectType):
                        r = v.resolve_values(host, content, imports, export_names)
                        values[arg_name] = r[0]
                        value_datatypes[arg_name] = r[1]
                        value_operations[arg_name] = r[2]
                        value_masks[arg_name] = r[3]
                    else:
                        values[arg_name] = [v]

                else:
                    if 'in' in element_def:
                        arg_name = element_def['in']
                    else:
                        arg_name = element_def['tag_name'].replace('-', '_')
                    values[arg_name] = [getattr(self, arg_name)]

            logger.debug('Values resolved to: ' + str(values))

            arg_order = list(values.keys())
            logger.debug('arg_order: ' + str(arg_order))
            counters = {x: 0 for x in values.keys()}
            arg_sets = self._iter_arg(arg_order[0], values, counters, arg_order)
            logger.debug('arg_sets: ' + str(arg_sets))

            for args in arg_sets:
                logger.debug('Collecting items for args ' + str(args))
                args['value_datatypes'] = value_datatypes
                args['value_operations'] = value_operations
                args['value_masks'] = value_masks
                items.extend(self.collect_items_for_args(host, args))

        for f in self.filters:
            items = f.filter(items)

        return items

    def collect_items_for_args(self, host, args):
        raise NotImplementedError(self.__class__.__name__ + ' does not define collect_items_for_args')
