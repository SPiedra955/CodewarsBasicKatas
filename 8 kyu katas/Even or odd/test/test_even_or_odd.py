from src.even_or_odd import evenOrOdd
import pytest

@pytest.mark.even_or_odd_number
def test_number_by_division():
    assert evenOrOdd(2) == "Even"
    assert evenOrOdd(1) == "Odd"
    assert evenOrOdd(0) == "Even"
    assert evenOrOdd(1545452) == "Even"
    assert evenOrOdd(7) == "Odd"
    assert evenOrOdd(78) == "Even"
    assert evenOrOdd(17) == "Odd"
    assert evenOrOdd(74156741) == "Odd"
    assert evenOrOdd(100000) == "Even"
    assert evenOrOdd(-123) == "Odd"
    assert evenOrOdd(-456) == "Even"
