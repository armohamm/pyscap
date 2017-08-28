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

TAG_MAP = {
    '{http://www.w3.org/1999/xhtml}html': 'HtmlTag',

    '{http://www.w3.org/1999/xhtml}b': 'BTag',
    '{http://www.w3.org/1999/xhtml}br': 'BrTag',
    '{http://www.w3.org/1999/xhtml}code': 'CodeTag',
    '{http://www.w3.org/1999/xhtml}em': 'EmTag',
    '{http://www.w3.org/1999/xhtml}i': 'ITag',
    '{http://www.w3.org/1999/xhtml}li': 'LiTag',
    '{http://www.w3.org/1999/xhtml}ol': 'OlTag',
    '{http://www.w3.org/1999/xhtml}p': 'PTag',
    '{http://www.w3.org/1999/xhtml}pre': 'PreTag',
    '{http://www.w3.org/1999/xhtml}strong': 'StrongTag',
    '{http://www.w3.org/1999/xhtml}ul': 'UlTag',
}

INPUT_TYPE_ENUMERATION = [
    'text',
    'password',
    'checkbox',
    'radio',
    'submit',
    'reset',
    'file',
    'hidden',
    'image',
    'button',
]

SHAPE_ENUMERATION = [
    'rect',
    'circle',
    'poly',
    'default',
]

T_FRAME_ENUMERATION = [
    'void',
    'above',
    'below',
    'hsides',
    'lhs',
    'rhs',
    'vsides',
    'box',
    'border',
]

T_RULES_ENUMERATION = [
    'none',
    'groups',
    'rows',
    'cols',
    'all',
]

CELL_H_ALIGN_ENUMERATION = [
    'left',
    'center',
    'right',
    'justify',
    'char',
]

CELL_V_ALIGN_ENUMERATION = [
    'top',
    'middle',
    'bottom',
    'baseline',
]

SCOPE_ENUMERATION = [
    'row',
    'col',
    'rowgroup',
    'colgroup',
]
