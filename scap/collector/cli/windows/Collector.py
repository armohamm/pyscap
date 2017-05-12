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

from scap.collector.CliCollector import CliCollector

logger = logging.getLogger(__name__)
class Collector(CliCollector):
    def collect(self):
        from scap.collector.cli.windows.UniqueIdCollector import UniqueIdCollector
        UniqueIdCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.CpeCollector import CpeCollector
        CpeCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.FqdnCollector import FqdnCollector
        FqdnCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.HostnameCollector import HostnameCollector
        HostnameCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.NetworkConnectionCollector import NetworkConnectionCollector
        NetworkConnectionCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.NetworkServiceCollector import NetworkServiceCollector
        NetworkServiceCollector(self.host, self.args).collect()

        from scap.collector.cli.windows.IdentityCollector import IdentityCollector
        IdentityCollector(self.host, self.args).collect()
