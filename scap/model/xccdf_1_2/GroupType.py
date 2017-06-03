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

from scap.model.xccdf_1_2 import *
from scap.model.xccdf_1_2.SelectableItemType import SelectableItemType

logger = logging.getLogger(__name__)
class GroupType(SelectableItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'GroupIDPattern'},
        },
        'elements': [
            {'tag_name': 'Value', 'class': 'ValueType', 'dict': 'values', 'min': 0, 'max': None},
            {'tag_name': 'Group', 'class': 'GroupType', 'dict': 'groups', 'min': 0, 'max': None},
            {'tag_name': 'Rule', 'class': 'RuleType', 'dict': 'rules', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
    }

    def resolve(self, benchmark):
        ### Loading.Resolve.Items

        # For each Item in the Benchmark that has an extends property, resolve
        # it by using the following steps:

        # (1) if the Item is Group, resolve all the enclosed Items,
        for item_id in self.items:
            logger.debug('Resolving item: ' + item_id)
            self.items[item_id].resolve(benchmark)

        # (2) resolve the extended Item,
        if self.extends is None:
            return

        extended = self.get_extended(benchmark)
        extended.resolve(benchmark)

        # (3) prepend the property sequence from the extended Item to the
        # extending Item,
        # (5) remove duplicate properties and apply property overrides, and
        for name in self._model_map['attributes']:
            attr_map = self._model_map['attributes'][name]

            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xmlns, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')
            self.resolve_property(extended, attr_name)

        for element_def in self._model_map['elements']:
            if element_def['tag_name'].endswith('*'):
                continue

            if 'list' in element_def:
                self.resolve_property(extended, element_def['list'])
            elif 'dict' in element_def:
                self.resolve_property(extended, element_def['dict'])
            else:
                if 'in' in element_def:
                    name = element_def['in']
                else:
                    name = element_def['tag_name'].replace('-', '_')
            self.resolve_property(extended, name)

        # (4) if the Item is a Group, assign values for the id properties of
        # Items copied from the extended Group,
        if hasattr(extended, 'items') and len(extended.items) > 0:
            for ext_item in extended.items:
                # make a copy of the item and append to our items
                self.items.append(ext_item.copy())

        # (6) remove the extends property.
        self.extends = None

        # If the directed graph formed by the extends properties includes a
        # loop, then Loading fails.
        # TODO

        # Otherwise, go to the next step: Loading.Resolve.Profiles.

    def process(self, host, benchmark, profile_id):
        super(GroupType, self).process(host, benchmark, profile_id)

        if not self._continue_processing():
            return

        ### Group.Front

        # If the Item is a Group, then process the properties of the Group.
        # TODO

        # TODO check that if this group has a platform identified, that the
        # target system matches

        ### Group.Content

        # If the Item is a Group, then for each Item in the Group’s items
        # property, initiate Item.Process.
        for item_id in self.items:
            self.items[item_id].process(host, benchmark, profile_id)

        # TODO result retention

    def score(self, host, benchmark, profile_id, model_system):
        from scap.model.xccdf_1_1.RuleType import RuleType

        if model_system == 'urn:xccdf:scoring:default':
            ### Score.Group.Init

            # If the node is a Group or the Benchmark, assign a count of 0, a
            # score s of 0.0, and an accumulator a of 0.0.
            count = 0
            score = 0.0
            accumulator = 0.0

            ### Score.Group.Recurse

            # For each selected child of this Group or Benchmark, do the following:
            # (1) compute the count and weighted score for the child using this
            # algorithm,
            # (2) if the child’s count value is not 0, then add the child’s
            # weighted score to this node’s score s, add 1 to this node’s count,
            # and add the child’s weight value to the accumulator a.
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                if not item.selected:
                    continue

                item_score = item.score(host, benchmark, profile_id, model_system)
                if item_score[item_id]['score'] is None:
                    continue

                if item_score[item_id]['count'] != 0:
                    score += item_score[item_id]['score'] * item_score[item_id]['weight']
                    count += 1
                    accumulator += item_score[item_id]['weight']

            ### Score.Group.Normalize

            # Normalize this node’s score: compute s = s / a
            if accumulator == 0.0:
                if score != 0.0:
                    raise ValueError('Got to score normalization with score ' + str(score) + ' / ' + str(accumulator))
                else:
                    score = 0.0
            else:
                score = score / accumulator

            ### Score.Weight

            # Assign the node a weighted score equal to the product of its score
            # and its weight.
            # (done upstream)

            return {self.id: {'model': model_system, 'score': score, 'weight': self.weight, 'count': count}}

        elif model_system == 'urn:xccdf:scoring:flat' \
        or model_system == 'urn:xccdf:scoring:flat-unweighted' \
        or model_system == 'urn:xccdf:scoring:absolute':
            scores = {}
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                if not item.selected:
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host, benchmark, profile_id, model_system))
            return scores

        else:
            raise NotImplementedError('Scoring model ' + model_system + ' is not implemented')
