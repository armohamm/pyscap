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
from scap.model.oval_defs_5.DateTimeFormatEnumeration import DATE_TIME_FORMAT_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class TimeDifferenceFunctionType(Model):
    MODEL_MAP = {
        'elements': [
            #TODO <xsd:sequence minOccurs="1" maxOccurs="2">
            # from ComponentGroup
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'object_component', 'append': 'components', 'class': 'ObjectComponentType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'variable_component', 'append': 'components', 'class': 'VariableComponentType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'literal_component', 'append': 'components', 'class': 'LiteralComponentType'},# from ComponentGroup/FunctionGroup
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'arithmetic', 'append': 'components', 'class': 'ArithmeticFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'begin', 'append': 'components', 'class': 'BeginFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'concat', 'append': 'components', 'class': 'ConcatFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'count', 'append': 'components', 'class': 'CountFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'end', 'append': 'components', 'class': 'EndFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'escape_regex', 'append': 'components', 'class': 'EscapeRegexFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'split', 'append': 'components', 'class': 'SplitFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'substring', 'append': 'components', 'class': 'SubstringFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'time_difference', 'append': 'components', 'class': 'TimeDifferenceFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'unique', 'append': 'components', 'class': 'UniqueFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'regex_capture', 'append': 'components', 'class': 'RegexCaptureFunctionType'},
            {'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'glob_to_regex', 'append': 'components', 'class': 'GlobToRegexFunctionType'},
        ],
        'attributes': {
            'format_1': {'enum': DATE_TIME_FORMAT_ENUMERATION, 'default': 'year_month_day'},
            'format_2': {'enum': DATE_TIME_FORMAT_ENUMERATION, 'default': 'year_month_day'},
        },
    }
