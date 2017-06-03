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

import logging

from scap.Model import Model
from scap.model.xccdf_1_2 import *

logger = logging.getLogger(__name__)
class ProfileType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'status', 'class': 'StatusType', 'list': 'statuses', 'min': 0, 'max': None},
            {'tag_name': 'dc-status', 'class': 'DCStatusType', 'list': 'dc_statuses', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'class': 'TextWithSubType', 'list': 'titles', 'min': 1, 'max': None},
            {'tag_name': 'description', 'class': 'HtmlTextWithSubType', 'list': 'descriptions', 'min': 0, 'max': None},
            {'tag_name': 'reference', 'class': 'ReferenceType', 'list': 'references', 'min': 0, 'max': None},
            {'tag_name': 'platform', 'class': 'OverrideableCPE2IDRefType', 'list': 'platforms', 'min': 0, 'max': None},
            {'tag_name': 'select', 'class': 'ProfileSelectType', 'dict': 'selects', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-complex-value', 'class': 'ProfileSetComplexValueType', 'dict': 'set_complex_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'set-value', 'class': 'ProfileSetValueType', 'dict': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'refine-value', 'class': 'ProfileRefineValueType', 'dict': 'refine_values', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'refine-rule', 'class': 'ProfileRefineRuleType', 'dict': 'refine_rules', 'key': 'idref', 'min': 0, 'max': None},
            {'tag_name': 'metadata', 'class': 'MetadataType', 'list': 'metadata', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'required': True, 'type': 'ProfileIDPattern'},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
            'abstract': {'type': 'Boolean', 'default': False},
            'note-tag': {'type': 'NCName'},
            'extends': {'type': 'NCName'},
            'Id': {'type': 'ID'},
        },
    }

    def __str__(self):
        return self.__class__.__name__ + ' # ' + self.id

    def get_extended(self, benchmark):
        try:
            extended = benchmark.profile[self.extends]
        except AttributeError:
            # If any Profile’s extends property identifier does not match the
            # identifier of another Profile in the Benchmark, then Loading
            # fails.
            raise ValueError('Profile ' + self.id + ' unable to extend unknown profile id: ' + self.extends)

        return extended

    def apply(self, host, benchmark):
        ### Benchmark.Profile

        # TODO check that if this group has a platform identified, that the
        # target system matches

        # If a Profile id was specified, then apply the settings in the Profile
        # to the Items of the Benchmark
        for setting_idref in self.settings:
            setting = self.settings[setting_idref]
            logger.debug('Looking for ' + setting_idref + ' in ' + str(benchmark))
            item = benchmark.find_reference(setting_idref)
            if item is None:
                raise ValueError('Unable to find idref ' + setting_idref + ' in ' + str(self) + ' setting application')

            logger.debug(str(self) + ' applying ' + setting.__class__.__name__ + ' to ' + str(item))
            setting.apply(item)
