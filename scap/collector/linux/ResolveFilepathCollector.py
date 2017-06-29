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
from scap.model.oval_5.defs.independent.FileBehaviors import FileBehaviors

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

        # TODO the max_depth behavior is not allowed with a filepath entity
        # recurse
        # TODO the recurse_direction behavior is not allowed with a filepath entity
        # the recurse_file_system behavior MUST not be set to 'defined' when a pattern match is used with a filepath entity
        if args['value_operations']['filepath'] == 'pattern match' and args['behavior_recurse_file_system'] == 'defined':
            raise ArgumentException('ResolveFilepathCollector behavior_recurse_file_system set to defined with pattern match operation')

    def collect(self):
        if self.args['value_operations']['filepath'] == 'equals':
            filepath = self.args['filepath'].replace('"', '\\"')
            cmd = 'find `dirname "' + filepath + '"` -wholename "' + filepath + '"'
            return_code, out_lines, err_lines = self.host.exec_command(cmd)
            if return_code != 0 or len(out_lines) == 0:
                raise FileNotFoundError(self.args['filepath'] + ' was not found')

            return out_lines

        elif self.args['value_operations']['filepath'] == 'not equal':
            raise NotImplementedError('not equal operation not supported for ResolveFilepathCollector')

        elif self.args['value_operations']['filepath'] == 'case insensitive equals':
            filepath = self.args['filepath'].replace('"', '\\"')
            cmd = 'find `dirname "' + filepath + '"` -iwholename "' + filepath + '"'
            return_code, out_lines, err_lines = self.host.exec_command(cmd)
            if return_code != 0 or len(out_lines) == 0:
                raise FileNotFoundError(self.args['filepath'] + ' was not found')

            return out_lines

        elif self.args['value_operations']['filepath'] == 'case insensitive not equal':
            raise NotImplementedError('not equal operation not supported for ResolveFilepathCollector')

        elif self.args['value_operations']['filepath'] == 'pattern match':
            filepath = self.args['filepath'].replace("'", "\\'")
            cmd = 'locate --regex \'' + filepath + "'"
            return_code, out_lines, err_lines = self.host.exec_command(cmd)
            if return_code != 0:
                raise FileNotFoundError('Unable to find pattern ' + self.args['filepath'] + ' in locatedb')
            return out_lines

        else:
            raise NotImplementedError('Unknown operation not supported for ResolveFilepathCollector')
