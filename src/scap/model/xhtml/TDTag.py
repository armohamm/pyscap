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

from scap.model.xhtml import *
from scap.model.xhtml.FlowType import FlowType

logger = logging.getLogger(__name__)
class TDTag(FlowType):
    MODEL_MAP = {
        'attributes': {
            'abbr': {'type': 'TextType'},
            'axis': {'type': 'StringType'},
            'headers': {'type': 'IDREFS'},
            'scope': {'enum': SCOPE_ENUMERATION},
            'rowspan': {'type': 'NumberType', 'default': 1},
            'colspan': {'type': 'NumberType', 'default': 1},
        },
    }
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_attrs)
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_cellhalign)
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_cellvalign)
