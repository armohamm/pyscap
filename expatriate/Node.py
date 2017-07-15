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
import re

class Node(object):
    FUNCTION_LIBRARY = {

    }
    def __init__(self, parent):
        self.parent = parent
        self._document = None

    def _tokenize(self, expr):
        tokens = []

        t = ''
        for i in range(len(expr)):
            if len(t) > 0:
                if t[0] in '\'"':
                    # string literal
                    t += expr[i]
                    if expr[i] == t[0] and t[-1] != '\\':
                        tokens.append(t)
                        t = ''
                elif t[0] == '-' and (expr[i].isdigit() or expr[i] == '.'):
                    if t == '-':
                        t += expr[i]
                    elif re.fullmatch(t[1:], r'[0-9.]+'):
                        if expr[i].isdigit() or expr[i] == '.':
                            t += expr[i]
                        else:
                            tokens.append(t)
                            t = expr[i]
                    else:
                        tokens.append(t)
                        t = expr[i]
                elif t[0] == '$' and expr[i].isalpha():
                    t += expr[i]
                elif t.isspace():
                    t = expr[i]
                elif t in ':/.!<>':
                    if t + expr[i] in ['::', '//', '..', '!=', '<=', '>=']:
                        tokens.append(t + expr[i])
                        t = ''
                    else:
                        tokens.append(t)
                        t = expr[i]
                elif t in '()[]@,\'"*|+=':
                    tokens.append(t)
                    t = expr[i]
                elif expr[i] in '()[]@,\'"*|+=':
                    tokens.append(t)
                    tokens.append(expr[i])
                    t = ''
                elif expr[i].isalnum() or expr[i] == '-':
                    t += expr[i]
                else:
                    tokens.append(t)
                    t = expr[i]
            else:
                if expr[i].isspace():
                    continue
                t += expr[i]
        if t != '':
            tokens.append(t)

        return tokens

    def xpath(self, expr, version=1.0, context_position=1, context_size=1, variables={}):
        if version != 1.0:
            raise NotImplementedError('Only XPath 1.0 has been implemented')

        tokens = self._tokenize(expr)

    def get_type(self):
        raise NotImplementedError('get_type has not been implemented in class ' + self.__class__.__name__)

    def escape(self, text):
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        return text

    def unescape(self, text):
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&apos;')
        return text
