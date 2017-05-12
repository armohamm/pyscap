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

import datetime
import logging
import sys

from scap.collector.Checker import Checker

logger = logging.getLogger(__name__)
class BenchmarkChecker(Checker):
    def __init__(self, host, args, model):
        super(BenchmarkChecker, self).__init__(host, args, model)

        self.model.noticing()

        self.model.selected_profiles = []
        if args['profile'] is None or len(args['profile']) == 0:
            # check them all
            self.model.selected_profiles.extend(self.model.profiles.keys())
        else:
            for profile in args['profile']:
                if profile not in list(self.model.profiles.keys()):
                    raise ValueError('Unable to select non-existent profile: ' + profile + ' Available profiles: ' + str(self.profiles.keys()))
                self.model.selected_profiles.append(profile)

        self.model.resolve()

    def collect(self):
        self.model.process(self.host)
