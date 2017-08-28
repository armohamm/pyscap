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
from scap.model.xs.NCNameType import NCNameType
from scap.model.xs.IdType import IdType
from scap.model.xs.StringType import StringType
from .StatusType import StatusType
from .DcStatusType import DcStatusType
from .VersionType import VersionType
from .TextWithSubType import TextWithSubType
from .HtmlTextWithSubType import HtmlTextWithSubType
from .WarningType import WarningType
from .TextType import TextType
from .ReferenceType import ReferenceType
from .MetadataType import MetadataType

logger = logging.getLogger(__name__)

@attribute(local_name='abstract', type=BooleanType, default=False)
@attribute(local_name='cluster-id', type=NCNameType)
@attribute(local_name='extends', type=NCNameType)
@attribute(local_name='hidden', type=BooleanType, default=False)
@attribute(local_name='prohibitChanges', type=BooleanType, default=False)
@attribute(local_name='Id', type=IdType)
@element(local_name='status', cls=StatusType, list='statuses', min=0, max=None)
@element(local_name='dc-status', cls=DcStatusType, list='dc_statuses', min=0, max=None)
@element(local_name='version', cls=VersionType, min=0, max=1)
@element(local_name='title', list='titles', cls=TextWithSubType, min=0, max=None)
@element(local_name='description', list='descriptions', min=0, max=None, cls=HtmlTextWithSubType)
@element(local_name='warning', cls=WarningType, min=0, max=None, type=StringType, list='warnings')
@element(local_name='question', list='questions', cls=TextType, min=0, max=None)
@element(local_name='reference', list='references', min=0, max=None, cls=ReferenceType)
@element(local_name='metadata', list='metadata', min=0, max=None, cls=MetadataType)
class ItemType(Model):
    def __str__(self):
        return self.__class__.__name__ + ' # ' + self.id

    def get_extended(self, benchmark):
        try:
            extended = benchmark.item[self.extends]
        except AttributeError:
            # If any Item’s extends property identifier does not match the
            # identifier of a visible Item of the same type, then Loading fails.
            raise ValueError('Item ' + self.id + ' unable to extend unknown item id: ' + self.extends)

        if self.hidden:
            raise ValueError('Item ' + self.id + ' unable to extend hidden item id: ' + self.extends)

        return extended

    def process(self, host, benchmark, profile):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
