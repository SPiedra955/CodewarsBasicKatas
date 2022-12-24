from src.drink_about import people_with_age_drink
import pytest

@pytest.mark.rank_age_14_18_yo
def test_drinkk_for_14_18yo():
    assert people_with_age_drink(17) == 'drink coke'
    assert people_with_age_drink(15) == 'drink coke'
    assert people_with_age_drink(14) == 'drink coke'
