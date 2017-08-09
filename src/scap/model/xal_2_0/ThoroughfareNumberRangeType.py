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
class ThoroughfareNumberRangeType(Model):
    MODEL_MAP = {
        'tag_name': 'ThoroughfareNumberRange',
        'elements': [
            {'tag_name': 'AddressLine', 'list': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'ThoroughfareNumberFrom', 'in': 'thoroughfare_number_from', 'class': 'ThoroughfareNumberFromType'},
            {'tag_name': 'ThoroughfareNumberTo', 'in': 'thoroughfare_number_to', 'class': 'ThoroughfareNumberToType'},
        ],
        'attributes': {
            'RangeType': {'enum': ['Odd', 'Even']},
            'Indicator': {},
            'Separator': {},
            'IndicatorOccurrence': {'enum': ['Before', 'After']},
            'NumberRangeOccurrence': {'enum': ['BeforeName', 'AfterName', 'BeforeType', 'AfterType']},
            'Type': {},
            'Code': {}, # from grPostal
            '*': {},
        },
    }
