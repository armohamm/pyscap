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
from scap.model.oval_5 import *
from scap.model.oval_def_5 import *

logger = logging.getLogger(__name__)
class CriteriaType(Model):
    MODEL_MAP = {
        'elements': [
            # TODO minOccurs="1" maxOccurs="unbounded" of the following:
            {'tag_name': 'criteria', 'list': 'criteria', 'class': 'CriteriaType', 'min': 0, 'max': None},
            {'tag_name': 'criterion', 'list': 'criteria', 'class': 'CriterionType', 'min': 0, 'max': None},
            {'tag_name': 'extend_definition', 'list': 'criteria', 'class': 'ExtendDefinitionType', 'min': 0, 'max': None},
        ],
        'attributes': {
            'applicability_check': {'type': 'Boolean'},
            'operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'negate': {'type': 'Boolean', 'default': False},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString'},
        }
    }
