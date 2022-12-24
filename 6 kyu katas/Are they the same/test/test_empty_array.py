from src.are_they_the_same import comp
import pytest

@pytest.mark.empty_array
def test_empty_array():
    a1 = None
    a2 = None
    assert comp(a1, a2) == False