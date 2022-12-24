from src.is_he_gonna_survive import hero
import pytest

@pytest.mark.he_not_survive

def test_he_not_survive():
    assert hero(7, 4) == False
    assert hero(4, 5) == False
    assert hero(1500, 751) == False
    assert hero(0, 1) == False