from src.leap_years import isLeapYear
import pytest

@pytest.mark.is_leap_year

def test_is_leap_year():
    assert isLeapYear(1984) == True
    assert isLeapYear(2000) == True
