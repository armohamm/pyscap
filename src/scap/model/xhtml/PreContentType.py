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
from scap.Model import Model

logger = logging.getLogger(__name__)
class PreContentType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'a', 'list': '_elements', 'class': 'ATag'},
        ],
    }
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_fontstyle)
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_phrase)
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_special_pre)
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_misc_inline)
    MODEL_MAP['elements'].extend(ELEMENT_GROUP_inline_forms)

    for el in MODEL_MAP['elements']:
        el['min'] = 0
        el['max'] = None
