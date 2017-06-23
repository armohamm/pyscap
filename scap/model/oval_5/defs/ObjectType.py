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

logger = logging.getLogger(__name__)
class ObjectType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'tag_name': 'notes', 'class': 'scap.model.oval_5.NotesType', 'min': 0, 'max': 1},
            {'tag_name': 'set', 'class': 'SetElement', 'min': 0},
            {'tag_name': 'filter', 'list': 'filters', 'class': 'FilterElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.ObjectIdPattern', 'required': True},
            'version': {'type': 'NonNegativeIntegerType', 'required': True},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString'}, # required in the spec, not always seen in the wild
            'deprecated': {'type': 'BooleanType', 'default': False},
        },
    }

    def evaluate(self, host, content, imports, export_names):
        if self.deprecated:
            logger.warning('Deprecated object ' + self.id + ' is being evaluated')

        if self.set is not None:
            results = self.set.evaluate(host, content, imports, export_names)
        else:
            values = {}
            for element_def in self._model_map['elements']:
                if element_def['tag_name'].endswith('*'):
                    # entity object should be defined explicitly
                    raise NotImplementedError('wildcard EntityObjectTypes are unsupported')

                # otherwise, resolve the entity_object
                elif 'list' in element_def:
                    arg_name = element_def['list']
                    values[arg_name] = []
                    lst = getattr(self, arg_name)
                    for v in lst:
                        if isinstance(v, EntityObjectType):
                            values[arg_name].extend(v.resolve_entity_object_values(host, content, imports, export_names))
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
                        values[arg_name] = v.resolve_entity_object_values(host, content, imports, export_names)
                    else:
                        values[arg_name] = [v]

                else:
                    if 'in' in element_def:
                        arg_name = element_def['in']
                    else:
                        arg_name = element_def['tag_name'].replace('-', '_')
                    values[arg_name] = [getattr(self, arg_name)]

            lens = {}
            for arg_name in values.keys():
                lens[arg_name] = len(values[arg_name])
            arg_sets = []
            # TODO

            results = []
            for arg_set in args_sets
            collector = self.load_collector(host, results['args'])
            results['items'] = collector.collect()

        for f in self.filters:
            results['items'] = f.filter_items(results['items'])

        return results

    def load_collector(self, host, args):
        if 'oval_family' not in host.facts:
            if 'cpe' not in host.facts or 'os' not in host.facts['cpe'] or len(host.facts['cpe']['os']) <= 0:
                raise ValueError('Need a defined OS CPE to determine family')

            for cpe in host.facts['cpe']['os']:
                logger.debug('Checking ' + str(cpe) + ' for family match')
                if CPE(part='o', vendor='linux').matches(cpe):
                    host.facts['oval_family'] = 'linux'
                elif CPE(part='o', vendor='microsoft').matches(cpe):
                    host.facts['oval_family'] = 'windows'

            if 'oval_family' not in host.facts:
                raise ValueError('Unable to determine family from discovered CPEs')

        collector_module = self.__module__.replace('ObjectElement', 'Collector').replace(
            'scap.model.oval_5.defs.',
            'scap.collector.' + host.facts['oval_family'] + '.oval_5.')
        collector_class = self.__class__.__name__.replace('ObjectElement', 'Collector')
        mod = importlib.import_module(collector_module, collector_class)
        class_ = getattr(mod, collector_class)
        return class_(host, args)
