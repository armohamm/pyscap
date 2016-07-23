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

from scap.model.Simple import Simple
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Asset(Simple):
    def __init__(self):
        super(Asset, self).__init__()

        self.asset = None

        self.tag_name = '{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset'
        self.required_attributes.append('id')

    def get_sub_elements(self):
        sub_els = super(Asset, self).get_sub_elements()

        import scap.model.ai_1_1.Asset
        from scap.model.arf_1_1.RemoteResource import RemoteResource
        if isinstance(self.asset, scap.model.ai_1_1.Asset.Asset) or isinstance(self.asset, RemoteResource):
            sub_els.append(self.asset.to_xml())
        else:
            logger.critical('Asset must define an asset or remote-resource')
            import sys
            sys.exit()

        return sub_els
