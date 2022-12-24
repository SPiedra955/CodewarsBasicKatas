from src.drink_about import people_with_age_drink
import pytest

@pytest.mark.drinks_minor
def test_drinks_allowed_depending_on_age():
    assert people_with_age_drink(13) == 'drink toddy'
    assert people_with_age_drink(0) == 'drink toddy'
