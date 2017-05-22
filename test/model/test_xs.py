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
for m in pkgutil.iter_modules(path=scap.model.xs.__path__):
    mod = importlib.import_module(scap.model.xs.__name__ + '.' + m.name, scap.model.xs.__name__)
    globals()[m.name] = getattr(mod, m.name)

logging.basicConfig(level=logging.DEBUG)

def test_seven_property_model_init():
    spm = SevenPropertyModel()
    for i in (spm.year, spm.month, spm.day, spm.hour, spm.minute, spm.second, spm.timezoneOffset):
        assert i is None

    spm = SevenPropertyModel(year=2017, month=5, day=22)
    assert spm.year == 2017
    assert spm.month == 5
    assert spm.day == 22
    for i in (spm.hour, spm.minute, spm.second, spm.timezoneOffset):
        assert i is None

    spm = SevenPropertyModel(hour=12, minute=42, second=42)
    assert spm.hour == 12
    assert spm.minute == 42
    assert spm.second == 42
    for i in (spm.year, spm.month, spm.day, spm.timezoneOffset):
        assert i is None

def test_seven_property_model_eq():
    assert SevenPropertyModel(hour=12, minute=42, second=42) == SevenPropertyModel(hour=12, minute=42, second=42)
    assert SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42) == \
        SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42)

def test_seven_property_model_ne():
    assert SevenPropertyModel(hour=12, minute=42, second=42) != SevenPropertyModel(hour=13, minute=42, second=42)

def test_seven_property_model_to_date():
    assert SevenPropertyModel(year=2017, month=5, day=22).to_date() == datetime.date(year=2017, month=5, day=22)
    # TODO test timezone offsets

def test_seven_property_model_to_datetime():
    assert SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42).to_datetime() == datetime.datetime(year=2017, month=5, day=22, hour=12, minute=42, second=42)
    # TODO test timezone offsets

def test_seven_property_model_to_time():
    assert SevenPropertyModel(hour=12, minute=42, second=42).to_time() == datetime.time(hour=12, minute=42, second=42)
    # TODO test timezone offsets

# def test_any_simple_type():
#     pass
#
# def test_any_type():
#     pass
#
# def test_any_uri():
#     pass
#
def test_base64_binary_parse():
    assert Base64Binary().parse_value(b'FPucA9l+') == b'\x14\xfb\x9c\x03\xd9\x7e'
    assert Base64Binary().parse_value(b'FPucA9k=') == b'\x14\xfb\x9c\x03\xd9'
    assert Base64Binary().parse_value(b'FPucAw==') == b'\x14\xfb\x9c\x03'

def test_base64_binary_produce():
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03\xd9\x7e') == b'FPucA9l+'
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03\xd9') == b'FPucA9k='
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03') == b'FPucAw=='

def test_boolean_parse():
    assert Boolean().parse_value('1') == True
    assert Boolean().parse_value('0') == False
    assert Boolean().parse_value('true') == True
    assert Boolean().parse_value('false') == False

def test_boolean_produce():
    assert Boolean().produce_value(True) == 'True'
    assert Boolean().produce_value(False) == 'False'

def test_byte_parse():
    assert Byte().parse_value('127') == 127

def test_byte_produce():
    assert Byte().produce_value(127) == '127'

def test_date_parse():
    assert Date().parse_value('2017-05-16Z') == SevenPropertyModel(year=2017, month=5, day=16, timezoneOffset=0)

def test_date_produce():
    assert Date().produce_value(SevenPropertyModel(year=2017, month=5, day=16, timezoneOffset=0)) == '2017-05-16Z'

def test_date_time_parse():
    assert DateTime().parse_value('2017-05-16T12:42:42Z') == SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)

def test_date_time_produce():
    assert DateTime().produce_value(SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)) == '2017-05-16T12:42:42Z'

def test_decimal_parse():
    assert Decimal().parse_value('1.1') == 1.1

def test_decimal_produce():
    assert Decimal().produce_value(1.1) == '1.1'

def test_double_parse():
    assert Double().parse_value('1.1') == 1.1

def test_double_produce():
    assert Double().produce_value(1.1) == '1.1'

# def test_duration():
#     i = Duration()
#
#     v = i.parse_value('5 days')

def test_entities_parse():
    assert ENTITIES().parse_value('blah0 blah1 blah2') == ('blah0', 'blah1', 'blah2')

    with pytest.raises(ValueError):
        ENTITIES().parse_value('')

def test_entities_produce():
    assert ENTITIES().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_entity_parse():
    assert ENTITY().parse_value('test_id_4') == 'test_id_4'

def test_entity_produce():
    assert ENTITY().produce_value('test_id_4') == 'test_id_4'

def test_float_parse():
    assert Float().parse_value('1.1') == 1.1

def test_float_produce():
    assert Float().produce_value(1.1) == '1.1'

def test_g_day_parse():
    assert GDay().parse_value('---22') == SevenPropertyModel(day=22)

def test_g_day_produce():
    assert GDay().produce_value(SevenPropertyModel(day=22)) == '---22'

def test_g_month_parse():
    assert GMonth().parse_value('--05') == SevenPropertyModel(month=5)

def test_g_month_produce():
    assert GMonth().produce_value(SevenPropertyModel(month=5)) == '--05'

def test_g_month_day_parse():
    assert GMonthDay().parse_value('--05-22') == SevenPropertyModel(month=5, day=22)

def test_g_month_day_produce():
    assert GMonthDay().produce_value(SevenPropertyModel(month=5, day=22)) == '--05-22'

def test_g_year_parse():
    assert GYear().parse_value('2017') == SevenPropertyModel(year=2017)

def test_g_year_produce():
    assert GYear().produce_value(SevenPropertyModel(year=2017)) == '2017'

def test_g_year_month_parse():
    assert GYearMonth().parse_value('2017-05') == SevenPropertyModel(year=2017, month=5)

def test_g_year_month_produce():
    assert GYearMonth().produce_value(SevenPropertyModel(year=2017, month=5)) == '2017-05'

def test_hex_binary_parse():
    assert HexBinary().parse_value(b'14fb9c03d97e') == b'\x14\xfb\x9c\x03\xd9\x7e'
    assert HexBinary().parse_value(b'14fb9c03d9') == b'\x14\xfb\x9c\x03\xd9'
    assert HexBinary().parse_value(b'14fb9c03') == b'\x14\xfb\x9c\x03'

def test_hex_binary_produce():
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03\xd9\x7e') == b'14fb9c03d97e'
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03\xd9') == b'14fb9c03d9'
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03') == b'14fb9c03'

def test_id_parse():
    assert ID().parse_value('test_id_4') == 'test_id_4'

def test_id_produce():
    assert ID().produce_value('test_id_4') == 'test_id_4'

def test_idref_parse():
    assert IDREF().parse_value('test_id_4') == 'test_id_4'

def test_idref_produce():
    assert IDREF().produce_value('test_id_4') == 'test_id_4'

def test_idrefs_parse():
    assert IDREFS().parse_value('blah0 blah1 blah2') == ('blah0', 'blah1', 'blah2')

    with pytest.raises(ValueError):
        IDREFS().parse_value('')

    assert IDREFS().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_idrefs_produce():
    assert IDREFS().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_int_parse():
    assert Int().parse_value('255') == 255

def test_int_produce():
    assert Int().produce_value(255) == '255'

def test_integer_parse():
    assert Integer().parse_value('255') == 255

def test_integer_produce():
    assert Integer().produce_value(255) == '255'

def test_language_parse():
    assert Language().parse_value('en') == 'en'
    assert Language().parse_value('en-US') == 'en-US'
    assert Language().parse_value('en-gb') == 'en-gb'

    with pytest.raises(ValueError):
        Language().parse_value('')

def test_language_parse():
    assert Language().produce_value('en') == 'en'
    assert Language().produce_value('en-US') == 'en-US'

def test_long_parse():
    assert Long().parse_value('255') == 255

def test_long_produce():
    assert Long().produce_value(255) == '255'

def test_name_parse():
    assert Name().parse_value('test_id_4') == 'test_id_4'

    with pytest.raises(ValueError):
        Name().parse_value('4test_id_4')

def test_name_produce():
    assert Name().produce_value('test_id_4') == 'test_id_4'

def test_nc_name_parse():
    assert NCName().parse_value('test_id_4') == 'test_id_4'

    with pytest.raises(ValueError):
        NCName().parse_value('test:id_4')

def test_nc_name_produce():
    assert NCName().produce_value('test_id_4') == 'test_id_4'

def test_negative_integer_parse():
    assert NegativeInteger().parse_value('-255') == -255

def test_negative_integer_produce():
    assert NegativeInteger().produce_value(-255) == '-255'

def test_nmtoken_parse():
    assert NMTOKEN().parse_value('xml:schema') == 'xml:schema'
    assert NMTOKEN().parse_value('2xml:schema') == '2xml:schema'
    assert NMTOKEN().parse_value('-xml:schema') == '-xml:schema'
    assert NMTOKEN().parse_value('.xml:schema') == '.xml:schema'

    with pytest.raises(ValueError):
        NMTOKEN().parse_value('\x0dtoken')

def test_nmtoken_produce():
    assert NMTOKEN().produce_value('xml:schema') == 'xml:schema'

def test_nm_tokens_parse():
    assert NMTOKENS().parse_value('xml:schema') == ('xml:schema',)
    assert NMTOKENS().parse_value('xml:schema xml:schema2') == ('xml:schema', 'xml:schema2')

    with pytest.raises(ValueError):
        NMTOKENS().parse_value('\x0dtoken')

def test_nm_tokens_parse():
    assert NMTOKENS().produce_value(('xml:schema',)) == 'xml:schema'
    assert NMTOKENS().produce_value(('xml:schema', 'xml:schema2')) == 'xml:schema xml:schema2'

def test_non_negative_integer_parse():
    assert NonNegativeInteger().parse_value('255') == 255

def test_non_negative_integer_produce():
    assert NonNegativeInteger().produce_value(255) == '255'

def test_non_positive_integer_parse():
    assert NonPositiveInteger().parse_value('-255') == -255

def test_non_positive_integer_produce():
    assert NonPositiveInteger().produce_value(-255) == '-255'

def test_normalized_string_parse():
    assert NormalizedString().parse_value('test_id_4') == 'test_id_4'

def test_normalized_string_produce():
    assert NormalizedString().produce_value('test_id_4') == 'test_id_4'

def test_notation_parse():
    assert NOTATION().parse_value('test_id_4') == 'test_id_4'

def test_notation_produce():
    assert NOTATION().produce_value('test_id_4') == 'test_id_4'

def test_positive_integer_parse():
    assert PositiveInteger().parse_value('255') == 255

def test_positive_integer_produce():
    assert PositiveInteger().produce_value(255) == '255'

def test_q_name_parse():
    assert QName().parse_value('test_id_4') == 'test_id_4'

def test_q_name_produce():
    assert QName().produce_value('test_id_4') == 'test_id_4'

def test_short_parse():
    assert Short().parse_value('255') == 255

def test_short_produce():
    assert Short().produce_value(255) == '255'

def test_string_parse():
    assert String().parse_value('test') == 'test'

    with pytest.raises(TypeError):
        String().parse_value(2)
    with pytest.raises(TypeError):
        String().parse_value(2.0)
    with pytest.raises(TypeError):
        String().parse_value(String())

def test_string_produce():
    assert String().produce_value('255') == '255'

def test_time_parse():
    assert Time().parse_value('12:42:42Z') == SevenPropertyModel(hour=12, minute=42, second=42, timezoneOffset=0)

def test_time_produce():
    assert Time().produce_value(SevenPropertyModel(hour=12, minute=42, second=42, timezoneOffset=0)) == '12:42:42Z'

def test_token_parse():
    assert Token().parse_value('test') == 'test'

def test_token_produce():
    assert Token().produce_value('test') == 'test'

def test_unsigned_byte_parse():
    assert UnsignedByte().parse_value('255') == 255

def test_unsigned_byte_produce():
    assert UnsignedByte().produce_value(255) == '255'

def test_unsigned_int_parse():
    assert UnsignedInt().parse_value('255') == 255

def test_unsigned_int_produce():
    assert UnsignedInt().produce_value(255) == '255'

def test_unsigned_long_parse():
    assert UnsignedLong().parse_value('255') == 255

def test_unsigned_long_produce():
    assert UnsignedLong().produce_value(255) == '255'

def test_unsigned_short_parse():
    assert UnsignedShort().parse_value('255') == 255

def test_unsigned_short_produce():
    assert UnsignedShort().produce_value(255) == '255'
