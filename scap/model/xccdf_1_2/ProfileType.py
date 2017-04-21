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
        'attributes': {
            'id': {'required': True, 'type': 'ProfileIDPattern'},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
            'abstract': {'type': 'Boolean', 'default': False},
            'note-tag': {'type': 'NCName'},
            'extends': {'notImplemented': True, 'type': 'NCName'},
            'Id': {'type': 'ID'},
        },
        'element_order': [],
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}status': {'class': 'StatusType', 'append': 'statuses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}dc-status': {'class': 'DCStatusType', 'append': 'dc_statuses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}version': {'class': 'VersionType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.2}title': {'class': 'TextWithSubType', 'append': 'titles', 'min': 1, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}description': {'class': 'HTMLTextWithSubType', 'append': 'descriptions', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}reference': {'class': 'ReferenceType', 'append': 'references', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}platform': {'class': 'OverrideableCPE2IDRefType', 'append': 'platforms', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.2}select': {'class': 'ProfileSelectType', 'map': 'selects', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}set-complex-value': {'class': 'ProfileSetComplexValueType', 'map': 'set_complex_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}set-value': {'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}refine-value': {'class': 'ProfileRefineValueType', 'map': 'refine_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}refine-rule': {'class': 'ProfileRefineRuleType', 'map': 'refine_rules', 'key': 'idref', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.2}metadata': {'class': 'MetadataType', 'append': 'metadata', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}signature': {'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }
