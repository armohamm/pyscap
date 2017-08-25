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
from scap.model.xs.DateTimeType import DateTimeType

from .ComponentIDPattern import ComponentIDPattern

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=ComponentIDPattern)
@attribute(local_name='timestamp', type=DateTimeType)
@element(namespace='http://checklists.nist.gov/xccdf/1.2', local_name='Benchmark',  into='model', min=0)
@element(namespace='http://scap.nist.gov/schema/ocil/2.0', local_name='ocil', into='model', min=0)
@element(namespace='http://oval.mitre.org/XMLSchema/oval-definitions-5', local_name='oval_definitions', into='model', min=0)
@element(namespace='http://cpe.mitre.org/dictionary/2.0', local_name='cpe-list', into='model', min=0)
@element(namespace='http://checklists.nist.gov/xccdf/1.2', local_name='Tailoring', into='model', min=0)
class ComponentElement(Model):
    pass
