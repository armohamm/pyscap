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
import uuid

from scap.Model import Model
from scap.model.decorators import *
from scap.model.xs.DateTimeType import DateTimeType
from scap.model.xs.IdType import IdType
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.StringType import StringType

from .BenchmarkReferenceType import BenchmarkReferenceType
from .IdentityType import IdentityType
from .IdrefType import IdrefType
from .ProfileSetValueType import ProfileSetValueType
from .RuleResultType import RuleResultType
from .ScoreType import ScoreType
from .SignatureType import SignatureType
from .TargetFactsType import TargetFactsType
from .TextType import TextType
from .UriIdrefType import UriIdrefType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=NCNameType, required=True)
@attribute(local_name='start-time', type=DateTimeType)
@attribute(local_name='end-time', type=DateTimeType, required=True)
@attribute(local_name='test-system', type=StringType)
@attribute(local_name='version', type=StringType)
@attribute(local_name='Id', type=IdType)
@element(local_name='benchmark', cls=BenchmarkReferenceType, min=0, max=1)
@element(local_name='title', list='titles', cls=TextType, min=0, max=None)
@element(local_name='remark', list='remarks', cls=TextType, min=0, max=None)
@element(local_name='organization', list='organizations', type=StringType, min=0, max=None)
@element(local_name='identity', cls=IdentityType, min=0, max=1)
@element(local_name='profile', cls=IdrefType, min=0, max=1)
@element(local_name='target', list='targets', type=StringType, min=1, max=None)
@element(local_name='target-address', list='target_addresses', type=StringType, min=0, max=None)
@element(local_name='target-facts', cls=TargetFactsType, min=0, max=1)
@element(local_name='platform', list='platforms', cls=UriIdrefType, min=0, max=None)
@element(local_name='set-value', dict='set_values', cls=ProfileSetValueType, key='idref', min=0, max=None)
@element(local_name='rule-result', dict='rule_results', cls=RuleResultType, key='idref', min=0, max=None)
@element(local_name='score', list='scores', cls=ScoreType, min=1, max=None)
@element(local_name='signature', cls=SignatureType, min=0, max=1)
class TestResultType(Model):
    @staticmethod
    def generate_id():
        return 'xccdf_biz.jaymes_testresult_' + uuid.uuid4().hex
