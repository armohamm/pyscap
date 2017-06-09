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
from scap.model.oval_5.defs import *
from scap.model.oval_5.res.DefinitionType import DefinitionType as res_DefinitionType

logger = logging.getLogger(__name__)
class DefinitionType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'tag_name': 'metadata', 'class': 'MetadataType'},
            {'tag_name': 'notes', 'class': 'scap.model.oval_5.NotesType', 'min': 0, 'max': 1},
            {'tag_name': 'criteria', 'class': 'CriteriaType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.DefinitionIdPattern', 'required': True},
            'version': {'type': 'NonNegativeIntegerType', 'required': True},
            'class': {'enum': CLASS_ENUMERATION, 'in': 'class_', 'required': True},
            'deprecated': {'type': 'BooleanType', 'default': False},
        }
    }

    def check(self, content, host, imports, export_names):
        # set up result
        res = res_DefinitionType()
        res.definition_id = self.id
        res.version = self.version
        # TODO res.variable_instance
        res.class_ = self.class_
        res.result = 'not evaluated'

        # TODO save to host for result generation

        if self.deprecated:
            logger.warning('Definition ' + self.id + ' is deprecated, but being used')

        if self.criteria is not None:
            res.criteria = self.criteria.check(content, host, imports, export_names)
            res.result = res.criteria.result

        return res
