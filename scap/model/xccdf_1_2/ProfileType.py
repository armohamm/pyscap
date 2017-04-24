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
class ProfileType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'status', 'class': 'StatusType', 'append': 'statuses', 'min': 0, 'max': None},
            {'tag_name': 'dc-status', 'class': 'DCStatusType', 'append': 'dc_statuses', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'class': 'TextWithSubType', 'append': 'titles', 'min': 1, 'max': None},
            {'tag_name': 'description', 'class': 'HTMLTextWithSubType', 'append': 'descriptions', 'min': 0, 'max': None},
            {'tag_name': 'reference', 'class': 'ReferenceType', 'append': 'references', 'min': 0, 'max': None},
            {'tag_name': 'platform', 'class': 'OverrideableCPE2IDRefType', 'append': 'platforms', 'min': 0, 'max': None},
            {'tag_name': 'select', 'class': 'ProfileSelectType', 'map': 'selects', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-complex-value', 'class': 'ProfileSetComplexValueType', 'map': 'set_complex_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-value', 'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'refine-value', 'class': 'ProfileRefineValueType', 'map': 'refine_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'refine-rule', 'class': 'ProfileRefineRuleType', 'map': 'refine_rules', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'append': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'required': True, 'type': 'ProfileIDPattern'},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
            'abstract': {'type': 'Boolean', 'default': False},
            'note-tag': {'type': 'NCName'},
            'extends': {'notImplemented': True, 'type': 'NCName'},
            'Id': {'type': 'ID'},
        },
    }
