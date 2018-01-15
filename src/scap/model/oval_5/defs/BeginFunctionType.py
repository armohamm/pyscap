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

from expatriate.model.Model import Model
from expatriate.model.decorators import *
from expatriate.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='character', type=StringType, required=True)
@element(local_name='object_component', list='components', cls=defer_class_load('scap.model.oval_5.defs.ObjectComponentType', 'ObjectComponentType'))
@element(local_name='variable_component', list='components', cls=defer_class_load('scap.model.oval_5.defs.VariableComponentType', 'VariableComponentType'))
@element(local_name='literal_component', list='components', cls=defer_class_load('scap.model.oval_5.defs.LiteralComponentType', 'LiteralComponentType'))
@element(local_name='arithmetic', list='components', cls=defer_class_load('scap.model.oval_5.defs.ArithmeticFunctionType', 'ArithmeticFunctionType'))
@element(local_name='begin', list='components', cls=defer_class_load('scap.model.oval_5.defs.BeginFunctionType', 'BeginFunctionType'))
@element(local_name='concat', list='components', cls=defer_class_load('scap.model.oval_5.defs.ConcatFunctionType', 'ConcatFunctionType'))
@element(local_name='count', list='components', cls=defer_class_load('scap.model.oval_5.defs.CountFunctionType', 'CountFunctionType'))
@element(local_name='end', list='components', cls=defer_class_load('scap.model.oval_5.defs.EndFunctionType', 'EndFunctionType'))
@element(local_name='escape_regex', list='components', cls=defer_class_load('scap.model.oval_5.defs.EscapeRegexFunctionType', 'EscapeRegexFunctionType'))
@element(local_name='split', list='components', cls=defer_class_load('scap.model.oval_5.defs.SplitFunctionType', 'SplitFunctionType'))
@element(local_name='substring', list='components', cls=defer_class_load('scap.model.oval_5.defs.SubstringFunctionType', 'SubstringFunctionType'))
@element(local_name='time_difference', list='components', cls=defer_class_load('scap.model.oval_5.defs.TimeDifferenceFunctionType', 'TimeDifferenceFunctionType'))
@element(local_name='unique', list='components', cls=defer_class_load('scap.model.oval_5.defs.UniqueFunctionType', 'UniqueFunctionType'))
@element(local_name='regex_capture', list='components', cls=defer_class_load('scap.model.oval_5.defs.RegexCaptureFunctionType', 'RegexCaptureFunctionType'))
@element(local_name='glob_to_regex', list='components', cls=defer_class_load('scap.model.oval_5.defs.GlobToRegexFunctionType', 'GlobToRegexFunctionType'))
class BeginFunctionType(Model):
    pass
