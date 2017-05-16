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

import datetime
import importlib
import logging
import pkgutil
import pytest

# import all the classes in the package
import scap.model.xs
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=scap.model.xs.__path__):
    mod = importlib.import_module(scap.model.xs.__name__ + '.' + m_name, scap.model.xs.__name__)
    globals()[m_name] = getattr(mod, m_name)

logging.basicConfig(level=logging.DEBUG)

def test_any_simple_type():
    pass

def test_any_type():
    pass

def test_any_uri():
    pass

def test_base64_binary():
    pass

def test_boolean():
    i = Boolean()

    v = i.parse_value('1')
    assert isinstance(v, bool)
    assert v == True
    assert i.produce_value(v) == 'True'

    v = i.parse_value('0')
    assert isinstance(v, bool)
    assert v == False

    v = i.parse_value('true')
    assert isinstance(v, bool)
    assert v == True

    v = i.parse_value('false')
    assert isinstance(v, bool)
    assert v == False

def test_byte():
    i = Byte()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_date():
    i = Date()

    v = i.parse_value('2017-05-16Z')
    assert isinstance(v, datetime.date)

def test_date_time():
    i = DateTime()

    v = i.parse_value('2017-05-16T12:00:00Z')
    assert isinstance(v, datetime.datetime)

def test_decimal():
    i = Decimal()

    v = i.parse_value('1.1')
    assert isinstance(v, float)
    assert v > 1.0 and v <= 1.1
    assert i.produce_value(v).startswith('1.')

def test_double():
    i = Double()

    v = i.parse_value('1.1')
    assert isinstance(v, float)
    assert v > 1.0 and v <= 1.1
    assert i.produce_value(v).startswith('1.')

# def test_duration():
#     i = Duration()
#
#     v = i.parse_value('5 days')

# def test_entities():
#     pass
#
# def test_entity():
#     pass

def test_float():
    i = Float()

    v = i.parse_value('1.1')
    assert isinstance(v, float)
    assert v > 1.0 and v <= 1.1
    assert i.produce_value(v).startswith('1.')

def test_g_day():
    pass

def test_g_month():
    pass

def test_g_month_day():
    pass

def test_g_year():
    pass

def test_g_year_month():
    pass

def test_hex_binary():
    pass

def test_id():
    i = ID()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_idref():
    i = IDREF()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_idrefs():
    pass

def test_int():
    i = Int()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_integer():
    i = Integer()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_language():
    pass

def test_long():
    i = Long()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_name():
    i = Name()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_nc_name():
    i = NCName()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_negative_integer():
    i = NegativeInteger()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_nm_token():
    i = NMTOKEN()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_nm_tokens():
    pass

def test_non_negative_integer():
    i = NonNegativeInteger()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_non_positive_integer():
    i = NonPositiveInteger()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_normalized_string():
    i = NormalizedString()

    v = i.parse_value('test_id_4')
    assert isinstance(v, str)

def test_notation():
    i = NOTATION()

    v = i.parse_value('test')
    assert isinstance(v, str)

def test_positive_integer():
    i = PositiveInteger()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_q_name():
    i = QName()

    v = i.parse_value('test')
    assert isinstance(v, str)

def test_short():
    i = Short()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_string():
    i = String()

    v = i.parse_value('test')
    assert isinstance(v, str)

def test_time():
    i = Time()

    v = i.parse_value('12:00:00')
    assert isinstance(v, datetime.time)

def test_token():
    i = Token()

    v = i.parse_value('test')
    assert isinstance(v, str)

def test_unsigned_byte():
    i = UnsignedByte()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_unsigned_int():
    i = UnsignedInt()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_unsigned_long():
    i = UnsignedLong()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'

def test_unsigned_short():
    i = UnsignedShort()

    v = i.parse_value('255')
    assert isinstance(v, int)
    assert v == 255
    assert i.produce_value(v) == '255'
