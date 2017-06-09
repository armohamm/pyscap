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
class ItemType(Model):
    MODEL_MAP = {
        # abstract
        'attributes': {
            'abstract': {'type': 'BooleanType', 'default': False},
            'cluster-id': {'type': 'NCNameType'},
            'extends': {'type': 'NCNameType'},
            'hidden': {'type': 'BooleanType', 'default': False},
            'prohibitChanges': {'type': 'BooleanType', 'default': False},
            'Id': {'type': 'ID'},
        },
        'elements': [
            {'tag_name': 'status', 'class': 'StatusType', 'list': 'statuses', 'min': 0, 'max': None},
            {'tag_name': 'dc-status', 'class': 'DCStatusType', 'list': 'dc_statuses', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'list': 'titles', 'class': 'TextWithSubType', 'min': 0, 'max': None},
            {'tag_name': 'description', 'list': 'descriptions', 'min': 0, 'max': None, 'class': 'HtmlTextWithSubType'},
            {'tag_name': 'warning', 'class': 'WarningType', 'min': 0, 'max': None, 'type': 'StringType', 'list': 'warnings'},
            {'tag_name': 'question', 'list': 'questions', 'class': 'TextType', 'min': 0, 'max': None},
            {'tag_name': 'reference', 'list': 'references', 'min': 0, 'max': None, 'class': 'ReferenceType'},
            {'tag_name': 'metadata', 'list': 'metadata', 'min': 0, 'max': None, 'class': 'MetadataType'},
        ],
    }

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
