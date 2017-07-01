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

from scap.model.oval_5.defs.independent.ObjectType import ObjectType
from scap.model.oval_5.sc.EntityItemType import EntityItemType
from scap.model.oval_5.sc.independent.EnvironmentVariable58ItemElement import EnvironmentVariable58ItemElement

logger = logging.getLogger(__name__)
class EnvironmentVariable58ObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'environmentvariable58_object',
        'elements': [
            {'tag_name': 'pid', 'class': 'scap.model.oval_5.defs.EntityObjectType', 'min': 0},
            {'tag_name': 'name', 'class': 'scap.model.oval_5.defs.EntityObjectType', 'min': 0},
        ],
    }

    def collect_items_for_args(self, host, args):
        env_var = None
        try:
            col = host.load_collector('EnvironmentVariableCollector', args)
            env_var = col.collect()
            logger.debug('Collected ' + str(env_var) + ' for name ' + args['name'])
        except KeyError:
            logger.warn('Unable to find environment variable named ' + args['name'])
            item = EnvironmentVariable58ItemElement(self, args)
            if not args['value_masks']['name']:
                item.name = EntityItemType(value=args['name'])
                item.name.datatype = args['value_datatypes']['name']
            item.status = 'not exists'
            return [item]
        except:
            logger.warn('Error collecting environment variable ' + args['name'])
            item = EnvironmentVariable58ItemElement(self, args)
            if not args['value_masks']['name']:
                item.name = EntityItemType(value=args['name'])
                item.name.datatype = args['value_datatypes']['name']
            item.status = 'error'
            return [item]

        item = EnvironmentVariable58ItemElement(self, args)
        if not args['value_masks']['name']:
            item.name = EntityItemType(value=args['name'])
            item.name.datatype = args['value_datatypes']['name']
        item.value = EntityItemType(value=env_var)
        item.value.datatype = 'string'
        item.status = 'exists'
        return [item]
