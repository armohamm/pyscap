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

from scap.model.xccdf_1_2.SelectableItemType import SelectableItemType
from scap.model.xccdf_1_2.RoleEnumeration import ROLE_ENUMERATION
from scap.model.xccdf_1_2.SeverityEnumeration import SEVERITY_ENUMERATION
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class RuleType(SelectableItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'RuleIDPattern'},
            'role': {'enum': ROLE_ENUMERATION, 'default': 'full'},
            'severity': {'enum': SEVERITY_ENUMERATION, 'default': 'unknown'},
            'multiple': {'type': 'Boolean', 'default': False},
        },
        'elements': [
            {'tag_name': 'ident', 'append': 'idents', 'min': 0, 'max': None, 'class': 'IdentType'},
            {'tag_name': 'impact-metric', 'min': 0, 'max': 1, 'type': 'String'},
            {'tag_name': 'profile-note', 'append': 'profile_notes', 'min': 0, 'max': None, 'class': 'ProfileNoteType'},
            {'tag_name': 'fix', 'class': 'FixType', 'min': 0, 'max': None, 'append': 'fixes'},
            {'tag_name': 'fixtext', 'class': 'FixtextType', 'min': 0, 'max': None, 'append': 'fixtexts'},
            {'tag_name': 'check', 'class': 'CheckType', 'min': 0, 'max': None, 'map': 'checks', 'key': 'selector'},
            {'tag_name': 'complex-check', 'class': 'ComplexCheckType', 'min': 0, 'max': 1},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
    }
