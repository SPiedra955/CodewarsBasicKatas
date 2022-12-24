from src.transportation_on_vacation import rental_car_cost
import pytest

@pytest.mark.price_of_rent

def test_calculating_price():

    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270
