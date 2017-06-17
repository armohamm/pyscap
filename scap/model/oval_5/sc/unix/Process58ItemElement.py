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

from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class Process58ItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'command_line', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'exec_time', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'pid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'tag_name': 'ppid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'tag_name': 'priority', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'tag_name': 'ruid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'tag_name': 'scheduling_class', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'start_time', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'tty', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'user_id', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'tag_name': 'exec_shield', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemBoolType', 'max': 1},
            {'tag_name': 'loginuid', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
            {'list': 'posix_capabilitys', 'tag_name': 'posix_capability', 'min': 0, 'class': 'EntityItemCapabilityType', 'max': None},
            {'list': 'selinux_domain_labels', 'tag_name': 'selinux_domain_label', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': None},
            {'tag_name': 'session_id', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIntType', 'max': 1},
        ],
        'attributes': {
        },
    }

