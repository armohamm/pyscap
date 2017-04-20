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
import xml.etree.ElementTree as ET
import uuid
import sys
import importlib

logger = logging.getLogger(__name__)
class Reporter(object):
    @staticmethod
    def load(hosts, args, model):
        from scap.model.xccdf_1_1.BenchmarkType import BenchmarkType as xccdf_1_1_BenchmarkType
        from scap.model.xccdf_1_2.BenchmarkType import BenchmarkType as xccdf_1_2_BenchmarkType
        from scap.model.scap_source_1_2.DataStreamCollectionElement import DataStreamCollectionElement
        if isinstance(model, xccdf_1_1_BenchmarkType):
            from scap.reporter.xccdf_1_1.BenchmarkReporter import BenchmarkReporter
            return BenchmarkReporter(hosts, args, model)
        elif isinstance(model, xccdf_1_2_BenchmarkType):
            from scap.reporter.xccdf_1_2.BenchmarkReporter import BenchmarkReporter
            return BenchmarkReporter(hosts, args, model)
        elif isinstance(model, DataStreamCollectionElement):
            from scap.reporter.scap_source_1_2.DataStreamCollectionReporter import DataStreamCollectionReporter
            return DataStreamCollectionReporter(hosts, args, model)
        else:
            raise NotImplementedError('Reporting with ' + model.__class__.__name__ + ' model has not been implemented')

    def __init__(self, hosts, args, model):
        self.hosts = hosts
        self.args = args
        self.model = model

    def report(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
