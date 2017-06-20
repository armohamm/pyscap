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

from scap.collector.OvalCollector import OvalCollector
from scap.model.oval_5.defs.independent.FileBehaviors import FileBehaviors
from scap.model.oval_5.sc.EntityItemType import EntityItemType
from scap.model.oval_5.sc.independent.FileHash58ItemElement import FileHash58ItemElement
from scap.model.oval_5.sc.independent.EntityItemHashTypeType import EntityItemHashTypeType

logger = logging.getLogger(__name__)
class FileHash58Collector(OvalCollector):
    def collect(self):
        obj = self.args['object']

        # if behaviors doesn't exist, use defaults
        if obj.behaviors is not None:
            behaviors = obj.behaviors
        else:
            behaviors = FileBehaviors()

        item = FileHash58ItemElement()
        hash_cmd = {
            'MD5': 'md5sum',
            'SHA-1': 'sha1sum',
            'SHA-224': 'sha224sum',
            'SHA-256': 'sha256sum',
            'SHA-384': 'sha384sum',
            'SHA-512': 'sha512sum',
        }
        if obj.filepath is not None:
            # TODO the max_depth and recurse_direction behaviors are not allowed with a filepath entity
            # TODO the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a filepath entity
            item.filepath = EntityItemType(value=obj.filepath.get_value())
            qfilepath = obj.filepath.get_value().replace('"', '\\"')

            # check if file exists
            cmd = 'if [ -f "' + qfilepath + '" ]; then echo "true"; else echo "false"; fi'
            logger.debug('Checking existence of ' + obj.filepath.get_value() + ': ' + cmd)
            return_code, out_lines, err_lines = self.host.exec_command(cmd)
            if out_lines[0] == 'false':
                item.status = 'does not exist'
                return [item]
            elif out_lines[0] != 'true':
                logger.warning('Unable to check existence ' + obj.filepath.get_value() + str((return_code, out_lines, err_lines)))
                item.status = 'error'
                return [item]
            item.status = 'exists'

            # get the hash
            item.hash_type = EntityItemHashTypeType(value=obj.hash_type.get_value())
            try:
                cmd = hash_cmd[obj.hash_type.get_value()] + ' "' + qfilepath + '" | cut -d" " -f1'
                logger.debug('Collecting ' + obj.filepath.get_value() + ': ' + cmd)
                return_code, out_lines, err_lines = self.host.exec_command(cmd)
                item.hash = EntityItemType(value=out_lines[0])
            except (IndexError, KeyError):
                logger.warning('Unable to collect ' + obj.filepath.get_value() + str((return_code, out_lines, err_lines)))
                item.status = 'not collected'
                return [item]

        elif obj.path is not None and obj.filename is not None:
            item.path = EntityItemType(value=obj.path.get_value())
            item.filename = EntityItemType(value=obj.filename.get_value())
            qpath = obj.path.get_value().replace('"', '\\"')

            # check if path exists
            logger.debug('Checking existence of ' + obj.path.get_value() + ': ' + cmd)
            return_code, out_lines, err_lines = self.host.exec_command('if [ -d "' + qpath + '"]; then echo "true"; else echo "false"; fi')
            if out_lines[0] == 'false':
                item.status = 'does not exist'
                return [item]
            elif out_lines[0] != 'true':
                logger.warning('Unable to check existence ' + obj.path.get_value() + str((return_code, out_lines, err_lines)))
                item.status = 'error'
                return [item]
            item.status = 'exists'

            # TODO the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a path entity
            # TODO the max_depth behavior MUST not be used when a pattern match is used with a path entity
            # TODO the recurse_direction behavior MUST not be used when a pattern match is used with a path entity
            # TODO the recurse behavior MUST not be used when a pattern match is used with a path entity

            # TODO filename entity cannot be empty unless the xsi:nil attribute is set to true or a var_ref is used
            if obj.filename.is_nil():
                # can't hash a dir
                item.status = 'not collected'
            else:
                # TODO
                pass

        else:
            item.status = 'not collected'

        return [item]
