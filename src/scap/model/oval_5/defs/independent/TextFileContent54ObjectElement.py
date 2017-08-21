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
import re

from scap.model.decorators import *
from scap.model.oval_5.defs.independent.ObjectType import ObjectType
from scap.model.oval_5.defs.independent.Textfilecontent54Behaviors import Textfilecontent54Behaviors
from scap.model.oval_5.sc.EntityItemType import EntityItemType
from scap.model.oval_5.sc.independent.TextFileContentItemElement import TextFileContentItemElement

logger = logging.getLogger(__name__)

@element(local_name='behaviors', cls='Textfilecontent54Behaviors', min=0, max=1)
@element(local_name='filepath', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='path', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='filename', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='pattern', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
@element(local_name='instance', cls='scap.model.oval_5.defs.EntityObjectType', min=0)
class TextFileContent54ObjectElement(ObjectType):
    def collect_items_for_args(self, host, args):
        if 'behaviors' in args and args['behaviors'] is not None:
            behaviors = args['behaviors']
            del args['behaviors']
        else:
            behaviors = Textfilecontent54Behaviors()

        args['behavior_max_depth'] = behaviors.max_depth
        args['behavior_recurse'] = behaviors.recurse
        args['behavior_recurse_direction'] = behaviors.recurse_direction
        args['behavior_recurse_file_system'] = behaviors.recurse_file_system
        args['behavior_windows_view'] = behaviors.windows_view

        flags = 0
        if behaviors.ignore_case:
            flags = flags | re.IGNORECASE
        if behaviors.multiline:
            flags = flags | re.MULTILINE
        if behaviors.singleline:
            flags = flags | re.DOTALL

        if 'filepath' in args and args['filepath'] is not None:
            paths = []
            try:
                col = host.load_collector('ResolveFilepathCollector', args)
                paths = col.collect()
                logger.debug('Collected ' + str(paths) + ' for filepath ' + args['filepath'])
            except FileNotFoundError:
                logger.warn('Filepath ' + args['filepath'] + ' did not match any files or directories')
                item = TextFileContentItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'not exists'
                return [item]
            except:
                logger.warn('Error resolving filepath ' + args['filepath'])
                item = TextFileContentItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'error'
                return [item]

            items = []
            for f in paths:
                item = TextFileContentItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']

                # get the content
                try:
                    col = host.load_collector('FileContentsCollector', {'path': f})
                    b = col.collect()
                except:
                    logger.warning('Unable to collect file content from ' + f)
                    item.status = 'error'
                    return [item]

                # try decoding
                for enc in ('utf_8', 'utf_8_sig', 'latin_1', 'cp1140', 'cp1250', 'ascii'):
                    try:
                        txt = b.decode(enc)
                        break
                    except (UnicodeError, ValueError):
                        # if didn't decode properly, try the next encoding
                        continue
                del b

                m = re.search(args['pattern'], txt, flags)
                if m is None:
                    logger.debug('File ' + f + ' did not match ' + args['pattern'])
                    # match failed
                    item.status = 'not exists'
                    return [item]

                item.text = EntityItemType(value=m.group(0))
                item.text.datatype = 'string'
                if 'instance' in args and isinstance(args['instance'], int):
                    item.instance = EntityItemType(value=args['instance'])
                    item.instance.datatype = 'int'
                    try:
                        ei = EntityItemType(tag_name='subexpression', value=m.group(args['instance']))
                        ei.datatype = 'string'
                        item.subexpressions.append(ei)
                    except IndexError:
                        logger.debug('subexpression ' + args['instance'] + ' does not exist in ' + m.group(0))
                        item.status = 'not exists'
                        return [item]
                else:
                    i = 1
                    for g in m.groups():
                        ei = EntityItemType(tag_name='subexpression', value=g)
                        ei.datatype = 'string'
                        item.subexpressions.append(ei)
                        i = i + 1

                items.append(item)

            return items

        elif (
            'path' in args
            and args['path'] is not None
            and 'filename' in args
            and args['filename'] is not None
        ):
            try:
                col = host.load_collector('ResolvePathFilenameCollector', args)
                paths = col.collect()
            except:
                item = TextFileContentItemElement(self, args)
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
                item = TextFileContentItemElement(self, args)
                if not args['value_masks']['path']:
                    item.path = EntityItemType(value=args['path'])
                    item.path.datatype = args['value_datatypes']['path']
                if not args['value_masks']['filename']:
                    item.filename = EntityItemType(value=args['filename'])
                    item.filename.datatype = args['value_datatypes']['filename']

                # get the content
                try:
                    col = host.load_collector('FileContentsCollector', {'path': f})
                    txt = col.collect()
                    m = re.search(args['pattern'], txt, flags)
                    if m is None:
                        # match failed
                        item.status = 'not exists'
                        return [item]

                    item.text = EntityItemType(value=m.group(0))
                    item.text.datatype = 'string'
                    if 'instance' in args and isinstance(args['instance'], int):
                        item.instance = EntityItemType(value=args['instance'])
                        item.instance.datatype = 'int'
                        try:
                            ei = EntityItemType(tag_name='subexpression', value=m.group(args['instance']))
                            ei.datatype = 'string'
                            item.subexpressions.append(ei)
                        except IndexError:
                            item.status = 'not exists'
                            return [item]
                    else:
                        i = 1
                        for g in m.groups():
                            ei = EntityItemType(tag_name='subexpression', value=g)
                            ei.datatype = 'string'
                            item.subexpressions.append(ei)
                            i = i + 1
                except:
                    logger.warning('Unable to collect from ' + f)
                    item.status = 'error'
                    return [item]

                items.append(item)

            return items
        else:
            item = TextFileContentItemElement(self, args)
            item.status = 'error'
            return [item]
