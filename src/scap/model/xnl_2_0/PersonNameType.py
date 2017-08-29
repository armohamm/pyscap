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

from .AliasElement import AliasElement
from .FirstNameElement import FirstNameElement
from .GeneralSuffixElement import GeneralSuffixElement
from .GenerationIdentifierElement import GenerationIdentifierElement
from .LastNameElement import LastNameElement
from .MiddleNameElement import MiddleNameElement
from .NameLineType import NameLineType
from .NamePrefixElement import NamePrefixElement
from .OtherNameElement import OtherNameElement
from .PrecedingTitleElement import PrecedingTitleElement
from .SuffixElement import SuffixElement
from .TitleElement import TitleElement

logger = logging.getLogger(__name__)

@attribute(local_name='Type', )
@attribute(local_name='Code', )
@attribute(local_name='NameDetailsKeyRef', ) # from grKeyRefs
@attribute(local_name='*', )
@element(local_name='NameLine', list='name_lines', cls=NameLineType)
@element(local_name='PrecedingTitle', list='preceding_titles', cls=PrecedingTitleElement)
@element(local_name='Title', list='titles', cls=TitleElement)
@element(local_name='FirstName', list='first_names', cls=FirstNameElement)
@element(local_name='MiddleName', list='middle_names', cls=MiddleNameElement)
@element(local_name='NamePrefix', into='name_prefix', cls=NamePrefixElement)
@element(local_name='LastName', list='last_names', cls=LastNameElement)
@element(local_name='OtherName', list='other_names', cls=OtherNameElement)
@element(local_name='Alias', list='aliases', cls=AliasElement)
@element(local_name='GenerationIdentifier', list='generation_identifiers', cls=GenerationIdentifierElement)
@element(local_name='Suffix', list='suffixes', cls=SuffixElement)
@element(local_name='GeneralSuffix', list='general_suffix', cls=GeneralSuffixElement)
class PersonNameType(Model):
    pass
