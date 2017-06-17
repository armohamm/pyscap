#!/usr/bin/env python

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

from scap.Model import Model

Model.register_namespace('scap.model.ai_1_1', 'http://scap.nist.gov/schema/asset-identification/1.1')
Model.register_namespace('scap.model.arf_1_1', 'http://scap.nist.gov/schema/asset-reporting-format/1.1')
Model.register_namespace('scap.model.arf_rel_1_0', 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0')
Model.register_namespace('scap.model.cpe_1_0', 'http://cpe.mitre.org/XMLSchema/cpe/1.0')
Model.register_namespace('scap.model.cpe_dict_2_3', 'http://cpe.mitre.org/dictionary/2.0')
Model.register_namespace('scap.model.cpe_lang_2_3', 'http://cpe.mitre.org/language/2.0')
Model.register_namespace('scap.model.cpe_naming_2_3', 'http://cpe.mitre.org/naming/2.0')
Model.register_namespace('scap.model.dc_elements_1_1', 'http://purl.org/dc/elements/1.1/')
Model.register_namespace('scap.model.tmsad_1_0', 'http://scap.nist.gov/schema/xml-dsig/1.0')
Model.register_namespace('scap.model.ocil_2_0', 'http://scap.nist.gov/schema/ocil/2.0')
Model.register_namespace('scap.model.ocil_2_0', 'http://scap.nist.gov/schema/ocil/2')
Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
Model.register_namespace('scap.model.oval_5.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
Model.register_namespace('scap.model.oval_5.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
Model.register_namespace('scap.model.oval_5.dir', 'http://oval.mitre.org/XMLSchema/oval-directives-5')
Model.register_namespace('scap.model.oval_5.sc', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5')
Model.register_namespace('scap.model.oval_5.sc.linux', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux')
Model.register_namespace('scap.model.oval_5.var', 'http://oval.mitre.org/XMLSchema/oval-variables-5')
Model.register_namespace('scap.model.scap_source_1_2', 'http://scap.nist.gov/schema/scap/source/1.2')
Model.register_namespace('scap.model.rep_core_1_1', 'http://scap.nist.gov/schema/reporting-core/1.1')
Model.register_namespace('scap.model.vuln_0_4', 'http://scap.nist.gov/schema/vulnerability/0.4')
Model.register_namespace('scap.model.xal_2_0', 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')
Model.register_namespace('scap.model.xccdf_1_1', 'http://checklists.nist.gov/xccdf/1.1')
Model.register_namespace('scap.model.xccdf_1_2', 'http://checklists.nist.gov/xccdf/1.2')
Model.register_namespace('scap.model.xccdf_p_1_1', 'http://checklists.nist.gov/xccdf-p/1.1')
Model.register_namespace('scap.model.xccdf_p_0_2_3', 'http://www.cisecurity.org/xccdf/platform/0.2.3')
Model.register_namespace('scap.model.xhtml', 'http://www.w3.org/1999/xhtml')
Model.register_namespace('scap.model.xlink', 'http://www.w3.org/1999/xlink')
Model.register_namespace('scap.model.xml_cat_1_1', 'urn:oasis:names:tc:entity:xmlns:xml:catalog')
Model.register_namespace('scap.model.xmldsig_2000_09', 'http://www.w3.org/2000/09/xmldsig#')
Model.register_namespace('scap.model.xnl_2_0', 'urn:oasis:names:tc:ciq:xsdschema:xNL:2.0')
