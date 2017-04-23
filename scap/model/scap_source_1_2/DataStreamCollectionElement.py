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
class DataStreamCollectionElement(Model):
    MODEL_MAP = {
        'tag_name': 'data-stream-collection',
        'elements': [
            {'xml_namespace': 'http://scap.nist.gov/schema/scap/source/1.2', 'tag_name': 'data-stream', 'max': None, 'class': 'DataStreamElement', 'map': 'data_streams'},
            {'xml_namespace': 'http://scap.nist.gov/schema/scap/source/1.2', 'tag_name': 'component', 'max': None, 'class': 'ComponentElement', 'map': 'components' },
            {'xml_namespace': 'http://scap.nist.gov/schema/scap/source/1.2', 'tag_name': 'extended-component', 'max': None, 'min': 0, 'class': 'ExtendedComponentElement', 'map': 'components' },
            {'xml_namespace': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'max': None, 'min': 0},
        ],
        'attributes': {
            'id': {'required': True, 'type': 'DataStreamCollectionIDPattern'},
            'schematron-version':{'type': 'Token', 'required': True},
        },
    }
