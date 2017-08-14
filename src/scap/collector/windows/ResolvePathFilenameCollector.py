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
class ResolvePathFilenameCollector(Collector):
    def __init__(self, host, args):
        super(ResolvePathFilenameCollector, self).__init__(host, args)

        if 'path' not in args:
            raise ArgumentException('ResolvePathFilenameCollector requires path argument')

        if 'filename' not in args:
            raise ArgumentException('ResolvePathFilenameCollector requires filename argument')

        for i in ('value_datatypes', 'value_masks', 'value_operations'):
            if i not in args:
                raise ArgumentException('ResolvePathFilenameCollector requires ' + i + ' argument')

        if args['value_datatypes']['path'] != 'string':
            raise ArgumentException('ResolvePathFilenameCollector requires string path')

        if args['value_datatypes']['filename'] != 'string':
            raise ArgumentException('ResolvePathFilenameCollector requires string filename')

        # NOTE: operation should be already validated by EntityObjectType

        # TODO the max_depth behavior MUST not be used when a pattern match is used with a path entity
        # TODO the recurse behavior MUST not be used when a pattern match is used with a path entity
        # TODO the recurse_direction behavior MUST not be used when a pattern match is used with a path entity
        # the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a path entity
        if args['value_operations']['path'] == 'pattern match' and args['behavior_recurse_file_system'] == 'defined':
            raise ArgumentException('ResolvePathFilenameCollector behavior_recurse_file_system set to defined with path pattern match operation')

    def collect(self):
        if self.args['value_operations']['path'] in ['equals', 'case insensitive equals']:
            # check if path exists
            col = self.host.load_collector('DirectoryExistsCollector', {'path': self.args['path']})
            if not col.collect():
                raise FileNotFoundError(self.args['path'] + ' was not found')

            paths = [self.args['path']]

        elif self.args['value_operations']['path'] in ['not equal', 'case insensitive not equal']:
            raise NotImplementedError(self.args['value_operations']['path'] + ' operation not supported for ResolvePathFilenameCollector')

        elif self.args['value_operations']['path'] == 'pattern match':
            path = self.args['path']
            logger.debug('Matching pattern ' + path)

            # strip off leading ^ or trailing $ as they are assumed
            if path.startswith('^'):
                path = path[1:]
            if path.endswith('$'):
                path = path[:-1]

            paths = []
            m = re.match(r'^([a-zA-Z]):\\', path)
            if m:
                # C:\ local abs path
                drive = m.group(1) + ':\\'
                logger.debug('Absolute path on drive ' + drive)

                cmd = "Get-PSDrive -PSProvider FileSystem | % { $_.Root }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if drive not in out_lines:
                    # don't have the drive, so path won't match
                    raise FileNotFoundError(self.args['path'] + ' was not found')

                start = m.group(1) + ':'

                fp = path.split('\\')
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
                    raise FileNotFoundError(self.args['path'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['path'], l)
                    if m:
                        logger.debug(l + ' matches ' + self.args['path'])
                        paths.append(l)

            elif path.startswith(r'\\\\\?\\UNC\\'):
                # \\?\UNC\ extended UNC length path
                raise NotImplementedError('extended UNC paths are not yet supported')

            elif path.startswith(r'\\\\\?\\'):
                # \\?\ extended length path
                raise NotImplementedError('extended paths are not yet supported')

            elif path.startswith(r'\\\\\.\\'):
                # \\.\ device namespace path
                raise NotImplementedError('device paths are not yet supported')

            elif path.startswith(r'\\\\'):
                # \\server\share UNC path
                m = re.match(r'^\\\\([^\\]+)\\')
                if not m:
                    raise ArgumentException('Invalid UNC path: ' + path)
                server = m.group(1)
                logger.debug('UNC path on server ' + server)

                start = '\\\\' + server

                fp = path.split('\\')
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
                    raise FileNotFoundError(self.args['path'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['path'], l)
                    if m:
                        logger.debug(l + ' matches ' + self.args['path'])
                        paths.append(l)

            elif path.startswith(r'\.\.\\'):
                # ..\ relative parent path
                cmd = "(Get-Item -Path '..\\' -Verbose).FullName"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                start = out_lines[0]

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['path'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['path'], l.replace(start, '..'))
                    if m:
                        logger.debug(l + ' matches ' + self.args['path'])
                        paths.append(l)

            elif path.startswith(r'\.\\'):
                # .\ relative current path
                cmd = "(Get-Item -Path '.\\' -Verbose).FullName"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                start = out_lines[0]

                logger.debug('Recursing from ' + start)
                cmd = "Get-ChildItem -LiteralPath '" + start + "' -Recurse -ErrorAction Ignore | % { $_.FullName }"
                return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')

                if return_code != 0 or len(out_lines) < 1:
                    raise FileNotFoundError(self.args['path'] + ' was not found')

                for l in out_lines:
                    m = re.fullmatch(self.args['path'], l.replace(start, '.'))
                    if m:
                        logger.debug(l + ' matches ' + self.args['path'])
                        paths.append(l)

            else:
                raise ArgumentException('Invalid path: ' + path)

        # TODO imp behavior_windows_view

        filepaths = []
        for path in paths:
            if self.args['behavior_recurse_file_system'] == 'local' and path.startswith('\\\\'):
                continue

            if self.args['value_operations']['filename'] in ['equals', 'case insensitive equals']:
                filepaths.extend(self.search_path_for(path, self.args['filename'], '-eq', self.args['behavior_max_depth'], self.args['behavior_recurse_direction']))

            elif self.args['value_operations']['filename'] in ['not equal', 'case insensitive not equal']:
                raise NotImplementedError(self.args['value_operations']['filename'] + ' operation not supported for ResolvePathFilenameCollector')

            elif self.args['value_operations']['filename'] == 'pattern match':
                filepaths.extend(self.search_path_for(path, self.args['filename'], '-match', self.args['behavior_max_depth'], self.args['behavior_recurse_direction']))

            else:
                raise NotImplementedError('Unknown operation not supported for ResolvePathFilenameCollector filename')

        return filepaths

    def search_path_for(self, path, filename, operator, remaining_depth, direction):
        logger.debug('Looking for ' + filename + ' in ' + path)

        if remaining_depth == 0:
            return []

        if direction == 'up':
            raise NotImplementedError('Upward recursion is not yet implemented')

        # TODO implement link traversal validation

        if remaining_depth == -1:
            cmd = "Get-ChildItem -Recurse -LiteralPath '" + path.replace("'", "\\'") + "'"
        else:
            cmd = "Get-ChildItem -LiteralPath '" + path.replace("'", "\\'") + "'"
        cmd = cmd + " | % {"
        cmd = cmd + "$_.FullName + ',' + "
        cmd = cmd + "($_.Mode[0] -eq 'd') + ',' + "
        cmd = cmd + "($_.Name " + operator + " '" + filename.replace("'", "\\'") + "')"
        cmd = cmd + " }"
        return_code, out_lines, err_lines = self.host.exec_command('powershell -Command "' + cmd.replace('\"', '\\"') + '"')
        if return_code != 0:
            raise FileNotFoundError('Error finding ' + filename + ' in ' + path)

        filepaths = []
        for l in out_lines:
            logger.debug('Got ' + l + ' in ' + path)
            fullname, is_dir, matches = l.rsplit(',', 3)
            is_dir = is_dir == 'True'
            matches = matches == 'True'
            if is_dir and direction == 'down' and remaining_depth >= 1:
                filepaths.extend(self.search_path_for(fullname, filename, operator, remaining_depth - 1, direction))

            if matches:
                filepaths.append(fullname)

        return filepaths
