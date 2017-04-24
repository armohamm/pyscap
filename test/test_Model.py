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

import pytest, logging
from scap.Model import Model, UnsupportedNamespaceException

logging.basicConfig(level=logging.DEBUG)

def test_parse_tag_supported():
    assert Model.parse_tag('{http://www.w3.org/XML/1998/namespace}test') == ('http://www.w3.org/XML/1998/namespace', 'test')
    assert Model.parse_tag('test') == (None, 'test')

def test_parse_tag_unsupported():
    with pytest.raises(UnsupportedNamespaceException):
        Model.parse_tag('{http://www.w3.org/XML/1998}test')

def test_load_root_classes():
    # 'http://scap.nist.gov/schema/asset-identification/1.1': 'ai_1_1',
    # 'http://scap.nist.gov/schema/asset-reporting-format/1.1': 'arf_1_1',
    # 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0': 'arf_rel_1_0',
    # 'http://cpe.mitre.org/XMLSchema/cpe/1.0': 'cpe_1_0',
    # 'http://cpe.mitre.org/dictionary/2.0': 'cpe_dict_2_3',
    # 'http://cpe.mitre.org/language/2.0': 'cpe_lang_2_3',
    # 'http://cpe.mitre.org/naming/2.0': 'cpe_naming_2_3',
    # 'http://purl.org/dc/elements/1.1/': 'dc_elements_1_1',
    # 'http://scap.nist.gov/schema/xml-dsig/1.0': 'tmsad_1_0',
    # 'http://scap.nist.gov/schema/ocil/2.0': 'ocil_2_0',
    # 'http://scap.nist.gov/schema/ocil/2': 'ocil_2_0',
    # 'http://oval.mitre.org/XMLSchema/oval-common-5': 'oval_common_5',
    # 'http://oval.mitre.org/XMLSchema/oval-definitions-5': 'oval_defs_5',
    # 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent': 'oval_defs_5_independent',
    # 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux': 'oval_defs_5_linux',
    # 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows': 'oval_defs_5_windows',
    # 'http://oval.mitre.org/XMLSchema/oval-results-5': 'oval_results_5',
    # 'http://scap.nist.gov/schema/scap/source/1.2': 'scap_source_1_2',
    # 'http://scap.nist.gov/schema/reporting-core/1.1': 'rep_core_1_1',
    # 'http://scap.nist.gov/schema/vulnerability/0.4': 'vuln_0_4',
    # 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0': 'xal_2_0',
    # 'http://checklists.nist.gov/xccdf/1.1': 'xccdf_1_1',
    # 'http://checklists.nist.gov/xccdf/1.2': 'xccdf_1_2',
    # 'http://checklists.nist.gov/xccdf-p/1.1': 'xccdf_p_1_1',
    # 'http://www.cisecurity.org/xccdf/platform/0.2.3': 'xccdf_p_0_2_3',
    # 'http://www.w3.org/1999/xhtml': 'xhtml_1999',
    # 'http://www.w3.org/1999/xlink': 'xlink_1999',
    # 'http://www.w3.org/XML/1998/namespace': 'xml',
    # 'urn:oasis:names:tc:entity:xmlns:xml:catalog': 'xml_cat_1_1',
    # 'http://www.w3.org/2000/09/xmldsig#': 'xmldsig_2000_09',
    # 'urn:oasis:names:tc:ciq:xsdschema:xNL:2.0': 'xnl_2_0',
    # 'http://www.w3.org/2001/XMLSchema': 'xs_2001',
    # 'http://www.w3.org/2001/XMLSchema-instance': 'xs_instance_2001',
    pass
