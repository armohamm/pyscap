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

from scap.model.oval_5.sc import *
from scap.model.oval_5.defs.linux import RPM_VERIFY_RESULT_ENUMERATION, PROTOCOL_ENUMERATION

TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}dpkginfo_item': 'DpkgInfoItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}iflisteners_item': 'IfListenersItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}inetlisteningserver_item': 'InetListeningServerItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}partition_item': 'PartitionItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}rpminfo_item': 'RpmInfoItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}rpmverify_item': 'RpmVerifyItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}rpmverifyfile_item': 'RpmVerifyFileItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}rpmverifypackage_item': 'RpmVerifyPackageItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}selinuxboolean_item': 'SeLinuxBooleanItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}selinuxsecuritycontext_item': 'SeLinuxSecurityContextItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}slackwarepkginfo_item': 'SlackwarePkgInfoItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}systemdunitdependency_item': 'SystemDUnitDependencyItemElement',
    '{http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux}systemdunitproperty_item': 'SystemDUnitPropertyItemElement',
}
