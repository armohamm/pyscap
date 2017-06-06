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
from scap.Host import Host

# import all the classes in the package
import scap.model.oval_5.defs.linux as pkg
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

logging.basicConfig(level=logging.DEBUG)

host = Host.load('localhost')

def test_EntityStateProtocolType_parse():
    assert EntityStateProtocolType().parse_value('ETH_P_802_3') == 'ETH_P_802_3'

def test_EntityStateRpmVerifyResultType_parse():
    assert EntityStateRpmVerifyResultType().parse_value('not performed') == 'not performed'

def test_def():
    test_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<oval_definitions xmlns:unix-def="http://oval.mitre.org/XMLSchema/oval-definitions-5#unix" xmlns:ind-def="http://oval.mitre.org/XMLSchema/oval-definitions-5#independent" xmlns:lin-def="http://oval.mitre.org/XMLSchema/oval-definitions-5#linux" xmlns:oval="http://oval.mitre.org/XMLSchema/oval-common-5" xmlns="http://oval.mitre.org/XMLSchema/oval-definitions-5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://oval.mitre.org/XMLSchema/oval-definitions-5#unix http://oval.mitre.org/language/version5.8/ovaldefinition/complete/unix-definitions-schema.xsd
	http://oval.mitre.org/XMLSchema/oval-definitions-5#independent http://oval.mitre.org/language/version5.8/ovaldefinition/complete/independent-definitions-schema.xsd
	http://oval.mitre.org/XMLSchema/oval-definitions-5#linux http://oval.mitre.org/language/version5.8/ovaldefinition/complete/linux-definitions-schema.xsd
	http://oval.mitre.org/XMLSchema/oval-definitions-5 http://oval.mitre.org/language/version5.8/ovaldefinition/complete/oval-definitions-schema.xsd
	http://oval.mitre.org/XMLSchema/oval-common-5 http://oval.mitre.org/language/version5.8/ovaldefinition/complete/oval-common-schema.xsd">
	<generator>
		<oval:product_name>Text Editors</oval:product_name>
		<oval:schema_version>5.8</oval:schema_version>
		<oval:timestamp>2013-12-17T12:00:00-04:00</oval:timestamp>
	</generator>
	<definitions>
    		<definition class="compliance" id="oval:gov.nist.usgcb.rhel:def:20000" version="2">
    			<metadata>
    				<title>Ensure that /tmp has its own partition or logical volume</title>
    				<affected family="unix">
    					<platform>Red Hat Enterprise Linux 5</platform>
    				</affected>
    				<reference ref_id="CCE-14161-4" source="CCE"/>
    				<description>The /tmp directory is a world-writable directory used for temporary ﬁle storage. Verify that it has its own partition or logical volume.</description>
    			</metadata>
    			<criteria>
    				<!-- <criterion test_ref="oval:gov.nist.usgcb.rhel:tst:20000" comment="Check in /etc/fstab for a /tmp mount point"/> -->
    				<criterion test_ref="oval:gov.nist.usgcb.rhel:tst:2000000" comment="Check if /tmp partition exists"/>
    			</criteria>
    		</definition>
	</definitions>
	<tests>
		<lin-def:partition_test id="oval:gov.nist.usgcb.rhel:tst:2000000" comment="Check if /tmp partition exists" check_existence="at_least_one_exists" check="at least one" version="1">
			<lin-def:object object_ref="oval:gov.nist.usgcb.rhel:obj:144120"/>
		</lin-def:partition_test>
    </tests>
    <objects>
		<lin-def:partition_object version="1" id="oval:gov.nist.usgcb.rhel:obj:144120">
			<lin-def:mount_point>/tmp</lin-def:mount_point>
		</lin-def:partition_object>
    </objects>
	<states>
	</states>
	<variables>
	</variables>
</oval_definitions>'''
