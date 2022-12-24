from src.grasshopper import summation
import pytest

@pytest.mark.check_sum

def test_sum():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791
