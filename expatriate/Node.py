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

class Node(object):
    def __init__(self, parent):
        self.parent = parent
        self._document = None

    def produce(self):
        raise NotImplementedError('produce has not been implemented in class ' + self.__class__.__name__)

    def get_xpath(self, expr, version=1.0):
        raise NotImplementedError('get_xpath has not been implemented in class ' + self.__class__.__name__)

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
