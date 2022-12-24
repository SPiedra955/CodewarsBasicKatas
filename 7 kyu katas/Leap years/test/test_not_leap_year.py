from src.leap_years import isLeapYear
import pytest

@pytest.mark.is_not_leap_year

def test_not_leap_year():
    assert isLeapYear(1234) == False
    assert isLeapYear(1100) == False
