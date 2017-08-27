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
from scap.model.xs.TokenType import TokenType

from .ComponentElement import ComponentElement
from .DataStreamCollectionIDPattern import DataStreamCollectionIDPattern
from .DataStreamElement import DataStreamElement
from .ExtendedComponentElement import ExtendedComponentElement

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=DataStreamCollectionIDPattern)
@attribute(local_name='schematron-version', type=TokenType, required=True)
@element(local_name='data-stream', max=None, cls=DataStreamElement, dict='data_streams')
@element(local_name='component', max=None, cls=ComponentElement, dict='components' )
@element(local_name='extended-component', max=None, min=0, cls=ExtendedComponentElement, dict='components' )
@element(namespace='http://www.w3.org/2000/09/xmldsig#', local_name='Signature', max=None, min=0)
class DataStreamCollectionElement(Model):
    pass
