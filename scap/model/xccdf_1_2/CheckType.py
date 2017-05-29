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

logger = logging.getLogger(__name__)
class CheckType(Model):
    MODEL_MAP = {
        'attributes': {
            'system': {'type': 'AnyURI', 'required': True},
            'negate': {'type': 'Boolean', 'default': False},
            'id': {'type': 'NCName'},
            'selector': {'default': None, 'type': 'String'},
            'multi-check': {'type': 'Boolean', 'default': False},
        },
        'elements': [
            {'tag_name': 'check-import', 'class': 'CheckImportType', 'list': 'check_imports', 'min': 0, 'max': None},
            {'tag_name': 'check-export', 'class': 'CheckExportType', 'list': 'check_exports', 'min': 0, 'max': None},
            {'tag_name': 'check-content-ref', 'class': 'CheckContentRefType', 'list': 'check_content_refs', 'min': 0, 'max': None},
            {'tag_name': 'check-content', 'class': 'CheckContentType', 'min': 0, 'max': 1},
        ],
    }

    def __str__(self):
        if self.system in CHECK_SYSTEM_ENUMERATION:
            s = self.system
        else:
            return self.system

        if hasattr(self, 'id'):
            s += self.id + ':'

        if len(self.check_content_refs) > 0:
            s += str([ref.href + ('' if not hasattr(ref, 'name') else '#' + ref.name) for ref in self.check_content_refs])
        return s
