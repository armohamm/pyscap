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

from scap.model.oval_5.defs.independent.FileBehaviors import FileBehaviors
from scap.model.oval_5.defs.independent.ObjectType import ObjectType
from scap.model.oval_5.sc.EntityItemType import EntityItemType
from scap.model.oval_5.sc.independent.EntityItemHashTypeType import EntityItemHashTypeType
from scap.model.oval_5.sc.independent.FileHash58ItemElement import FileHash58ItemElement

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
class FileHash58ObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'filehash58_object',
        'elements': [
            {'tag_name': 'behaviors', 'class': 'FileBehaviors', 'min': 0, 'max': 1},
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.defs.EntityObjectType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval_5.defs.EntityObjectType', 'min': 0},
            {'tag_name': 'filename', 'class': 'scap.model.oval_5.defs.EntityObjectType', 'min': 0},
            {'tag_name': 'hash_type', 'class': 'EntityObjectHashTypeType', 'min': 0},
        ],
    }

    HASH_TYPES = [
        'MD5',
        'SHA-1',
        'SHA-224',
        'SHA-256',
        'SHA-384',
        'SHA-512',
    ]

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
                item = FileHash58ItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'not exists'
                return [item]
            except:
                logger.warn('Error resolving filepath ' + args['filepath'])
                item = FileHash58ItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']
                item.status = 'error'
                return [item]

            items = []
            for f in paths:
                logger.debug('Hashing ' + f)
                item = FileHash58ItemElement(self, args)
                if not args['value_masks']['filepath']:
                    item.filepath = EntityItemType(value=args['filepath'])
                    item.filepath.datatype = args['value_datatypes']['filepath']

                # check the hash_type arg
                if 'hash_type' not in args:
                    logger.warning('hash_type argument is required')
                    item.status = 'error'
                    return [item]

                if args['hash_type'] not in FileHash58ObjectElement.HASH_TYPES:
                    logger.warning('Unknown hash type: ' + args['hash_type'])
                    item.status = 'error'
                    return [item]

                item.hash_type = EntityItemHashTypeType(value=args['hash_type'])

                # get the hash
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': args['hash_type']})
                    item.hash = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect ' + args['hash_type'] + ' hash from ' + f)
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
                item = FileHash58ItemElement(self, args)
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
                item = FileHash58ItemElement(self, args)
                if not args['value_masks']['path']:
                    item.path = EntityItemType(value=args['path'])
                    item.path.datatype = args['value_datatypes']['path']
                if not args['value_masks']['filename']:
                    item.filename = EntityItemType(value=args['filename'])
                    item.filename.datatype = args['value_datatypes']['filename']

                # check the hash_type arg
                if 'hash_type' not in args:
                    logger.warning('hash_type argument is required')
                    item.status = 'error'
                    return [item]

                if args['hash_type'] not in FileHash58ObjectElement.HASH_TYPES:
                    logger.warning('Unknown hash type: ' + args['hash_type'])
                    item.status = 'error'
                    return [item]

                item.hash_type = EntityItemHashTypeType(value=args['hash_type'])

                # get the hash
                try:
                    col = host.load_collector('FileHashCollector', {'path': f, 'type': args['hash_type']})
                    item.hash = EntityItemType(value=col.collect())
                except:
                    logger.warning('Unable to collect ' + args['hash_type'] + ' hash from ' + f)
                    item.status = 'error'
                    return [item]

                items.append(item)

            return items
        else:
            item = FileHash58ItemElement(self, args)
            item.status = 'error'
            return [item]

    #     hash_param = {
    #         'MD5': 'MD5',
    #         'SHA-1': 'SHA1',
    #         #'SHA-224': '',
    #         'SHA-256': 'SHA256',
    #         'SHA-384': 'SHA384',
    #         'SHA-512': 'SHA512',
    #     }
    #     if obj.filepath is not None:
    #         item = FileHash58ItemElement()
    #         # TODO the max_depth and recurse_direction behaviors are not allowed with a filepath entity
    #         # TODO the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a filepath entity
    #
    #         # check datatype
    #         if obj.filepath.datatype != 'string':
    #             item.status = 'not collected'
    #             return [item]
    #
    #         filepath_value = self.resolve_entity_object_value(obj.filepath)
    #         qfilepath = filepath_value.replace('"', '\\"')
    #         if not obj.filepath.mask:
    #             item.filepath = EntityItemType(value=filepath_value)
    #
    #         # since we're given an absolute path, we need equals as the operation
    #         if obj.filepath.operation != 'equals':
    #             item.status = 'not collected'
    #             return [item]
    #
    #         # check if file exists
    #         cmd = 'Test-Path -LiteralPath \'' + qfilepath + '\' -PathType Leaf'
    #         cmd = 'powershell -Command "' + cmd.replace('"', '\\"') + '"'
    #
    #         logger.debug('Checking existence of ' + obj.filepath.get_value() + ': ' + cmd)
    #         return_code, out_lines, err_lines = self.host.exec_command(cmd)
    #         if out_lines[0] == 'False':
    #             item.status = 'does not exist'
    #             return [item]
    #         elif out_lines[0] != 'True':
    #             logger.warning('Unable to check existence ' + obj.filepath.get_value() \
    #             + str((return_code, out_lines, err_lines)))
    #             item.status = 'error'
    #             return [item]
    #         item.status = 'exists'
    #
    #         # get the hash
    #         hash_type_value = self.resolve_entity_object_value(obj.hash_type)
    #         item.hash_type = EntityItemHashTypeType(value=hash_type_value)
    #         try:
    #             cmd = 'Get-FileHash -LiteralPath \'' + qfilepath + '\'' \
    #             + ' -Algorithm ' + hash_param[hash_type_value] \
    #             + ' | foreach {$_.Hash}"'
    #             cmd = 'powershell -Command "' + cmd.replace('"', '\\"') + '"'
    #
    #             logger.debug('Collecting ' + obj.filepath.get_value() + ': ' + cmd)
    #             return_code, out_lines, err_lines = self.host.exec_command(cmd)
    #             item.hash = EntityItemType(value=out_lines[0])
    #         except (IndexError, KeyError):
    #             logger.warning('Unable to collect ' + obj.filepath.get_value() + str((return_code, out_lines, err_lines)))
    #             item.status = 'error'
    #             return [item]
    #
    #     elif obj.path is not None and obj.filename is not None:
    #         # TODO the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a path entity
    #         # TODO the max_depth behavior MUST not be used when a pattern match is used with a path entity
    #         # TODO the recurse_direction behavior MUST not be used when a pattern match is used with a path entity
    #         # TODO the recurse behavior MUST not be used when a pattern match is used with a path entity
    #
    #         # check datatype
    #         if obj.path.datatype != 'string':
    #             item = FileHash58ItemElement()
    #             if not obj.path.mask:
    #                 item.path = EntityItemType(value=obj.path.get_value())
    #                 item.path.datatype = obj.path.datatype
    #             item.status = 'not collected'
    #             return [item]
    #
    #         path_value = self.resolve_entity_object_value(obj.path)
    #         paths = []
    #         if obj.path.operation == 'equals':
    #             # check if path exists
    #             qpath = path_value.replace('"', '\\"')
    #             cmd = 'Test-Path -Path \'' + qpath + '\' -PathType Container'
    #             cmd = 'powershell -Command "' + cmd.replace('"', '\\"') + '"'
    #             logger.debug('Checking existence of ' + path_value + ': ' + cmd)
    #             return_code, out_lines, err_lines = self.host.exec_command(cmd)
    #             if out_lines[0] == 'False':
    #                 item = FileHash58ItemElement()
    #                 if not obj.path.mask:
    #                     item.path = EntityItemType(value=path_value)
    #                     item.path.datatype = 'string'
    #                 item.status = 'does not exist'
    #                 return [item]
    #             elif out_lines[0] != 'True':
    #                 logger.warning('Unable to check existence of ' + path_value + str((return_code, out_lines, err_lines)))
    #                 item = FileHash58ItemElement()
    #                 if not obj.path.mask:
    #                     item.path = EntityItemType(value=path_value)
    #                     item.path.datatype = 'string'
    #                 item.status = 'error'
    #                 return [item]
    #
    #             paths.append(path_value)
    #         elif obj.path.operation == 'pattern match':
    #             # strip the pattern off the path
    #             # TODO
    #
    #             # check if base path exists
    #             qpath = path_value.replace('"', '\\"')
    #             cmd = 'Test-Path -Path \'' + qpath + '\' -PathType Container'
    #             cmd = 'powershell -Command "' + cmd.replace('"', '\\"') + '"'
    #             logger.debug('Checking existence of ' + path_value + ': ' + cmd)
    #             return_code, out_lines, err_lines = self.host.exec_command(cmd)
    #             if out_lines[0] == 'False':
    #                 item = FileHash58ItemElement()
    #                 if not obj.path.mask:
    #                     item.path = EntityItemType(value=path_value)
    #                     item.path.datatype = 'string'
    #                 item.status = 'does not exist'
    #                 return [item]
    #             elif out_lines[0] != 'True':
    #                 logger.warning('Unable to check existence of ' + path_value + str((return_code, out_lines, err_lines)))
    #                 item = FileHash58ItemElement()
    #                 if not obj.path.mask:
    #                     item.path = EntityItemType(value=path_value)
    #                     item.path.datatype = 'string'
    #                 item.status = 'error'
    #                 return [item]
    #
    #             # get child items of the base path
    #             # TODO
    #
    #             # if child items match the pattern, append path
    #             # TODO
    #
    #         if obj.filename.datatype != 'string':
    #             item = FileHash58ItemElement()
    #             if not obj.path.mask:
    #                 item.path = EntityItemType(value=path_value)
    #                 item.path.datatype = 'string'
    #             if not obj.filename.mask:
    #                 item.filename = EntityItemType(value=obj.filename.get_value())
    #                 item.filename.datatype = obj.filename.datatype
    #             item.status = 'not collected'
    #             return [item]
    #
    #         # filename entity cannot be empty unless the xsi:nil attribute is set to true or a var_ref is used
    #         filename_value = self.resolve_entity_object_value(obj.filename)
    #         if obj.filename.is_nil() and filename_value is None:
    #             # can't hash a dir
    #             item = FileHash58ItemElement()
    #             if not obj.path.mask:
    #                 item.path = EntityItemType(value=path_value)
    #                 item.path.datatype = 'string'
    #             if not obj.filename.mask:
    #                 item.filename = EntityItemType()
    #                 item.filename.set_nil()
    #                 item.filename.datatype = 'string'
    #             item.status = 'not collected'
    #             return [item]
    #
    #         hash_type_value = self.resolve_entity_object_value(obj.hash_type)
    #         for path in paths:
    #             filenames = []
    #             # get child items of the path(s)
    #             # TODO
    #
    #             for filename in filenames:
    #                 if obj.filename.operation == 'equals':
    #                     # if child item doesn't match the filename, continue
    #                     # TODO
    #                     continue
    #                 elif obj.filename.operation == 'pattern match':
    #                     # if child items doesn't match the pattern, continue
    #                     # TODO
    #                     continue
    #
    #                 item = FileHash58ItemElement()
    #                 if not obj.path.mask:
    #                     item.path = EntityItemType(value=path)
    #                     item.path.datatype = 'string'
    #                 if not obj.filename.mask:
    #                     item.filename = EntityItemType(value=filename)
    #                     item.filename.datatype = 'string'
    #                 item.status = 'exists'
    #                 item.hash_type = EntityItemHashTypeType(value=hash_type_value)
    #
    #                 try:
    #                     cmd = 'Get-FileHash -Path \'' + qfilepath + '\'' \
    #                     + ' -Algorithm ' + hash_param[hash_type_value] \
    #                     + ' | foreach {$_.Hash}'
    #                     cmd = 'powershell -Command "' + cmd.replace('"', '\\"') + '"'
    #
    #                     logger.debug('Collecting ' + obj.filepath.get_value() + ': ' + cmd)
    #                     return_code, out_lines, err_lines = self.host.exec_command(cmd)
    #                     item.hash = EntityItemType(value=out_lines[0])
    #                 except (IndexError, KeyError):
    #                     logger.warning('Unable to collect ' + obj.filepath.get_value() + str((return_code, out_lines, err_lines)))
    #                     item.status = 'error'
    #
    #                 items.append(item)
    #     else:
    #         item = FileHash58ItemElement()
    #         item.status = 'error'
    #         return [item]
