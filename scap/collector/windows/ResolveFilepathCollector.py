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

from scap.Collector import Collector, ArgumentException

logger = logging.getLogger(__name__)
class ResolveFilepathCollector(Collector):
    def __init__(self, host, args):
        super(ResolveFilepathCollector, self).__init__(host, args)

        if 'filepath' not in args:
            raise ArgumentException('ResolveFilepathCollector requires filepath argument')

        for i in ('value_datatypes', 'value_masks', 'value_operations'):
            if i not in args:
                raise ArgumentException('ResolveFilepathCollector requires ' + i + ' argument')

        if args['value_datatypes']['filepath'] != 'string':
            raise ArgumentException('ResolveFilepathCollector requires string filepath')

        # NOTE: operation should be already validated by EntityObjectType

        if args['value_operations']['filepath'] == 'pattern match' and args['behavior_recurse_file_system'] == 'defined':
            raise ArgumentException('ResolveFilepathCollector behavior_recurse_file_system set to defined with pattern match operation')

    def collect(self):
        if self.args['value_operations']['filepath'] in ['equals', 'case insensitive equals']:
            cmd = "Test-Path -LiteralPath '" + self.args['filepath'].replace("\'", "\\'") + "'"
            return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

            if return_code != 0 or len(out_lines) < 1 or out_lines[0] != 'True':
                raise FileNotFoundError(self.args['filepath'] + ' was not found')
            else:
                return [self.args['filepath']]

        elif self.args['value_operations']['filepath'] in ['not equal', 'case insensitive not equal']:
            raise NotImplementedError(self.args['value_operations']['filepath'] + ' operation not supported for ResolveFilepathCollector')

        elif self.args['value_operations']['filepath'] == 'pattern match':
            filepath = self.args['filepath']
            logger.debug('Matching pattern ' + filepath)

            # strip off leading ^ or trailing $ as they are assumed
            if filepath.startswith('^'):
                filepath = filepath[1:]
            if filepath.endswith('$'):
                filepath = filepath[:-1]

            paths = []
            m = re.match(r'^([a-zA-Z]):\\', filepath)
            if m:
                # C:\ local abs path
                drive = m.group(1) + ':\\'
                logger.debug('Absolute path on drive ' + drive)

                cmd = "Get-PSDrive -PSProvider FileSystem | % { $_.Root }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if drive not in out_lines:
                    # don't have the drive, so path won't match
                    raise FileNotFoundError(self.args['filepath'] + ' was not found')

                start = m.group(1) + ':'

                fp = filepath.split('\\')
                fp = fp[1:]
                for p in fp:
                    logger.debug('Checking if path component ' + p + ' exists')
                    cmd = "Get-Item -LiteralPath '" + start + '\\' + p + "' -ErrorAction Ignore | % { $_.Name }"
                    return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')
                    if return_code == 0 and len(out_lines) == 1:
                        logger.debug(p + ' exists')
                        start = start + '\\' + p
                    else:
                        logger.debug(p + ' does not exist; using ' + start + ' as starting point')
                        break

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['filepath'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['filepath'], l)
                    if m:
                        logger.debug(l + ' matches ' + self.args['filepath'])
                        paths.append(l)

            elif filepath.startswith(r'\\\\\?\\UNC\\'):
                # \\?\UNC\ extended UNC length path
                raise NotImplementedError('extended UNC paths are not yet supported')

            elif filepath.startswith(r'\\\\\?\\'):
                # \\?\ extended length path
                raise NotImplementedError('extended paths are not yet supported')

            elif filepath.startswith(r'\\\\\.\\'):
                # \\.\ device namespace path
                raise NotImplementedError('device paths are not yet supported')

            elif filepath.startswith(r'\\\\'):
                # \\server\share UNC path
                m = re.match(r'^\\\\([^\\]+)\\')
                if not m:
                    raise ArgumentException('Invalid UNC path: ' + filepath)
                server = m.group(1)
                logger.debug('UNC path on server ' + server)

                start = '\\\\' + server

                fp = filepath.split('\\')
                fp = fp[3:]
                for p in fp:
                    logger.debug('Checking if path component ' + p + ' exists')
                    cmd = "Get-Item -LiteralPath '" + start + '\\' + p + "' -ErrorAction Ignore | % { $_.Name }"
                    return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')
                    if return_code == 0 and len(out_lines) == 1:
                        logger.debug(p + ' exists')
                        start = start + '\\' + p
                    else:
                        logger.debug(p + ' does not exist; using ' + start + ' as starting point')
                        break

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['filepath'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['filepath'], l)
                    if m:
                        logger.debug(l + ' matches ' + self.args['filepath'])
                        paths.append(l)

            elif filepath.startswith(r'\.\.\\'):
                # ..\ relative parent path
                cmd = "(Get-Item -Path '..\\' -Verbose).FullName"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                start = out_lines[0]

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['filepath'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['filepath'], l.replace(start, '..'))
                    if m:
                        logger.debug(l + ' matches ' + self.args['filepath'])
                        paths.append(l)

            elif filepath.startswith(r'\.\\'):
                # .\ relative current path
                cmd = "(Get-Item -Path '.\\' -Verbose).FullName"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                start = out_lines[0]

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['filepath'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['filepath'], l.replace(start, '.'))
                    if m:
                        logger.debug(l + ' matches ' + self.args['filepath'])
                        paths.append(l)

            else:
                raise ArgumentException('Invalid filepath: ' + filepath)

            return paths

        else:
            raise NotImplementedError('Unknown operation not supported for ResolveFilepathCollector')
