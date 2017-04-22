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
TEST_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'dpkginfo_test', 'map': 'tests', 'class': 'DpkgInfoTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'iflisteners_test', 'map': 'tests', 'class': 'IfListenersTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'inetlisteningservers_test', 'map': 'tests', 'class': 'InetListeningServersTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'partition_test', 'map': 'tests', 'class': 'PartitionTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpminfo_test', 'map': 'tests', 'class': 'RpmInfoTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifyfile_test', 'map': 'tests', 'class': 'RpmVerifyFileTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifypackage_test', 'map': 'tests', 'class': 'RpmVerifyPackageTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverify_test', 'map': 'tests', 'class': 'RpmVerifyTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxboolean_test', 'map': 'tests', 'class': 'SeLinuxBooleanTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxsecuritycontext_test', 'map': 'tests', 'class': 'SeLinuxSecurityContextTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'slackwarepkginfo_test', 'map': 'tests', 'class': 'SlackwarePkgInfoTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitdependency_test', 'map': 'tests', 'class': 'SystemDUnitDependencyTestElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitproperty_test', 'map': 'tests', 'class': 'SystemDUnitPropertyTestElement', 'min': 0, 'max': None},
}
OBJECT_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'dpkginfo_object', 'map': 'objects', 'class': 'DpkgInfoObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'iflisteners_object', 'map': 'objects', 'class': 'IfListenersObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'inetlisteningservers_object', 'map': 'objects', 'class': 'InetListeningServersObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'partition_object', 'map': 'objects', 'class': 'PartitionObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpminfo_object', 'map': 'objects', 'class': 'RpmInfoObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifyfile_object', 'map': 'objects', 'class': 'RpmVerifyFileObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifypackage_object', 'map': 'objects', 'class': 'RpmVerifyPackageObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverify_object', 'map': 'objects', 'class': 'RpmVerifyObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxboolean_object', 'map': 'objects', 'class': 'SeLinuxBooleanObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxsecuritycontext_object', 'map': 'objects', 'class': 'SeLinuxSecurityContextObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'slackwarepkginfo_object', 'map': 'objects', 'class': 'SlackwarePkgInfoObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitdependency_object', 'map': 'objects', 'class': 'SystemDUnitDependencyObjectElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitproperty_object', 'map': 'objects', 'class': 'SystemDUnitPropertyObjectElement', 'min': 0, 'max': None},
}
STATE_MAP = {
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'dpkginfo_state', 'map': 'states', 'class': 'DpkgInfoStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'iflisteners_state', 'map': 'states', 'class': 'IfListenersStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'inetlisteningservers_state', 'map': 'states', 'class': 'InetListeningServersStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'partition_state', 'map': 'states', 'class': 'PartitionStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpminfo_state', 'map': 'states', 'class': 'RpmInfoStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifyfile_state', 'map': 'states', 'class': 'RpmVerifyFileStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverifypackage_state', 'map': 'states', 'class': 'RpmVerifyPackageStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'rpmverify_state', 'map': 'states', 'class': 'RpmVerifyStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxboolean_state', 'map': 'states', 'class': 'SeLinuxBooleanStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'selinuxsecuritycontext_state', 'map': 'states', 'class': 'SeLinuxSecurityContextStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'slackwarepkginfo_state', 'map': 'states', 'class': 'SlackwarePkgInfoStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitdependency_state', 'map': 'states', 'class': 'SystemDUnitDependencyStateElement', 'min': 0, 'max': None},
    {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux', 'tag_name': 'systemdunitproperty_state', 'map': 'states', 'class': 'SystemDUnitPropertyStateElement', 'min': 0, 'max': None},
}
