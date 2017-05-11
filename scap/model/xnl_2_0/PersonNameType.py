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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class PersonNameType(Model):
    MODEL_MAP = {
        'tag_name': 'PersonName',
        'elements': [
            {'tag_name': 'NameLine', 'list': 'name_lines', 'class': 'NameLineType'},
            {'tag_name': 'PrecedingTitle', 'list': 'preceding_titles', 'class': 'PrecedingTitleElement'},
            {'tag_name': 'Title', 'list': 'titles', 'class': 'TitleElement'},
            {'tag_name': 'FirstName', 'list': 'first_names', 'class': 'FirstNameElement'},
            {'tag_name': 'MiddleName', 'list': 'middle_names', 'class': 'MiddleNameElement'},
            {'tag_name': 'NamePrefix', 'in': 'name_prefix', 'class': 'NamePrefixElement'},
            {'tag_name': 'LastName', 'list': 'last_names', 'class': 'LastNameElement'},
            {'tag_name': 'OtherName', 'list': 'other_names', 'class': 'OtherNameElement'},
            {'tag_name': 'Alias', 'list': 'aliases', 'class': 'AliasElement'},
            {'tag_name': 'GenerationIdentifier', 'list': 'generation_identifiers', 'class': 'GenerationIdentifierElement'},
            {'tag_name': 'Suffix', 'list': 'suffixes', 'class': 'SuffixElement'},
            {'tag_name': 'GeneralSuffix', 'list': 'general_suffix', 'class': 'GeneralSuffixElement'},
        ],
        'attributes': {
            'Type': {},
            'Code': {},
            'NameDetailsKeyRef': {}, # from grKeyRefs
            '*': {},
        }
    }
