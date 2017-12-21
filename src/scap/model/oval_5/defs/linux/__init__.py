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
TAG_MAP = {
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'dpkginfo_test'): 'DpkgInfoTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'iflisteners_test'): 'IfListenersTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'inetlisteningservers_test'): 'InetListeningServersTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'partition_test'): 'PartitionTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpminfo_test'): 'RpmInfoTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifyfile_test'): 'RpmVerifyFileTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifypackage_test'): 'RpmVerifyPackageTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverify_test'): 'RpmVerifyTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxboolean_test'): 'SeLinuxBooleanTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxsecuritycontext_test'): 'SeLinuxSecurityContextTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'slackwarepkginfo_test'): 'SlackwarePkgInfoTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitdependency_test'): 'SystemDUnitDependencyTestElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitproperty_test'): 'SystemDUnitPropertyTestElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'dpkginfo_object'): 'DpkgInfoObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'iflisteners_object'): 'IfListenersObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'inetlisteningservers_object'): 'InetListeningServersObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'partition_object'): 'PartitionObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpminfo_object'): 'RpmInfoObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifyfile_object'): 'RpmVerifyFileObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifypackage_object'): 'RpmVerifyPackageObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverify_object'): 'RpmVerifyObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxboolean_object'): 'SeLinuxBooleanObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxsecuritycontext_object'): 'SeLinuxSecurityContextObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'slackwarepkginfo_object'): 'SlackwarePkgInfoObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitdependency_object'): 'SystemDUnitDependencyObjectElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitproperty_object'): 'SystemDUnitPropertyObjectElement',

    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'dpkginfo_state'): 'DpkgInfoStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'iflisteners_state'): 'IfListenersStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'inetlisteningservers_state'): 'InetListeningServersStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'partition_state'): 'PartitionStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpminfo_state'): 'RpmInfoStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifyfile_state'): 'RpmVerifyFileStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverifypackage_state'): 'RpmVerifyPackageStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'rpmverify_state'): 'RpmVerifyStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxboolean_state'): 'SeLinuxBooleanStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'selinuxsecuritycontext_state'): 'SeLinuxSecurityContextStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'slackwarepkginfo_state'): 'SlackwarePkgInfoStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitdependency_state'): 'SystemDUnitDependencyStateElement',
    ('http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'systemdunitproperty_state'): 'SystemDUnitPropertyStateElement',
}
