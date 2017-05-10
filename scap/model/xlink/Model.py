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

from scap.Model import scapModel
import logging

logger = logging.getLogger(__name__)
class Model(scapModel):
    MODEL_MAP = {
        'attributes': {
            '{http://www.w3.org/1999/xlink}type': {'enum': ['simple', 'extended', 'locator', 'arc', 'resource', 'title', 'none']},
            '{http://www.w3.org/1999/xlink}href': {'type': 'AnyURI'},
            '{http://www.w3.org/1999/xlink}role': {'type': 'AnyURI'}, # min length = 1
            '{http://www.w3.org/1999/xlink}arcrole': {'type': 'AnyURI'}, # min length = 1
            '{http://www.w3.org/1999/xlink}title': {'type': 'String'},
            '{http://www.w3.org/1999/xlink}show': {'enum': ['new', 'replace', 'embed', 'other', 'none']},
            '{http://www.w3.org/1999/xlink}actuate': {'enum': ['onLoad', 'onRequest', 'other', 'none']},
            '{http://www.w3.org/1999/xlink}label': {'type': 'NCName'},
            '{http://www.w3.org/1999/xlink}from': {'type': 'NCName'},
            '{http://www.w3.org/1999/xlink}to': {'type': 'NCName'},
        }
    }
