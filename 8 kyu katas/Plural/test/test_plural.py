from src.plural import english_plural
import pytest

@pytest.mark.testing_plural

def test_plural():
    assert english_plural(0) == True
    assert english_plural(1) == False
    assert english_plural(100) == True