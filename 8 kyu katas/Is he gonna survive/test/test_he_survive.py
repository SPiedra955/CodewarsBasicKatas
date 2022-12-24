from src.is_he_gonna_survive import hero
import pytest

@pytest.mark.he_survive

def test_if_he_survive():
    assert hero(10,5) == True
    assert hero(100,40) == True
