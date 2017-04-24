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

from scap.model.oval_defs_5.ObjectType import ObjectType
import logging

logger = logging.getLogger(__name__)
class SQL57ObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'sql57_object',
        'elements': [
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'set', 'class': 'SetElement'},
            {'tag_name': 'engine', 'class': 'EntityObjectEngineType'},
            {'tag_name': 'version', 'class': 'oval_defs_5.EntityObjectStringType'},
            {'tag_name': 'connection_string', 'class': 'oval_defs_5.EntityObjectStringType'},
            {'tag_name': 'sql', 'class': 'oval_defs_5.EntityObjectStringType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'filter', 'class': 'FilterElement'},
        ],
    }
