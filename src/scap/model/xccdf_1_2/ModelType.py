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
class ModelType(Model):
    MODEL_MAP = {
        'attributes': {
            'system': {'required': True, 'type': 'AnyUriType'},
        },
        'elements': [
            {'tag_name': 'param', 'class': 'ParamType', 'dict': 'params', 'key': 'name', 'min': 0, 'max': None},
        ],
    }

    def score(self, host, benchmark, profile_id):
        from scap.model.xccdf_1_1.GroupType import GroupType
        from scap.model.xccdf_1_1.RuleType import RuleType

        if self.system == 'urn:xccdf:scoring:default':
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
            for item_id in benchmark.items:
                item = benchmark.items[item_id]

                if (
                    not isinstance(item, GroupType)
                    and not isinstance(item, RuleType)
                ):
                    continue

                if not item.selected:
                    continue

                item_score = item.score(host, benchmark, profile_id, self.system)
                if item_score[item_id]['score'] is None:
                    continue

                if item_score[item_id]['count'] != 0:
                    score += item_score[item_id]['score'] * item_score[item_id]['weight']
                    count += 1
                    accumulator += item_score[item_id]['weight']

            ### Score.Group.Normalize

            # Normalize this node’s score: compute s = s / a.
            if accumulator == 0.0:
                if score != 0.0:
                    raise ValueError('Got to score normalization with score ' + str(score) + ' / ' + str(accumulator))
                else:
                    score = 0.0
            else:
                score = score / accumulator

            logger.debug(self.system + ' score: ' + str(score))
            host.facts['checklist'][benchmark.id]['profile'][profile_id]['scores'].append({'score': score, 'system': self.system})

        elif self.system == 'urn:xccdf:scoring:flat':
            scores = {}
            for item_id in benchmark.items:
                item = benchmark.items[item_id]

                if (
                    not isinstance(item, GroupType)
                    and not isinstance(item, RuleType)
                ):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host, benchmark, profile_id, self.system))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += scores[rule_id]['weight']
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += scores[rule_id]['weight']

            logger.debug(self.system + ' score: ' + str(score) + ' / ' + str(max_score))
            host.facts['checklist'][benchmark.id]['profile'][profile_id]['scores'].append({'score': score, 'max_score': max_score, 'system': self.system})

        elif self.system == 'urn:xccdf:scoring:flat-unweighted':
            scores = {}
            for item_id in benchmark.items:
                item = benchmark.items[item_id]

                if (
                    not isinstance(item, GroupType)
                    and not isinstance(item, RuleType)
                ):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host, benchmark, profile_id, self.system))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += 1.0
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += 1.0

            logger.debug(self.system + ' score: ' + str(score) + ' / ' + str(max_score))
            host.facts['checklist'][benchmark.id]['profile'][profile_id]['scores'].append({'score': score, 'max_score': max_score, 'system': self.system})

        elif self.system == 'urn:xccdf:scoring:absolute':
            scores = {}
            for item_id in benchmark.items:
                item = benchmark.items[item_id]

                if (
                    not isinstance(item, GroupType)
                    and not isinstance(item, RuleType)
                ):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host, benchmark, profile_id, self.system))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += scores[rule_id]['weight']
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += scores[rule_id]['weight']

            if score == max_score:
                score = 1.0
            else:
                score = 0.0

            logger.debug(self.system + ' score: ' + str(score))
            host.facts['checklist'][benchmark.id]['profile'][profile_id]['scores'].append({'score': score, 'system': self.system})

        else:
            raise NotImplementedError('Scoring model ' + self.system + ' is not implemented')
