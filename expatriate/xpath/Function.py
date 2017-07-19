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
import math
import re

logger = logging.getLogger(__name__)
class Function(object):
    # Node Set Functions
    def f_last(args, context_node, context_position, context_size, variables):
        return context_size

    def f_position(args, context_node, context_position, context_size, variables):
        return context_position

    def f_count(args, context_node, context_position, context_size, variables):
        return len(args[0])

    def f_id(args, context_node, context_position, context_size, variables):
        ids = []
        if isinstance(args, list): # node list
            for n in args:
                ids.extend(re.split(r'[\x20\x09\x0D\x0A]+', n.get_string_value()))
        else:
            ids = re.split(r'[\x20\x09\x0D\x0A]+', f_string(args))

        ns = []
        for i in ids:
            if i in context_node._document._element_index:
                ns.append(context_node._document._element_index[i])
        return s

    def f_local_name(args, context_node, context_position, context_size, variables):
        pass

    def f_namespace_uri(args, context_node, context_position, context_size, variables):
        pass

    def f_name(args, context_node, context_position, context_size, variables):
        pass

    # String Functions

    def f_string(args, context_node, context_position, context_size, variables):
        # TODO If the argument is omitted, it defaults to a node-set with the context node as its only member.
        if isinstance(args, float):
            if args == math.nan:
                return 'NaN'
            elif args == -math.inf:
                return '-Infinity'
            elif args == math.inf:
                return 'Infinity'
            else:
                return str(args)
        elif args == True:
            return 'true'
        elif args == False:
            return 'false'
        else:
            return str(args)

    def f_concat(args, context_node, context_position, context_size, variables):
        r = ''
        for a in args:
            r += a
        return r

    def f_starts_with(args, context_node, context_position, context_size, variables):
        return args[0].startswith(args[1])

    def f_contains(args, context_node, context_position, context_size, variables):
        return args[1] in args[0]

    def f_substring_before(args, context_node, context_position, context_size, variables):
        return args[0].partition(args[1])[0]

    def f_substring_after(args, context_node, context_position, context_size, variables):
        return args[0].partition(args[1])[2]

    def f_substring(args, context_node, context_position, context_size, variables):
        if args[1] == -math.inf:
            return ''

        arg_1 = Function.f_round((args[1]), context_node, context_position, context_size, variables)
        start = arg_1 - 1
        if start < 0:
            start = 0
        logger.debug('Substring start: ' + str(start))

        if len(args) > 2:
            if args[2] == -math.inf:
                return ''
            elif args[2] == math.inf:
                return args[0][start:]

            end = arg_1 - 1 + Function.f_round(args[2], context_node, context_position, context_size, variables)
            logger.debug('Substring end: ' + str(end))

            return args[0][start:end]
        else:
            return args[0][start:]

    def f_string_length(args, context_node, context_position, context_size, variables):
        return len(args)

    def f_normalize_space(args, context_node, context_position, context_size, variables):
        # TODO If the argument is omitted, it defaults to the context node converted to a string, in other words the string-value of the context node.
        args = args.strip('\x20\x09\x0D\x0A')
        return re.sub(r'[\x20\x09\x0D\x0A]+', ' ', args)

    def f_translate(args, context_node, context_position, context_size, variables):
        s = args[0]
        from_ = args[1]
        to = args[2]
        if len(to) > len(from_):
            to = to[:len(from_)]
        delete = from_[len(to):]
        from_ = from_[:len(to)]

        return s.translate(str.maketrans(from_, to, delete))

    # Boolean Functions

    def f_boolean(args, context_node, context_position, context_size, variables):
        if isinstance(args, int) or isinstance(args, float):
            if args != 0 and args != math.nan:
                return True
            else:
                return False
        # TODO if nodeset; return len(set) > 0
        elif isinstance(args, str):
            return len(args) > 0
        else:
            return bool(args)

    def f_not(args, context_node, context_position, context_size, variables):
        return not args

    def f_true(args, context_node, context_position, context_size, variables):
        return True

    def f_false(args, context_node, context_position, context_size, variables):
        return False

    def f_lang(args, context_node, context_position, context_size, variables):
        pass

    # Number Functions

    def f_number(args, context_node, context_position, context_size, variables):
        if isinstance(args, str):
            if '.' in args:
                return float(args)
            else:
                return int(args)
        elif args == True:
            return 1
        elif args == False:
            return 0
        # TODO a node-set is first converted to a string as if by a call to the string function and then converted in the same way as a string argument
        elif isinstance(args, int) or isinstance(args, float):
            return args
        else:
            return int(args)

    def f_sum(args, context_node, context_position, context_size, variables):
        pass

    def f_floor(args, context_node, context_position, context_size, variables):
        return math.floor(args)

    def f_ceiling(args, context_node, context_position, context_size, variables):
        return math.ceil(args)

    def f_round(args, context_node, context_position, context_size, variables):
        if args == math.nan:
            return math.nan
        elif args == math.inf:
            return math.inf
        elif args == - math.inf:
            return - math.inf
        return round(args)

    FUNCTIONS = {
        # Node Set Functions
        'last': f_last,
        'position': f_position,
        'count': f_count,
        'id': f_id,
        'local-name': f_local_name,
        'namespace-uri': f_namespace_uri,
        'name': f_name,

        # String Functions
        'string': f_string,
        'concat': f_concat,
        'starts-with': f_starts_with,
        'contains': f_contains,
        'substring-before': f_substring_before,
        'substring-after': f_substring_after,
        'substring': f_substring,
        'string-length': f_string_length,
        'normalize-space': f_normalize_space,
        'translate': f_translate,

        # Boolean Functions
        'boolean': f_boolean,
        'not': f_not,
        'true': f_true, # x is to swallow the empty expression
        'false': f_false, # x is to swallow the empty expression
        'lang': f_lang,

        # Number Functions
        'number': f_number,
        'sum': f_sum,
        'floor': f_floor,
        'ceiling': f_ceiling,
        'round': f_round,
    }

    def __init__(self, name, function):
        self.name = name
        self.function = function
        self.children = []

    def evaluate(self, context_node, context_position, context_size, variables):
        child_evals = []
        for c in self.children:
            v = c.evaluate(context_node, context_position, context_size, variables)
            logger.debug('Evaluated child of ' + str(self) + ' to ' + str(v))
            child_evals.append(v)
        return self.function(*child_evals, context_node, context_position, context_size, variables)

    def __str__(self):
        return 'Function ' + self.name + ': ' + str([str(x) for x in self.children])
