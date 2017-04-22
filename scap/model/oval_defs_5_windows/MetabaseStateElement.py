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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class MetabaseStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'metabase_state',
        'elements': [
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'key', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'id', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'name', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'user_type', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'data_type', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows', 'tag_name': 'data', 'class': 'oval_defs_5.EntityStateAnySimpleType', 'min': 0},
        ],
    }
