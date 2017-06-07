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

import importlib
import logging
import pytest
import pkgutil

from scap.Model import Model

# import all the classes in the package
import scap.model.oval_5.defs.windows as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
Model.register_namespace('scap.model.oval_5.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
Model.register_namespace('scap.model.oval_5.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
Model.register_namespace('scap.model.oval_5.defs.unix', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#unix')

logging.basicConfig(level=logging.DEBUG)

def test_EntityObjectCmdletVerbType_parse():
    assert EntityObjectCmdletVerbType().parse_value('Request') == 'Request'

def test_EntityObjectGUIDType_parse():
    assert EntityObjectGUIDType().parse_value('{12345678-1234-1234-1234-1234567890ab}') == '{12345678-1234-1234-1234-1234567890ab}'

def test_EntityObjectNamingContextType_parse():
    assert EntityObjectNamingContextType().parse_value('configuration') == 'configuration'

def test_EntityObjectProtocolType_parse():
    assert EntityObjectProtocolType().parse_value('UDP') == 'UDP'

def test_EntityObjectRegistryHiveType_parse():
    assert EntityObjectRegistryHiveType().parse_value('HKEY_CURRENT_CONFIG') == 'HKEY_CURRENT_CONFIG'

def test_EntityObjectSystemMetricIndexType_parse():
    assert EntityObjectSystemMetricIndexType().parse_value('SM_CXDOUBLECLK') == 'SM_CXDOUBLECLK'

def test_EntityObjectUserRightType_parse():
    assert EntityObjectUserRightType().parse_value('SE_LOAD_DRIVER_NAME') == 'SE_LOAD_DRIVER_NAME'

def test_EntityStateAddrTypeType_parse():
    assert EntityStateAddrTypeType().parse_value('MIB_IPADDR_DYNAMIC') == 'MIB_IPADDR_DYNAMIC'

def test_EntityStateAdstypeType_parse():
    assert EntityStateAdstypeType().parse_value('ADSTYPE_LARGE_INTEGER') == 'ADSTYPE_LARGE_INTEGER'

def test_EntityStateAuditType_parse():
    assert EntityStateAuditType().parse_value('AUDIT_NONE') == 'AUDIT_NONE'

def test_EntityStateCmdletVerbType_parse():
    assert EntityStateCmdletVerbType().parse_value('Request') == 'Request'

def test_EntityStateDriveTypeType_parse():
    assert EntityStateDriveTypeType().parse_value('DRIVE_CDROM') == 'DRIVE_CDROM'

def test_EntityStateFileTypeType_parse():
    assert EntityStateFileTypeType().parse_value('FILE_TYPE_PIPE') == 'FILE_TYPE_PIPE'

def test_EntityStateGUIDType_parse():
    assert EntityStateGUIDType().parse_value('{12345678-1234-1234-1234-1234567890ab}') == '{12345678-1234-1234-1234-1234567890ab}'

def test_EntityStateInterfaceTypeType_parse():
    assert EntityStateInterfaceTypeType().parse_value('MIB_IF_TYPE_LOOPBACK') == 'MIB_IF_TYPE_LOOPBACK'

def test_EntityStateNamingContextType_parse():
    assert EntityStateNamingContextType().parse_value('configuration') == 'configuration'

def test_EntityStateNTUserAccountTypeType_parse():
    assert EntityStateNTUserAccountTypeType().parse_value('domain') == 'domain'

def test_EntityStatePeSubsystemType_parse():
    assert EntityStatePeSubsystemType().parse_value('IMAGE_SUBSYSTEM_POSIX_CUI') == 'IMAGE_SUBSYSTEM_POSIX_CUI'

def test_EntityStatePeTargetMachineType_parse():
    assert EntityStatePeTargetMachineType().parse_value('IMAGE_FILE_MACHINE_M68K') == 'IMAGE_FILE_MACHINE_M68K'

def test_EntityStateProtocolType_parse():
    assert EntityStateProtocolType().parse_value('UDP') == 'UDP'

def test_EntityStateRegistryHiveType_parse():
    assert EntityStateRegistryHiveType().parse_value('HKEY_CURRENT_USER') == 'HKEY_CURRENT_USER'

def test_EntityStateRegistryTypeType_parse():
    assert EntityStateRegistryTypeType().parse_value('reg_multi_sz') == 'reg_multi_sz'

def test_EntityStateServiceControlsAcceptedType_parse():
    assert EntityStateServiceControlsAcceptedType().parse_value('SERVICE_ACCEPT_POWEREVENT') == 'SERVICE_ACCEPT_POWEREVENT'

def test_EntityStateServiceCurrentStateType_parse():
    assert EntityStateServiceCurrentStateType().parse_value('SERVICE_RUNNING') == 'SERVICE_RUNNING'

def test_EntityStateServiceStartTypeType_parse():
    assert EntityStateServiceStartTypeType().parse_value('SERVICE_DEMAND_START') == 'SERVICE_DEMAND_START'

def test_EntityStateServiceTypeType_parse():
    assert EntityStateServiceTypeType().parse_value('SERVICE_KERNEL_DRIVER') == 'SERVICE_KERNEL_DRIVER'

def test_EntityStateSharedResourceTypeType_parse():
    assert EntityStateSharedResourceTypeType().parse_value('STYPE_PRINTQ_SPECIAL') == 'STYPE_PRINTQ_SPECIAL'

def test_EntityStateSystemMetricIndexType_parse():
    assert EntityStateSystemMetricIndexType().parse_value('SM_CXCURSOR') == 'SM_CXCURSOR'

def test_EntityStateUserRightType_parse():
    assert EntityStateUserRightType().parse_value('SE_CREATE_PAGEFILE_NAME') == 'SE_CREATE_PAGEFILE_NAME'

def test_EntityStateWindowsViewType_parse():
    assert EntityStateWindowsViewType().parse_value('64_bit') == '64_bit'
