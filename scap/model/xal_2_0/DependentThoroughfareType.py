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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class DependentThoroughfareType(Model):
    MODEL_MAP = {
        'tag_name': 'DependentThoroughfare',
        'elements': [
            {'tag_name': 'AddressLine', 'append': 'address_lines', 'class': 'AddressLineType'},
            {'tag_name': 'ThoroughfarePreDirection', 'in': 'thoroughfare_pre_direction', 'class': 'ThoroughfarePreDirectionType'},
            {'tag_name': 'ThoroughfareLeadingType', 'in': 'thoroughfare_leading_type', 'class': 'ThoroughfareLeadingTypeType'},
            {'tag_name': 'ThoroughfareName', 'append': 'thoroughfare_names', 'class': 'ThoroughfareNameType'},
            {'tag_name': 'ThoroughfareTrailingType', 'in': 'thoroughfare_trailing_type', 'class': 'ThoroughfareTrailingTypeType'},
            {'tag_name': 'ThoroughfarePostDirection', 'in': 'thoroughfare_post_direction', 'class': 'ThoroughfarePostDirectionType'},
            {'tag_name': '*'},
        ],
        'attributes': {
            'Type': {},
            '*': {},
        }
    }
