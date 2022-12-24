from src.drink_about import people_with_age_drink
import pytest

@pytest.mark.drink_for_21yo
def test_age_greater_21():
    assert people_with_age_drink(22) == 'drink whisky'
    assert people_with_age_drink(21) == 'drink whisky'