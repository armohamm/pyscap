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
from scap.model.decorators import *
from .TestResultIdPattern import TestResultIdPattern
from scap.model.xs.DateTimeType import DateTimeType
from scap.model.xs.StringType import StringType
from scap.model.xs.IdType import IdType
from .BenchmarkReferenceType import BenchmarkReferenceType
from .TailoringReferenceType import TailoringReferenceType
from .TextType import TextType
from .IdentityType import IdentityType
from .IdRefType import IdRefType
from .TargetFactsType import TargetFactsType
from .TargetIdRefType import TargetIdRefType
from .Cpe2IdRefType import Cpe2IdRefType
from .ProfileSetValueType import ProfileSetValueType
from .ProfileSetComplexValueType import ProfileSetComplexValueType
from .RuleResultType import RuleResultType
from .ScoreType import ScoreType
from .MetadataType import MetadataType
from .SignatureType import SignatureType

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=TestResultIdPattern)
@attribute(local_name='start-time', type=DateTimeType)
@attribute(local_name='end-time', type=DateTimeType)
@attribute(local_name='test-system', type=StringType)
@attribute(local_name='version', type=StringType)
@attribute(local_name='Id', type=IdType)
@element(local_name='benchmark', cls=BenchmarkReferenceType, min=0, max=1)
@element(local_name='tailoring-file', cls=TailoringReferenceType, min=0, max=1)
@element(local_name='title', cls=TextType, list='titles', min=0, max=None)
@element(local_name='remark', cls=TextType, list='remarks', min=0, max=None)
@element(local_name='organization', type=StringType, list='organizations', min=0, max=None)
@element(local_name='identity', cls=IdentityType, min=0, max=1)
@element(local_name='profile', cls=IdRefType, min=0, max=1)
@element(local_name='target', type=StringType, list='targets', min=1, max=None)
@element(local_name='target-address', type=StringType, list='target_addresses', min=0, max=None)
@element(local_name='target-facts', cls=TargetFactsType, list='target_facts', min=0, max=None)
@element(local_name='target-id-ref', cls=TargetIdRefType, list='target_id_refs', min=0, max=None)
@element(local_name='platform', cls=Cpe2IdRefType, list='platforms', min=0, max=None)
@element(local_name='set-value', cls=ProfileSetValueType, dict='set_values', dict_key='idref', min=0, max=None)
@element(local_name='set-complex-value', cls=ProfileSetComplexValueType, dict='set_values', dict_key='idref', min=0, max=None)
@element(local_name='rule-result', cls=RuleResultType, dict='rule_results', dict_key='idref', min=0, max=None)
@element(local_name='score', cls=ScoreType, list='scores', min=1, max=None)
@element(local_name='metadata', cls=MetadataType, list='metadata', min=0, max=None)
@element(local_name='signature', cls=SignatureType, min=0, max=1)
@element(local_name='*', min=0, max=None)
class TestResultType(Model):
    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
