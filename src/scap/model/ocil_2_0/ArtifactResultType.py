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

logger = logging.getLogger(__name__)

@attribute(local_name='artifact_ref', type='ArtifactIDPattern', required=True)
@attribute(local_name='timestamp', type='DateTimeType', required=True)
@element(local_name='text_artifact_value', cls='TextArtifactValueElement', min=0, max=1)
@element(local_name='binary_artifact_value', cls='BinaryArtifactValueElement', min=0, max=1)
@element(local_name='reference_artifact_value', cls='ReferenceArtifactValueElement', min=0, max=1)
@element(local_name='provider', type='ProviderValuePattern', min=1, max=1)
@element(local_name='submitter', cls='UserType', min=1, max=1)
class ArtifactResultType(Model):
    pass
