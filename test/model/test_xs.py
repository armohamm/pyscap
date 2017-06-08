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
import pathlib
import pkgutil
import pytest
import xml.etree.ElementTree as ET

from scap.Model import Model

# import all the classes in the package
import scap.model.xs as pkg
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

logging.basicConfig(level=logging.DEBUG)

# NOTE: this namespace is registered by default
#Model.register_namespace('scap.model.xs', 'http://www.w3.org/2001/XMLSchema')

def test_parse():
    path = pathlib.Path(str(pytest.config.rootdir)) / 'test' / 'model' / 'test_xs.xsd'
    model = Model.load(None, ET.parse(str(path)).getroot())

def test_SevenPropertyModel_init():
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

    spm = SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42)
    assert spm.year == 2017
    assert spm.month == 5
    assert spm.day == 22
    assert spm.hour == 12
    assert spm.minute == 42
    assert spm.second == 42
    assert spm.timezoneOffset is None

    spm = SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42, timezoneOffset=60)
    assert spm.year == 2017
    assert spm.month == 5
    assert spm.day == 22
    assert spm.hour == 12
    assert spm.minute == 42
    assert spm.second == 42
    assert spm.timezoneOffset == 60

def test_SevenPropertyModel_init_date():
    spm = SevenPropertyModel(date=datetime.date(year=2017, month=5, day=22))
    assert spm.year == 2017
    assert spm.month == 5
    assert spm.day == 22
    for i in (spm.hour, spm.minute, spm.second, spm.timezoneOffset):
        assert i is None

def test_SevenPropertyModel_init_datetime():
    spm = SevenPropertyModel(datetime=datetime.datetime(year=2017, month=5, day=22, hour=12, minute=42, second=42))
    assert spm.year == 2017
    assert spm.month == 5
    assert spm.day == 22
    assert spm.hour == 12
    assert spm.minute == 42
    assert spm.second == 42
    assert spm.timezoneOffset is None

def test_SevenPropertyModel_init_time():
    spm = SevenPropertyModel(time=datetime.time(hour=12, minute=42, second=42))
    assert spm.hour == 12
    assert spm.minute == 42
    assert spm.second == 42
    for i in (spm.year, spm.month, spm.day, spm.timezoneOffset):
        assert i is None

def test_SevenPropertyModel_eq():
    assert SevenPropertyModel(hour=12, minute=42, second=42) == SevenPropertyModel(hour=12, minute=42, second=42)
    assert SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42) == \
        SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42)

def test_SevenPropertyModel_ne():
    assert SevenPropertyModel(hour=12, minute=42, second=42) != SevenPropertyModel(hour=13, minute=42, second=42)

def test_SevenPropertyModel_to_date():
    assert SevenPropertyModel(year=2017, month=5, day=22).to_date() == datetime.date(year=2017, month=5, day=22)
    # TODO test timezone offsets

def test_SevenPropertyModel_to_datetime():
    assert SevenPropertyModel(year=2017, month=5, day=22, hour=12, minute=42, second=42).to_datetime() == datetime.datetime(year=2017, month=5, day=22, hour=12, minute=42, second=42)
    # TODO test timezone offsets

def test_SevenPropertyModel_to_time():
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
def test_Base64Binary_parse():
    assert Base64Binary().parse_value(b'FPucA9l+') == b'\x14\xfb\x9c\x03\xd9\x7e'
    assert Base64Binary().parse_value(b'FPucA9k=') == b'\x14\xfb\x9c\x03\xd9'
    assert Base64Binary().parse_value(b'FPucAw==') == b'\x14\xfb\x9c\x03'

def test_Base64Binary_produce():
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03\xd9\x7e') == b'FPucA9l+'
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03\xd9') == b'FPucA9k='
    assert Base64Binary().produce_value(b'\x14\xfb\x9c\x03') == b'FPucAw=='

def test_Boolean_parse():
    assert Boolean().parse_value('1') == True
    assert Boolean().parse_value('0') == False
    assert Boolean().parse_value('true') == True
    assert Boolean().parse_value('false') == False

def test_Boolean_produce():
    assert Boolean().produce_value(True) == 'True'
    assert Boolean().produce_value(False) == 'False'

def test_Byte_parse():
    assert Byte().parse_value('127') == 127

def test_Byte_produce():
    assert Byte().produce_value(127) == '127'

def test_Date_parse():
    assert Date().parse_value('2017-05-16Z') == SevenPropertyModel(year=2017, month=5, day=16, timezoneOffset=0)

def test_Date_produce():
    assert Date().produce_value(SevenPropertyModel(year=2017, month=5, day=16, timezoneOffset=0)) == '2017-05-16Z'

def test_DateTime_parse():
    assert DateTime().parse_value('2017-05-16T12:42:42Z') == SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)

def test_DateTime_produce():
    assert DateTime().produce_value(SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)) == '2017-05-16T12:42:42Z'

def test_DateTimeStamp_parse():
    assert DateTime().parse_value('2017-05-16T12:42:42Z') == SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)

def test_DateTimeStamp_produce():
    assert DateTime().produce_value(SevenPropertyModel(year=2017, month=5, day=16, hour=12, minute=42, second=42, timezoneOffset=0)) == '2017-05-16T12:42:42Z'

def test_DayTimeDuration_parse():
    assert DayTimeDuration().parse_value('P1DT1H1M1.1S') == (0, 90061.1)

    assert DayTimeDuration().parse_value('P1D') == (0, 86400.0)
    assert DayTimeDuration().parse_value('PT1H') == (0, 3600.0)
    assert DayTimeDuration().parse_value('PT1M') == (0, 60.0)
    assert DayTimeDuration().parse_value('PT1S') == (0, 1.0)

    assert DayTimeDuration().parse_value('-P1D') == (0, -86400.0)
    assert DayTimeDuration().parse_value('-PT1H') == (0, -3600.0)
    assert DayTimeDuration().parse_value('-PT1M') == (0, -60.0)
    assert DayTimeDuration().parse_value('-PT1S') == (0, -1.0)

    with pytest.raises(ValueError):
        DayTimeDuration().parse_value('P1Y1M1DT1H1M1.1S')

def test_DayTimeDuration_produce():
    assert DayTimeDuration().produce_value((0, 90061.1)) == 'P1DT1H1M1.100000S'

    assert DayTimeDuration().produce_value((0, 86400.0)) == 'P1D'
    assert DayTimeDuration().produce_value((0, 3600.0)) == 'PT1H'
    assert DayTimeDuration().produce_value((0, 60.0)) == 'PT1M'
    assert DayTimeDuration().produce_value((0, 1.0)) == 'PT1S'

    assert DayTimeDuration().produce_value((0, -86400.0)) == '-P1D'
    assert DayTimeDuration().produce_value((0, -3600.0)) == '-PT1H'
    assert DayTimeDuration().produce_value((0, -60.0)) == '-PT1M'
    assert DayTimeDuration().produce_value((0, -1.0)) == '-PT1S'

    with pytest.raises(ValueError):
        DayTimeDuration().produce_value((1, 1.0))

def test_Decimal_parse():
    assert Decimal().parse_value('1.1') == 1.1

def test_Decimal_produce():
    assert Decimal().produce_value(1.1) == '1.1'

def test_Double_parse():
    assert Double().parse_value('1.1') == 1.1

def test_Double_produce():
    assert Double().produce_value(1.1) == '1.1'

def test_Duration_parse():
    assert Duration().parse_value('P1Y1M1DT1H1M1.1S') == (13, 90061.1)

    assert Duration().parse_value('P1Y') == (12, 0.0)
    assert Duration().parse_value('P1M') == (1, 0.0)
    assert Duration().parse_value('P1D') == (0, 86400.0)
    assert Duration().parse_value('PT1H') == (0, 3600.0)
    assert Duration().parse_value('PT1M') == (0, 60.0)
    assert Duration().parse_value('PT1S') == (0, 1.0)

    assert Duration().parse_value('-P1Y') == (-12, 0.0)
    assert Duration().parse_value('-P1M') == (-1, 0.0)
    assert Duration().parse_value('-P1D') == (0, -86400.0)
    assert Duration().parse_value('-PT1H') == (0, -3600.0)
    assert Duration().parse_value('-PT1M') == (0, -60.0)
    assert Duration().parse_value('-PT1S') == (0, -1.0)

def test_Duration_produce():
    assert Duration().produce_value((13, 90061.1)) == 'P1Y1M1DT1H1M1.100000S'

    assert Duration().produce_value((12, 0.0)) == 'P1Y'
    assert Duration().produce_value((1, 0.0)) == 'P1M'
    assert Duration().produce_value((0, 86400.0)) == 'P1D'
    assert Duration().produce_value((0, 3600.0)) == 'PT1H'
    assert Duration().produce_value((0, 60.0)) == 'PT1M'
    assert Duration().produce_value((0, 1.0)) == 'PT1S'

    assert Duration().produce_value((-12, 0.0)) == '-P1Y'
    assert Duration().produce_value((-1, 0.0)) == '-P1M'
    assert Duration().produce_value((0, -86400.0)) == '-P1D'
    assert Duration().produce_value((0, -3600.0)) == '-PT1H'
    assert Duration().produce_value((0, -60.0)) == '-PT1M'
    assert Duration().produce_value((0, -1.0)) == '-PT1S'

def test_ENTITIES_parse():
    assert ENTITIES().parse_value('blah0 blah1 blah2') == ('blah0', 'blah1', 'blah2')

    with pytest.raises(ValueError):
        ENTITIES().parse_value('')

def test_ENTITIES_produce():
    assert ENTITIES().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_ENTITY_parse():
    assert ENTITY().parse_value('test_id_4') == 'test_id_4'

def test_ENTITY_produce():
    assert ENTITY().produce_value('test_id_4') == 'test_id_4'

def test_Float_parse():
    assert Float().parse_value('1.1') == 1.1

def test_Float_produce():
    assert Float().produce_value(1.1) == '1.1'

def test_GDay_parse():
    assert GDay().parse_value('---22') == SevenPropertyModel(day=22)

def test_GDay_produce():
    assert GDay().produce_value(SevenPropertyModel(day=22)) == '---22'

def test_GMonth_parse():
    assert GMonth().parse_value('--05') == SevenPropertyModel(month=5)

def test_GMonth_produce():
    assert GMonth().produce_value(SevenPropertyModel(month=5)) == '--05'

def test_GMonthDay_day_parse():
    assert GMonthDay().parse_value('--05-22') == SevenPropertyModel(month=5, day=22)

def test_GMonthDay_produce():
    assert GMonthDay().produce_value(SevenPropertyModel(month=5, day=22)) == '--05-22'

def test_GYear_parse():
    assert GYear().parse_value('2017') == SevenPropertyModel(year=2017)

def test_GYear_produce():
    assert GYear().produce_value(SevenPropertyModel(year=2017)) == '2017'

def test_GYearMonth_parse():
    assert GYearMonth().parse_value('2017-05') == SevenPropertyModel(year=2017, month=5)

def test_GYearMonth_produce():
    assert GYearMonth().produce_value(SevenPropertyModel(year=2017, month=5)) == '2017-05'

def test_HexBinary_parse():
    assert HexBinary().parse_value(b'14fb9c03d97e') == b'\x14\xfb\x9c\x03\xd9\x7e'
    assert HexBinary().parse_value(b'14fb9c03d9') == b'\x14\xfb\x9c\x03\xd9'
    assert HexBinary().parse_value(b'14fb9c03') == b'\x14\xfb\x9c\x03'

def test_HexBinary_produce():
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03\xd9\x7e') == b'14fb9c03d97e'
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03\xd9') == b'14fb9c03d9'
    assert HexBinary().produce_value(b'\x14\xfb\x9c\x03') == b'14fb9c03'

def test_ID_parse():
    assert ID().parse_value('test_id_4') == 'test_id_4'

def test_ID_produce():
    assert ID().produce_value('test_id_4') == 'test_id_4'

def test_IDREF_parse():
    assert IDREF().parse_value('test_id_4') == 'test_id_4'

def test_IDREF_produce():
    assert IDREF().produce_value('test_id_4') == 'test_id_4'

def test_IDREFS_parse():
    assert IDREFS().parse_value('blah0 blah1 blah2') == ('blah0', 'blah1', 'blah2')

    with pytest.raises(ValueError):
        IDREFS().parse_value('')

    assert IDREFS().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_IDREFS_produce():
    assert IDREFS().produce_value(('blah0', 'blah1', 'blah2')) == 'blah0 blah1 blah2'

def test_Int_parse():
    assert Int().parse_value('255') == 255

def test_Int_produce():
    assert Int().produce_value(255) == '255'

def test_Integer_parse():
    assert Integer().parse_value('255') == 255

def test_Integer_produce():
    assert Integer().produce_value(255) == '255'

def test_Language_parse():
    assert Language().parse_value('en') == 'en'
    assert Language().parse_value('en-US') == 'en-US'
    assert Language().parse_value('en-gb') == 'en-gb'

    with pytest.raises(ValueError):
        Language().parse_value('')

def test_Language_parse():
    assert Language().produce_value('en') == 'en'
    assert Language().produce_value('en-US') == 'en-US'

def test_Long_parse():
    assert Long().parse_value('255') == 255

def test_Long_produce():
    assert Long().produce_value(255) == '255'

def test_Name_parse():
    assert Name().parse_value('test_id_4') == 'test_id_4'

    with pytest.raises(ValueError):
        Name().parse_value('4test_id_4')

def test_Name_produce():
    assert Name().produce_value('test_id_4') == 'test_id_4'

def test_NCName_parse():
    assert NCName().parse_value('test_id_4') == 'test_id_4'

    with pytest.raises(ValueError):
        NCName().parse_value('test:id_4')

def test_NCName_produce():
    assert NCName().produce_value('test_id_4') == 'test_id_4'

def test_NegativeInteger_parse():
    assert NegativeInteger().parse_value('-255') == -255

def test_NegativeInteger_produce():
    assert NegativeInteger().produce_value(-255) == '-255'

def test_NMTOKEN_parse():
    assert NMTOKEN().parse_value('xml:schema') == 'xml:schema'
    assert NMTOKEN().parse_value('2xml:schema') == '2xml:schema'
    assert NMTOKEN().parse_value('-xml:schema') == '-xml:schema'
    assert NMTOKEN().parse_value('.xml:schema') == '.xml:schema'

    with pytest.raises(ValueError):
        NMTOKEN().parse_value('\x0dtoken')

def test_NMTOKEN_produce():
    assert NMTOKEN().produce_value('xml:schema') == 'xml:schema'

def test_NMTOKENS_parse():
    assert NMTOKENS().parse_value('xml:schema') == ('xml:schema',)
    assert NMTOKENS().parse_value('xml:schema xml:schema2') == ('xml:schema', 'xml:schema2')

    with pytest.raises(ValueError):
        NMTOKENS().parse_value('\x0dtoken')

def test_NMTOKENS_produce():
    assert NMTOKENS().produce_value(('xml:schema',)) == 'xml:schema'
    assert NMTOKENS().produce_value(('xml:schema', 'xml:schema2')) == 'xml:schema xml:schema2'

def test_NonNegativeInteger_parse():
    assert NonNegativeInteger().parse_value('255') == 255

def test_NonNegativeInteger_produce():
    assert NonNegativeInteger().produce_value(255) == '255'

def test_NonPositiveInteger_parse():
    assert NonPositiveInteger().parse_value('-255') == -255

def test_NonPositiveInteger_produce():
    assert NonPositiveInteger().produce_value(-255) == '-255'

def test_NormalizedString_parse():
    assert NormalizedString().parse_value('test_id_4') == 'test_id_4'

def test_NormalizedString_produce():
    assert NormalizedString().produce_value('test_id_4') == 'test_id_4'

def test_NOTATION_parse():
    assert NOTATION().parse_value('test_id_4') == 'test_id_4'

def test_NOTATION_produce():
    assert NOTATION().produce_value('test_id_4') == 'test_id_4'

def test_PositiveInteger_parse():
    assert PositiveInteger().parse_value('255') == 255

def test_PositiveInteger_produce():
    assert PositiveInteger().produce_value(255) == '255'

def test_QName_parse():
    assert QName().parse_value('test_id_4') == 'test_id_4'

def test_QName_produce():
    assert QName().produce_value('test_id_4') == 'test_id_4'

def test_Short_parse():
    assert Short().parse_value('255') == 255

def test_Short_produce():
    assert Short().produce_value(255) == '255'

def test_String_parse():
    assert String().parse_value('test') == 'test'

    with pytest.raises(TypeError):
        String().parse_value(2)
    with pytest.raises(TypeError):
        String().parse_value(2.0)
    with pytest.raises(TypeError):
        String().parse_value(String())

def test_String_produce():
    assert String().produce_value('255') == '255'

def test_Time_parse():
    assert Time().parse_value('12:42:42Z') == SevenPropertyModel(hour=12, minute=42, second=42, timezoneOffset=0)

def test_Time_produce():
    assert Time().produce_value(SevenPropertyModel(hour=12, minute=42, second=42, timezoneOffset=0)) == '12:42:42Z'

def test_Token_parse():
    assert Token().parse_value('test') == 'test'

def test_Token_produce():
    assert Token().produce_value('test') == 'test'

def test_UnsignedByte_parse():
    assert UnsignedByte().parse_value('255') == 255

def test_UnsignedByte_produce():
    assert UnsignedByte().produce_value(255) == '255'

def test_UnsignedInt_parse():
    assert UnsignedInt().parse_value('255') == 255

def test_UnsignedInt_produce():
    assert UnsignedInt().produce_value(255) == '255'

def test_UnsignedLong_parse():
    assert UnsignedLong().parse_value('255') == 255

def test_UnsignedLong_produce():
    assert UnsignedLong().produce_value(255) == '255'

def test_UnsignedShort_parse():
    assert UnsignedShort().parse_value('255') == 255

def test_UnsignedShort_produce():
    assert UnsignedShort().produce_value(255) == '255'

def test_YearMonthDuration_parse():
    assert YearMonthDuration().parse_value('P1Y1M') == (13, 0)

    assert YearMonthDuration().parse_value('P1Y') == (12, 0.0)
    assert YearMonthDuration().parse_value('P1M') == (1, 0.0)

    assert YearMonthDuration().parse_value('-P1Y') == (-12, 0.0)
    assert YearMonthDuration().parse_value('-P1M') == (-1, 0.0)

    with pytest.raises(ValueError):
        DayTimeDuration().parse_value('P1Y1M1DT1H1M1.1S')

def test_YearMonthDuration_produce():
    assert YearMonthDuration().produce_value((13, 0)) == 'P1Y1M'

    assert YearMonthDuration().produce_value((12, 0.0)) == 'P1Y'
    assert YearMonthDuration().produce_value((1, 0.0)) == 'P1M'

    assert YearMonthDuration().produce_value((-12, 0.0)) == '-P1Y'
    assert YearMonthDuration().produce_value((-1, 0.0)) == '-P1M'

    with pytest.raises(ValueError):
        DayTimeDuration().produce_value((1, 1.0))
