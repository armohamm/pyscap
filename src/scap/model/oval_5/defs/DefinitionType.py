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

from .MetadataType import MetadataType
from .CriteriaType import CriteriaType
from ..NotesType import NotesType
from .. import DefinitionIdPattern
from .. import CLASS_ENUMERATION
from ..res.DefinitionType import DefinitionType as res_DefinitionType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=scap.model.oval_5.DefinitionIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='class', enum=CLASS_ENUMERATION, into='class_', required=True)
@attribute(local_name='deprecated', type=BooleanType, default=False)
@element(local_name='metadata', cls=MetadataType)
@element(local_name='notes', cls=NotesType, min=0, max=1)
@element(local_name='criteria', cls=CriteriaType, min=0, max=1)
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', min=0, max=1)
class DefinitionType(Model):
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
