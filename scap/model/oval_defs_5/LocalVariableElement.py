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

from scap.model.oval_defs_5.Variable import Variable
import logging

logger = logging.getLogger(__name__)
class LocalVariableElement(VariableType):
    MODEL_MAP = {
        'tag_name': 'local_variable',
        'elements': [
            # from ComponentGroup
            {'tag_name': 'object_component', 'list': 'components', 'class': 'ObjectComponentType'},
            {'tag_name': 'variable_component', 'list': 'components', 'class': 'VariableComponentType'},
            {'tag_name': 'literal_component', 'list': 'components', 'class': 'LiteralComponentType'},# from ComponentGroup/FunctionGroup
            {'tag_name': 'arithmetic', 'list': 'components', 'class': 'ArithmeticFunctionType'},
            {'tag_name': 'begin', 'list': 'components', 'class': 'BeginFunctionType'},
            {'tag_name': 'concat', 'list': 'components', 'class': 'ConcatFunctionType'},
            {'tag_name': 'count', 'list': 'components', 'class': 'CountFunctionType'},
            {'tag_name': 'end', 'list': 'components', 'class': 'EndFunctionType'},
            {'tag_name': 'escape_regex', 'list': 'components', 'class': 'EscapeRegexFunctionType'},
            {'tag_name': 'split', 'list': 'components', 'class': 'SplitFunctionType'},
            {'tag_name': 'substring', 'list': 'components', 'class': 'SubstringFunctionType'},
            {'tag_name': 'time_difference', 'list': 'components', 'class': 'TimeDifferenceFunctionType'},
            {'tag_name': 'unique', 'list': 'components', 'class': 'UniqueFunctionType'},
            {'tag_name': 'regex_capture', 'list': 'components', 'class': 'RegexCaptureFunctionType'},
            {'tag_name': 'glob_to_regex', 'list': 'components', 'class': 'GlobToRegexFunctionType'},
        ],
    }
