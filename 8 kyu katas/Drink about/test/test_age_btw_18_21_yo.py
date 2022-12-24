from src.drink_about import people_with_age_drink
import pytest

@pytest.mark.drinks_for_18_21_yo
def test_drink_to_18_21_yo():
    assert people_with_age_drink(20) == 'drink beer'
    assert people_with_age_drink(18) == 'drink beer'