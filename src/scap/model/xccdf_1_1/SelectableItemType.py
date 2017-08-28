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
import re

from .ItemType import ItemType
from scap.model.decorators import *
from scap.model.xs.BooleanType import BooleanType
from .WeightType import WeightType
from .HtmlTextWithSubType import HtmlTextWithSubType
from .OverrideableUriIdrefType import OverrideableUriIdrefType
from .IdrefListType import IdrefListType
from .IdrefType import IdrefType

logger = logging.getLogger(__name__)

@attribute(local_name='selected', type=BooleanType, default=True)
@attribute(local_name='weight', type=WeightType, default=1.0)
@element(local_name='rationale', list='rationales', min=0, max=None, cls=HtmlTextWithSubType)
@element(local_name='platform', list='platforms', min=0, max=None, cls=OverrideableUriIdrefType)
@element(local_name='requires', list='requires', min=0, max=None, cls=IdrefListType)
@element(local_name='conflicts', list='conflicts', min=0, max=None, cls=IdrefType)
class SelectableItemType(ItemType):
    def _require_one_item(self, benchmark, item_ids):
        for item_id in item_ids:
            item = benchmark.items[item_id]
            if item.selected:
                return True
        return False

    def _continue_processing(self):
        ### Item.Select

        # If any of the following conditions holds, cease processing of this
        # Item:

        # 1. The processing type is Tailoring, and the optional property and
        # selected property are both false.
        # TODO

        # 2. The processing type is Document Generation, and the hidden property
        # is true.
        # TODO

        # 3. The processing type is Compliance Checking, and the selected
        # property is false.
        if not self.selected:
            return False

        # 4. The processing type is Compliance Checking, and the current
        # platform (if known by the tool) is not a member of the set of
        # platforms for this Item.
        # TODO

        return True

    def process(self, host, benchmark, profile_id):
        ### Item.Process

        # Check the contents of the requires and conflicts properties, and if
        # any required Items are unselected or any conflicting Items are
        # selected, then set the selected and allowChanges properties to false.
        for required_item in self.requires:
            # at least one
            required_item_ids = re.split(r'\S+', required_item.value)
            logger.debug('Checking that one of ' + str(required_item_ids) + ' is selected')
            if not self._require_one_item(benchmark, required_item_ids):
                self.selected = False
                self.prohibitChanges = True
                break

        for conflicting_item in self.conflicts:
            item = benchmark.items[conflicting_item.value]
            if item.selected:
                self.selected = False
                self.prohibitChanges = True
                break
