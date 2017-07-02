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
        if self.args['value_operations']['path'] == 'equals':
            # check if path exists
            col = self.host.load_collector('DirectoryExistsCollector', {'path': self.args['path']})
            if not col.collect():
                raise FileNotFoundError(self.args['path'] + ' was not found')

            paths = [self.args['path']]

        elif self.args['value_operations']['path'] == 'not equal':
            raise NotImplementedError('not equal operation not supported for ResolvePathFilenameCollector')

        elif self.args['value_operations']['path'] == 'case insensitive equals':
            # check if path exists
            col = self.host.load_collector('DirectoryExistsCollector', {'path': self.args['path'], 'case_insensitive': True})
            if not col.collect():
                raise FileNotFoundError(self.args['path'] + ' was not found')

            paths = [self.args['path']]

        elif self.args['value_operations']['path'] == 'case insensitive not equal':
            raise NotImplementedError('not equal operation not supported for ResolvePathFilenameCollector')

        elif self.args['value_operations']['path'] == 'pattern match':
            path = self.args['path'].replace('\"', '\\"')

            cmd = 'find -H / -type d 2>/dev/null | grep --perl-regexp --line-regexp --colour=never "' + path + '"'
            logger.debug(cmd)
            return_code, out_lines, err_lines = self.host.exec_command(cmd)
            if return_code != 0 or len(out_lines) < 1:
                raise FileNotFoundError('Unable to find pattern ' + self.args['path'] + '; using base dir ' + basedir + '; regex ' + regex)

            paths = []
            for d in out_lines:
                col = self.host.load_collector('DirectoryExistsCollector', {'path': d})
                if col.collect():
                    paths.append(d)

        else:
            raise NotImplementedError('Unknown operation not supported for ResolvePathFilenameCollector')

        opts = []
        if self.args['behavior_recurse_direction'] == 'down':
            if self.args['behavior_max_depth'] == -1:
                pass
            elif self.args['behavior_max_depth'] >= 0:
                opts.append('-maxdepth ' + str(self.args['behavior_max_depth']))
            else:
                raise ArgumentException('ResolvePathFilenameCollector arg behavior_max_depth is invalid ' + str(self.args['behavior_max_depth']))

            if self.args['behavior_recurse_file_system'] == 'defined':
                opts.append('-xdev')
            elif self.args['behavior_recurse_file_system'] == 'local':
                logger.warn('Local/remote filesystem detection is not yet implemented')
            elif self.args['behavior_recurse_file_system'] == 'all':
                pass
            else:
                raise ArgumentException('ResolvePathFilenameCollector arg behavior_recurse_file_system is invalid ' + str(self.args['behavior_recurse_file_system']))

        elif self.args['behavior_recurse_direction'] == 'none':
            pass
        elif self.args['behavior_recurse_direction'] == 'up':
            raise NotImplementedError('Upward recursion is not yet implemented')
        else:
            raise ArgumentException('ResolvePathFilenameCollector arg behavior_recurse_direction is invalid ' + str(self.args['behavior_recurse_direction']))

        # NOTE: behavior_windows_view is ignored

        filepaths = []
        filename = self.args['filename'].replace("'", "\\'")
        for path in paths:
            path = path.replace("'", "\\'")
            if self.args['value_operations']['filename'] == 'equals':
                if self.args['behavior_recurse'] == 'directories':
                    # TODO might want to use -H
                    cmd = 'find \'' + path + '\' ' + ' '.join(opts) + ' -name \'' + filename + '\''
                elif self.args['behavior_recurse'] in ('symlinks', 'symlinks and directories'):
                    cmd = 'find -L \'' + path + '\' ' + ' '.join(opts) + ' -name \'' + filename + '\''
                else:
                    raise ArgumentException('ResolvePathFilenameCollector arg behavior_recurse is invalid ' + str(self.args['behavior_recurse']))

                return_code, out_lines, err_lines = self.host.exec_command(cmd)
                if return_code != 0:
                    raise FileNotFoundError('Unable to find ' + filename + ' in ' + path)

                filepaths.extend(out_lines)

            elif self.args['value_operations']['filename'] == 'not equal':
                raise NotImplementedError('not equal operation not supported for ResolvePathFilenameCollector')

            elif self.args['value_operations']['filename'] == 'case insensitive equals':
                if self.args['behavior_recurse'] == 'directories':
                    # TODO might want to use -H
                    cmd = 'find \'' + path + '\' ' + ' '.join(opts) + ' -iname \'' + filename + '\''
                elif self.args['behavior_recurse'] in ('symlinks', 'symlinks and directories'):
                    cmd = 'find -L \'' + path + '\' ' + ' '.join(opts) + ' -iname \'' + filename + '\''
                else:
                    raise ArgumentException('ResolvePathFilenameCollector arg behavior_recurse is invalid ' + str(self.args['behavior_recurse']))

                return_code, out_lines, err_lines = self.host.exec_command(cmd)
                if return_code != 0:
                    raise FileNotFoundError('Unable to find ' + filename + ' in ' + path)

                filepaths.extend(out_lines)

            elif self.args['value_operations']['filename'] == 'case insensitive not equal':
                raise NotImplementedError('not equal operation not supported for ResolvePathFilenameCollector')

            elif self.args['value_operations']['filename'] == 'pattern match':
                if self.args['behavior_recurse'] == 'directories':
                    # TODO might want to use -H
                    cmd = 'find \'' + path + '\' ' + ' '.join(opts) + ' -regex \'' + filename + '\''
                elif self.args['behavior_recurse'] in ('symlinks', 'symlinks and directories'):
                    cmd = 'find -L \'' + path + '\' ' + ' '.join(opts) + ' -regex \'' + filename + '\''
                else:
                    raise ArgumentException('ResolvePathFilenameCollector arg behavior_recurse is invalid ' + str(self.args['behavior_recurse']))

                return_code, out_lines, err_lines = self.host.exec_command(cmd)
                if return_code != 0:
                    raise FileNotFoundError('Unable to find ' + filename + ' in ' + path)

                filepaths.extend(out_lines)

            else:
                raise NotImplementedError('Unknown operation not supported for ResolvePathFilenameCollector filename')

        return filepaths
