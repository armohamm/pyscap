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

logger = logging.getLogger(__name__)
class OvalDirectivesElement(Model):
    MODEL_MAP = {
        'tag_name' : 'oval_results',
        'elements': [
            {'tag_name': 'generator', 'class': 'scap.model.oval_5.GeneratorType'},
            {'tag_name': 'directives', 'class': 'scap.model.oval_5.res.DefaultDirectivesType'},
            {'tag_name': 'class_directives', 'class': 'scap.model.oval_5.res.ClassDirectivesType', 'min': 0, 'max': 5},
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
        ],
    }
