from src.twice_as_old import twiceOld
import pytest

@pytest.mark.calculating_age

def test_calculating_age():
    assert twiceOld(36,7) == 22
    assert twiceOld(55,30) == 5
    assert twiceOld(42,21) == 0
    assert twiceOld(22,1) == 20
    assert twiceOld(29,0) == 29
 