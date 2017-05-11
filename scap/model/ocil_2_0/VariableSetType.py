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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class VariableSetType(Model):
    MODEL_MAP = {
        'elements': [
            #TODO: at least one when_*
            {'tag_name': 'when_pattern', 'list': 'expressions', 'class': 'WhenPatternElement', 'min': 0, 'max': None},
            {'tag_name': 'when_choice', 'list': 'expressions', 'class': 'WhenChoiceElement', 'min': 0, 'max': None},
            {'tag_name': 'when_range', 'list': 'expressions', 'class': 'WhenRangeElement', 'min': 0, 'max': None},
            {'tag_name': 'when_boolean', 'list': 'expressions', 'class': 'WhenBooleanElement', 'min': 0, 'max': None},
        ],
    }
