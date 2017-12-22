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
from scap.model.decorators import *
from scap.model.xs.BooleanType import BooleanType
from scap.model.xs.IdType import IdType
from scap.model.xs.NCNameType import NCNameType

from .Extendable import Extendable
from .HtmlTextWithSubType import HtmlTextWithSubType
from .ProfileRefineRuleType import ProfileRefineRuleType
from .ProfileRefineValueType import ProfileRefineValueType
from .ProfileSelectType import ProfileSelectType
from .ProfileSetValueType import ProfileSetValueType
from .ReferenceType import ReferenceType
from .SignatureType import SignatureType
from .StatusType import StatusType
from .TextWithSubType import TextWithSubType
from .UriIdrefType import UriIdrefType
from .VersionType import VersionType

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=NCNameType)
@attribute(local_name='prohibitChanges', type=BooleanType, default=False)
@attribute(local_name='abstract', type=BooleanType, default=False)
@attribute(local_name='note-tag', type=NCNameType)
@attribute(local_name='extends', type=NCNameType)
@attribute(local_name='Id', type=IdType)
@element(local_name='status', cls=StatusType, list='statuses', min=0, max=None)
@element(local_name='version', cls=VersionType, min=0, max=1)
@element(local_name='title', cls=TextWithSubType, list='titles', min=1, max=None)
@element(local_name='description', cls=HtmlTextWithSubType, list='descriptions', min=0, max=None)
@element(local_name='reference', cls=ReferenceType, list='references', min=0, max=None)
@element(local_name='platform', cls=UriIdrefType, list='platforms', min=0, max=None)
# choice
@element\(local_name='select', cls=ProfileSelectType, dict='settings', dict_key='idref', min=0, max=None)
@element\(local_name='set-value', cls=ProfileSetValueType, dict='settings', dict_key='idref', min=0, max=None)
@element\(local_name='refine-value', cls=ProfileRefineValueType, dict='settings', dict_key='idref', min=0, max=None)
@element\(local_name='refine-rule', cls=ProfileRefineRuleType, dict='settings', dict_key='idref', min=0, max=None)
@element(local_name='signature', cls=SignatureType, min=0, max=1)
class ProfileType(Extendable):
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
