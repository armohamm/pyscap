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

class InitFixture(Model):
    MODEL_MAP = {
        'attributes': {
            'attr': {},
            'in_attr': {'in': 'test_attr'},
            'dash-attr': {},
            'default_attr': {'default': 'Default'},
        },
        'elements': [
            {'tag_name': 'append',  'append': 'append'},
            {'tag_name': 'map',     'map': 'map'},
            {'tag_name': 'in_test', 'in': 'test_in'},
            {'tag_name': 'dash-test'},
            {'tag_name': '{http://jaymes.biz/test2}*', 'in': 'test2_elements'},
            {'tag_name': '*'},
        ]
    }
