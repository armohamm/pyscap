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

from scap.model.decorators import *
from scap.model.oval_5.defs.independent.FileBehaviors import FileBehaviors
from scap.model.oval_5.defs.independent.ObjectType import ObjectType
from scap.model.oval_5.sc.EntityItemType import EntityItemType
from scap.model.oval_5.sc.independent.FileHashItemElement import FileHashItemElement

logger = logging.getLogger(__name__)

@element(local_name='behaviors', cls='FileBehaviors', min=0)
@element(local_name='filepath', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='path', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='filename', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
class FileHashObjectElement(ObjectType):
    def collect_items_for_args(self, host, args):
        if 'behaviors' in args and args['behaviors'] is not None:
            behaviors = args['behaviors']
            del args['behaviors']
        else:
            behaviors = FileBehaviors()

        args['behavior_max_depth'] = behaviors.max_depth
        args['behavior_recurse'] = behaviors.recurse
        args['behavior_recurse_direction'] = behaviors.recurse_direction
        args['behavior_recurse_file_system'] = behaviors.recurse_file_system
        args['behavior_windows_view'] = behaviors.windows_view

        if 'filepath' in args and args['filepath'] is not None:
            paths = []
            try:
                col = host.load_collector('ResolveFilepathCollector', args)
                paths = col.collect()
                logger.debug('Collected ' + str(paths) + ' for filepath ' + args['filepath'])
            except FileNotFoundError:
                logger.warn('Filepath ' + args['filepath'] + ' did not match any files or directories')
                item = FileHashItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'not exists'
                return [item]
            except:
                logger.warn('Error resolving filepath ' + args['filepath'])
                item = FileHashItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'error'
                return [item]

            items = []
            for f in paths:
                logger.debug('Hashing ' + f)
                item = FileHashItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']

                # get the hashes
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': 'MD5'})
                    item.md5 = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect MD5 hash from ' + f)
                    item.status = 'error'
                    return [item]
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': 'SHA-1'})
                    item.sha1 = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect SHA-1 hash from ' + f)
                    item.status = 'error'
                    return [item]

                items.append(item)

            return items

        elif 'path' in args and args['path'] is not None \
        and 'filename' in args and args['filename'] is not None:
            try:
                col = host.load_collector('ResolvePathFilenameCollector', args)
                paths = col.collect()
            except:
                item = FileHashItemElement(self, args)
                if not args['value_masks']['path']:
                    item.path = EntityItemType(value=args['path'])
                    item.path.datatype = args['value_datatypes']['path']
                if not args['value_masks']['filename']:
                    item.filename = EntityItemType(value=args['filename'])
                    item.filename.datatype = args['value_datatypes']['filename']
                item.status = 'error'
                return [item]

            items = []
            for f in paths:
                item = FileHashItemElement(self, args)
                if not args['value_masks']['path']:
                    item.path = EntityItemType(value=args['path'])
                    item.path.datatype = args['value_datatypes']['path']
                if not args['value_masks']['filename']:
                    item.filename = EntityItemType(value=args['filename'])
                    item.filename.datatype = args['value_datatypes']['filename']

                # get the hashes
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': 'MD5'})
                    item.md5 = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect MD5 hash from ' + f)
                    item.status = 'error'
                    return [item]
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': 'SHA-1'})
                    item.sha1 = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect SHA-1 hash from ' + f)
                    item.status = 'error'
                    return [item]

                items.append(item)

            return items
        else:
            item = FileHashItemElement(self, args)
            item.status = 'error'
            return [item]
