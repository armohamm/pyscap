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

from scap.model.oval_5 import *
from scap.model.oval_5.defs import *
from scap.model.oval_5.defs.unix import *
from scap.model.oval_5.defs.EntityStateStringType import EntityStateStringType

logger = logging.getLogger(__name__)
class EntityStateRoutingTableFlagsType(EntityStateStringType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    # TODO restrict to ROUTING_TABLE_FLAGS_ENUMERATION

    # Name                           Linux    Solaris    HPUX    Mac OS    FreeBSD    AIX
    # UP                             U        U          U       U         U          U
    # GATEWAY                        G        G          G       G         G          G
    # HOST                           H        H          H       H         H          H
    # REINSTATE                      R
    # DYNAMIC                        D        D                  D         D          D
    # MODIFIED                       M                           M         M          M
    # ADDRCONF                       A        A
    # CACHE                          C                                                e
    # REJECT                         !                           R         R          R
    # REDUNDANT                               M (>=9)
    # SETSRC                                  S
    # BROADCAST                               B                  b         b          b
    # LOCAL                                   L                                       l
    # PROTOCOL_1                                                 1         1          1
    # PROTOCOL_2                                                 2         2          2
    # PROTOCOL_3                                                 3         3          3
    # BLACK_HOLE                                                 B         B
    # CLONING                                                    C         C          c
    # PROTOCOL_CLONING                                           c         c
    # INTERFACE_SCOPE                                            I
    # LINK_LAYER                                                 L         L          L
    # MULTICAST                                                  m                    m
    # STATIC                                                     S         S          S
    # WAS_CLONED                                                 W         W          W
    # XRESOLVE                                                   X         X
    # USABLE                                                                          u
    # PINNED                                                                          P
    # ACTIVE_DEAD_GATEWAY_DETECTION                                                   A (>=5.1)
