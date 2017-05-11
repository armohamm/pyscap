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

class AppendElementFixture(Model):
    MODEL_MAP = {
        'tag_name': 'AppendElementFixture',
        'elements': [
            {'tag_name': 'append_nil', 'append': 'append_nil', 'nillable': True, 'class': 'EnclosedFixture', 'min': 0},
            {'tag_name': 'append_type', 'append': 'append_type', 'type': 'Decimal', 'min': 0},
            {'tag_name': 'append_class', 'append': 'append_class', 'class': 'EnclosedFixture', 'min': 0},
        ],
    }
