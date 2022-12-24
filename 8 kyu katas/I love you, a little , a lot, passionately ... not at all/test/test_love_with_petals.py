from src.love_with_petals_flowers import how_much_i_love_you
import pytest

@pytest.mark.quantity_of_love

def test_of_love():
    assert how_much_i_love_you(7) == "I love you"
    assert how_much_i_love_you(3) == "a lot"
    assert how_much_i_love_you(6) == "not at all"
    assert how_much_i_love_you(4) == 'passionately'
    assert how_much_i_love_you(5) == 'madly'