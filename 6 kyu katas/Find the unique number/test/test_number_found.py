from src.find_the_number import find_uniq
import pytest

@pytest.mark.unique_number

def test_find_uniq_number():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10