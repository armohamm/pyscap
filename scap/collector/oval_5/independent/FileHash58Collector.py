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

from scap.collector.oval_5.OvalCollector import OvalCollector
from scap.collector.oval_5.independent.FamilyCollector import FamilyCollector
from scap.model.cpe_matching_2_3.CPE import CPE
from scap.model.oval_5.defs.independent.FileBehaviors import FileBehaviors
from scap.model.oval_5.sc.EntityItemStringType import EntityItemStringType
from scap.model.oval_5.sc.independent.FileHash58ItemElement import FileHash58ItemElement
from scap.model.oval_5.sc.independent.EntityItemHashTypeType import EntityItemHashTypeType

logger = logging.getLogger(__name__)
class FileHash58Collector(OvalCollector):
    def collect(self):
        obj = self.args['object']

        if 'oval_family' not in self.host.facts:
            FamilyCollector(self.host, {}).collect()

        # if behaviors doesn't exist, use defaults
        if obj.behaviors is not None:
            behaviors = obj.behaviors
        else:
            behaviors = FileBehaviors()

        hash_cmd = {
            'MD5': 'md5sum',
            'SHA-1': 'sha1sum',
            'SHA-224': 'sha224sum',
            'SHA-256': 'sha256sum',
            'SHA-384': 'sha384sum',
            'SHA-512': 'sha512sum',
        }
        item = FileHash58ItemElement()
        if self.host.facts['oval_family'] == 'linux':
            if obj.filepath is not None:
                item.filepath = EntityItemStringType(value=obj.filepath.text)
                qfilepath = obj.filepath.text.replace('"', '\\"')

                # check if file exists
                cmd = 'if [ -f "' + qfilepath + '" ]; then echo "true"; else echo "false"; fi'
                logger.debug('Checking existence of ' + obj.filepath.text + ': ' + cmd)
                return_code, out_lines, err_lines = self.host.exec_command(cmd)
                if out_lines[0] == 'true':
                    item.status = 'exists'
                elif out_lines[0] == 'false':
                    item.status = 'does not exist'
                else:
                    logger.warning('Unable to check existence ' + obj.filepath.text + str((return_code, out_lines, err_lines)))
                    item.status = 'error'

                # get the hash
                item.hash_type = EntityItemHashTypeType(value=obj.hash_type.text)
                try:
                    cmd = hash_cmd[obj.hash_type.text] + ' "' + qfilepath + '" | cut -d" " -f1'
                    logger.debug('Collecting ' + obj.filepath.text + ': ' + cmd)
                    return_code, out_lines, err_lines = self.host.exec_command(cmd)
                    item.hash = EntityItemStringType(value=out_lines[0])
                except (IndexError, KeyError):
                    logger.warning('Unable to collect ' + obj.filepath.text + str((return_code, out_lines, err_lines)))
                    item.status = 'not collected'

            elif obj.path is not None:
                item.path = EntityItemStringType(value=obj.path.text)
                qpath = obj.path.text.replace('"', '\\"')

                # check if path exists
                return_code, out_lines, err_lines = self.host.exec_command('if [ -d "' + qpath + '"]; then echo "true"; else echo "false"; fi')
                if out_lines[0] == 'true':
                    item.status = 'exists'
                elif out_lines[0] == 'false':
                    item.status = 'does not exist'
                else:
                    item.status = 'error'

                if obj.filename is None or obj.filename.is_nil():
                    # can't hash a dir
                    item.status = 'not collected'

        else:
            raise NotImplementedError(self.__class__.__name__ + ' has not been implemented for OVAL family: ' + self.host.facts['oval_family'])

        return [item]
