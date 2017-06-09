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

class MapElementFixture(Model):
    MODEL_MAP = {
        'tag_name': 'MapElementFixture',
        'elements': [
            {'tag_name': 'map_explicit_key', 'dict': 'map_explicit_key', 'key': 'key', 'type': 'StringType', 'min': 0},
            {'tag_name': 'map_implicit_key', 'dict': 'map_implicit_key', 'type': 'StringType', 'min': 0},
            {'tag_name': 'map_value_nil', 'dict': 'map_value_nil', 'nillable': True, 'type': 'StringType', 'min': 0},
            {'tag_name': 'map_value_attr', 'dict': 'map_value_attr', 'value_attr': 'value', 'type': 'StringType', 'min': 0},
            {'tag_name': 'map_value_type', 'dict': 'map_value_type', 'type': 'StringType', 'min': 0},
            {'tag_name': 'map_value_class', 'dict': 'map_value_class', 'class': 'MappableElementFixture', 'min': 0},
        ],
    }
