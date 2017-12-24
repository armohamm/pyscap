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

ELEMENT_MAP = {
    ('http://checklists.nist.gov/xccdf/1.1', 'Benchmark'): 'BenchmarkType',
}

CHECK_OPERATOR_ENUMERATION = [
    'AND',
    'OR',
]

CHECK_OPERATOR_AND_TABLE = {
    # ------------------------------------------------------
    #    AND             || P | F | U | E | N | K | S | I ||
    # -------------------||-------------------------------||
    #           Pass (P) || P | F | U | E | P | P | P | P ||
    'pass': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'pass',
        'notchecked': 'pass',
        'notselected': 'pass',
        'informational': 'pass',
    },
    #           Fail (F) || F | F | F | F | F | F | F | F ||
    'fail': {
        'pass': 'fail',
        'fail': 'fail',
        'unknown': 'fail',
        'error': 'fail',
        'notapplicable': 'fail',
        'notchecked': 'fail',
        'notselected': 'fail',
        'informational': 'fail',
    },
    #        Unknown (U) || U | F | U | U | U | U | U | U ||
    'unknown': {
        'pass': 'unknown',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'unknown',
        'notapplicable': 'unknown',
        'notchecked': 'unknown',
        'notselected': 'unknown',
        'informational': 'unknown',
    },
    #          Error (E) || E | F | U | E | E | E | E | E ||
    'error': {
        'pass': 'error',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'error',
        'notchecked': 'error',
        'notselected': 'error',
        'informational': 'error',
    },
    #  Notapplicable (N) || P | F | U | E | N | N | N | N ||
    'notapplicable': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notapplicable',
        'notselected': 'notapplicable',
        'informational': 'notapplicable',
    },
    #     Notchecked (K) || P | F | U | E | N | K | K | K ||
    'notchecked': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notchecked',
        'informational': 'notchecked',
    },
    #    Notselected (S) || P | F | U | E | N | K | S | S ||
    'notselected': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notselected',
        'informational': 'notselected',
    },
    #  Informational (I) || P | F | U | E | N | K | S | I ||
    'informational': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notselected',
        'informational': 'informational',
    },
}

def check_operator_AND(values):
    value = values[0]
    for i in range(1, len(values)):
        value = CHECK_OPERATOR_AND_TABLE[value][values[i]]
    return value

CHECK_OPERATOR_OR_TABLE = {
    # ------------------------------------------------------
    #     OR             || P | F | U | E | N | K | S | I ||
    # -------------------||-------------------------------||
    #           Pass (P) || P | P | P | P | P | P | P | P ||
    'pass': {
        'pass': 'pass',
        'fail': 'pass',
        'unknown': 'pass',
        'error': 'pass',
        'notapplicable': 'pass',
        'notchecked': 'pass',
        'notselected': 'pass',
        'informational': 'pass',
    },
    #           Fail (F) || P | F | U | E | F | F | F | F ||
    'fail': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'fail',
        'notchecked': 'fail',
        'notselected': 'fail',
        'informational': 'fail',
    },
    #        Unknown (U) || P | U | U | U | U | U | U | U ||
    'unknown': {
        'pass': 'pass',
        'fail': 'unknown',
        'unknown': 'unknown',
        'error': 'unknown',
        'notapplicable': 'unknown',
        'notchecked': 'unknown',
        'notselected': 'unknown',
        'informational': 'unknown',
    },
    #          Error (E) || P | E | U | E | E | E | E | E ||
    'error': {
        'pass': 'pass',
        'fail': 'error',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'error',
        'notchecked': 'error',
        'notselected': 'error',
        'informational': 'error',
    },
    #  Notapplicable (N) || P | F | U | E | N | N | N | N ||
    'notapplicable': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notapplicable',
        'notselected': 'notapplicable',
        'informational': 'notapplicable',
    },
    #     Notchecked (K) || P | F | U | E | N | K | K | K ||
    'notchecked': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notchecked',
        'informational': 'notchecked',
    },
    #    Notselected (S) || P | F | U | E | N | K | S | S ||
    'notselected': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notselected',
        'informational': 'notselected',
    },
    #  Informational (I) || P | F | U | E | N | K | S | I ||
    'informational': {
        'pass': 'pass',
        'fail': 'fail',
        'unknown': 'unknown',
        'error': 'error',
        'notapplicable': 'notapplicable',
        'notchecked': 'notchecked',
        'notselected': 'notselected',
        'informational': 'informational',
    },
}
def check_operator_OR(values):
    value = values[0]
    for i in range(1, len(values)):
        value = CHECK_OPERATOR_OR_TABLE[value][values[i]]
    return value

# ---------------------------------------
# NOT || P | F | U | E | N | K | S | I ||
# ----||-------------------------------||
#     || F | P | U | E | N | K | S | I ||
# ---------------------------------------
def check_operator_negate(value):
    if value == 'pass':
        return 'fail'
    elif value == 'fail':
        return 'pass'
    else:
        return value

OVAL_XLATE = {
    'true': 'pass',
    'false': 'fail',
    'error': 'error',
    'unknown': 'unknown',
    'not evaluated': 'notchecked',
    'not applicable': 'notapplicable',
}

def oval_translate(value):
    return OVAL_XLATE[value]

OCIL_XLATE = {
    'PASS': 'pass',
    'FAIL': 'fail',
    'ERROR': 'error',
    'UNKNOWN': 'unknown',
    'NOT_TESTED': 'notchecked',
    'NOT_APPLICABLE': 'notapplicable',
}

def ocil_translate(value):
    return OCIL_XLATE[value]

CHECK_SYSTEM_ENUMERATION = [
    'http://oval.mitre.org/XMLSchema/oval-definitions-5',
    'http://scap.nist.gov/schema/ocil/2.0',
    'http://scap.nist.gov/schema/ocil/2',
]

FACT_SYSTEM_ENUMERATION = [
    'urn:scap:fact:asset:identifier:mac',
    # Ethernet media access control address (should be sent as a pair with
    # the IP or IPv6 address to ensure uniqueness)
    'urn:scap:fact:asset:identifier:ipv4',
    # Internet Protocol version 4 address
    'urn:scap:fact:asset:identifier:ipv6',
    # Internet Protocol version 6 address
    'urn:scap:fact:asset:identifier:host_name',
    # Host name of the asset, if assigned
    'urn:scap:fact:asset:identifier:fqdn',
    # Fully qualified domain name
    'urn:scap:fact:asset:identifier:ein',
    # Equipment identification number or other inventory tag number
    'urn:scap:fact:asset:identifier:pki:',
    # X.509 PKI certificate for the asset (encoded in Base-64)
    'urn:scap:fact:asset:identifier:pki:thumbprint',
    # SHA.1 hash of the PKI certification for the asset (encoded in Base-64)
    'urn:scap:fact:asset:identifier:guid',
    # Globally unique identifier for the asset
    'urn:scap:fact:asset:identifier:ldap',
    # LDAP directory string (distinguished name) of the asset, if assigned
    'urn:scap:fact:asset:identifier:active_directory',
    # Active Directory realm to which the asset belongs, if assigned
    'urn:scap:fact:asset:identifier:nis_domain',
    # NIS domain of the asset, if assigned
    'urn:scap:fact:asset:environmental_information:owning_organization',
    # Organization that tracks the asset on its inventory
    'urn:scap:fact:asset:environmental_information:current_region',
    # Geographic region where the asset is located
    'urn:scap:fact:asset:environmental_information:administration_unit',
    # Name of the organization that does system administration for the asset
    'urn:scap:fact:asset:environmental_information:administration_poc:title',
    # Title (e.g., Mr, Ms, Col) of the system administrator for an asset]
    'urn:scap:fact:asset:environmental_information:administration_poc:e-mail',
    # E-mail address of the system administrator for the asset
    'urn:scap:fact:asset:environmental_information:administration_poc:first_name',
    # First name of the system administrator for the asset
    'urn:scap:fact:asset:environmental_information:administration_poc:last_name',
    # Last name of the system administrator for the asset
]

FIX_STRATEGY_ENUMERATION = [
    'unknown',
    # strategy not defined (default for forward compatibility for XCCDF 1.0)
    'configure',
    # adjust target config or settings
    'patch',
    # apply a patch, hotfix, or update
    'policy',
    # remediation by changing policies/procedures
    'disable',
    # turn off or deinstall something
    'enable',
    # turn on or install something
    'restrict',
    # adjust permissions or ACLs
    'update',
    # install upgrade or update the system
    'combination',
    # combo of two or more of the above
]

FIX_SYSTEM_ENUMERATION = [
    'urn:xccdf:fix:commands',
    # This specifies that the content of the fix element is a list of target
    # system commands; executed in order, the commands should bring the
    # target system into compliance with the Rule.

    'urn:xccdf:fix:urls',
    # This specifies that the content of the fix element is a list of one or
    # more URLs. The resources identified by the URLs should be applied to
    # bring the system into compliance with the Rule.

    'urn:xccdf:fix:script:sh', # Bourne shell
    'urn:xccdf:fix:script:csh', # C Shell
    'urn:xccdf:fix:script:perl', # Perl
    'urn:xccdf:fix:script:batch', # Windows batch script
    'urn:xccdf:fix:script:python', # Python and all Python-based scripting languages
    'urn:xccdf:fix:script:vbscript', # Visual Basic Script (VBS)
    'urn:xccdf:fix:script:javascript', # Javascript (ECMAScript, JScript)
    'urn:xccdf:fix:script:tcl', # Tcl and all Tcl-based scripting languages
    # A URN of this form specifies that the content of the fix element is a
    # script written in the given language. Executing the script should
    # bring the target system into compliance with the Rule.

    'urn:xccdf:fix:patch:microsoft',
    'urn:xccdf:fix:patch:redhat',
    # A URN of this form specifies that the content of the fix element is a
    # patch identifier, in proprietary format as defined by the vendor.
]

IDENT_SCHEME_ENUMERATION = [
    'http://cve.mitre.org/',
    # MITRE's Common Vulnerabilities and Exposures the identifier value
    # should be a CVE number or CVE candidate number.
    'http://cce.mitre.org/',
    # This specifies the Common Configuration Enumeration identifier scheme.
    'http://www.cert.org/',
    # CERT Coordination Center the identifier value should be a CERT
    # advisory identifier (e.g. CA-2004-02).
    'http://www.us-cert.gov/cas/techalerts/',
    # US-CERT technical cyber security alerts the identifier value should
    # be a technical cyber security alert ID (e.g. TA05-189A)
    'http://www.kb.cert.org/',
    # US-CERT vulnerability notes database the identifier values should be
    # a vulnerability note number (e.g. 709220).
    'http://iase.disa.mil/IAalerts/',
    # DISA Information Assurance Vulnerability Alerts (IAVA) the
    # identifier value should be a DOD IAVA identifier.
]

INTERFACE_HINT_ENUMERATION = [
    'choice',
    'textline',
    'text',
    'date',
    'datetime',
]

MESSAGE_SEVERITY_ENUMERATION = [
    'error',
    'warning',
    'info',
]

RATING_ENUMERATION = [
    'unknown',
    # rating unknown or impossible to estimate (default for forward
    # compatibility for XCCDF 1.0)
    'low',
    # little or no potential for disruption, very modest complexity
    'medium',
    # some chance of minor disruption,  substantial complexity
    'high',
    # likely to cause serious disruption, very complex
]

RESULT_ENUMERATION = [
    'pass',
    # the test passed, target complies w/ benchmark
    'fail',
    # the test failed, target does not comply
    'error',
    # an error occurred and test could not complete, or the test does not apply
    # to this plaform
    'unknown',
    # could not tell what happened, results  with this status are not to be
    # scored
    'notapplicable',
    # Rule did not apply to test target
    'fixed',
    # rule failed, but was later fixed (score as pass)
    'notchecked',
    # Rule did not cause any evaluation by the checking engine (role of
    # "unchecked")
    'notselected',
    # Rule was not selected in the Benchmark, and therefore was not checked
    # (selected="0")
    'informational',
    # Rule was evaluated by the checking engine, but isn't to be scored (role of
    # "unscored")
]

ROLE_ENUMERATION = [
    'full',
    # if the rule is selected, then check it and let the result contribute to
    # the score and appear in reports (default, for compatibility for XCCDF
    # 1.0).
    'unscored',
    # check the rule, and include the results in  any report, but do not include
    # the result in  score computations (in the default scoring model the same
    # effect can be achieved with weight=0)
    'unchecked',
    # don't check the rule, just force the result status to 'unknown'.  Include
    # the rule's  information in any reports.
]

SCORING_MODEL_ENUMERATION = [
    'urn:xccdf:scoring:default',
    # This specifies the default (XCCDF 1.0) scoring model.
    'urn:xccdf:scoring:flat',
    # This specifies the flat, weighted scoring model.
    'urn:xccdf:scoring:flat-unweighted',
    # This specifies the flat scoring model with weights ignored (all
    # weights set to 1).
    'urn:xccdf:scoring:absolute',
    # This specifies the absolute (1 or 0) scoring model.
]

SEVERITY_ENUMERATION = [
    'unknown',
    # severity not defined (default, for forward compatibility from XCCDF 1.0)
    'info',
    # rule is informational only, failing the rule does not imply failure to
    # conform to the security guidance of the benchmark. (usually would also
    # have a weight of 0)
    'low',
    # not a serious problem
    'medium',
    # fairly serious problem
    'high',
    # a grave or critical problem
]

STATUS_ENUMERATION = [
    'accepted',
    'deprecated',
    'draft',
    'incomplete',
    'interim',
]

VALUE_OPERATOR_ENUMERATION = [
    'equals',
    'not equal',
    'greater than',
    'less than',
    'greater than or equal',
    'less than or equal',
    'pattern match',
]

VALUE_TYPE_ENUMERATION = [
    'number',
    'string',
    'boolean',
]

WARNING_CATEGORY_ENUMERATION = [
    'general',
    # broad or general-purpose warning (default for compatibility for XCCDF 1.0)
    'functionality',
    # warning about possible impacts to functionality or operational features
    'performance',
    # warning about changes to target system performance or throughput
    'hardware',
    # warning about hardware restrictions or possible impacts to hardware
    'legal',
    # warning about legal implications
    'regulatory',
    # warning about regulatory obligations or compliance implications
    'management',
    # warning about impacts to the mgmt or administration of the target system
    'audit',
    # warning about impacts to audit or logging
    'dependency',
    # warning about dependencies between this Rule and other parts of the target
    # system, or version dependencies.
]
