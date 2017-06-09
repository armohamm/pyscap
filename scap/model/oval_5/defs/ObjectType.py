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

logger = logging.getLogger(__name__)
class ObjectType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'tag_name': 'notes', 'class': 'scap.model.oval_5.NotesType', 'min': 0, 'max': 1},
            {'tag_name': 'set', 'class': 'scap.model.oval_5.defs.SetElement', 'min': 0},
            {'tag_name': 'filter', 'class': 'FilterElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.ObjectIdPattern', 'required': True},
            'version': {'type': 'NonNegativeInteger', 'required': True},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString'}, # required in the spec
            'deprecated': {'type': 'BooleanType', 'default': False},
        },
    }

    def resolve(self, content, host, imports, export_names):
        raise NotImplementedError('resolve is not implemented')
