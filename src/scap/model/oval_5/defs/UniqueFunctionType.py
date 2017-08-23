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

import logging

from scap.model.decorators import *
from scap.Model import Model

logger = logging.getLogger(__name__)

@element(local_name='object_component', list='components', cls='ObjectComponentType')
@element(local_name='variable_component', list='components', cls='VariableComponentType')
@element(local_name='literal_component', list='components', cls='LiteralComponentType')
@element(local_name='arithmetic', list='components', cls='ArithmeticFunctionType')
@element(local_name='begin', list='components', cls='BeginFunctionType')
@element(local_name='concat', list='components', cls='ConcatFunctionType')
@element(local_name='count', list='components', cls='CountFunctionType')
@element(local_name='end', list='components', cls='EndFunctionType')
@element(local_name='escape_regex', list='components', cls='EscapeRegexFunctionType')
@element(local_name='split', list='components', cls='SplitFunctionType')
@element(local_name='substring', list='components', cls='SubstringFunctionType')
@element(local_name='time_difference', list='components', cls='TimeDifferenceFunctionType')
@element(local_name='unique', list='components', cls='UniqueFunctionType')
@element(local_name='regex_capture', list='components', cls='RegexCaptureFunctionType')
@element(local_name='glob_to_regex', list='components', cls='GlobToRegexFunctionType')
class UniqueFunctionType(Model):
    pass
