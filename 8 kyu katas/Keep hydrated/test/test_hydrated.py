from src.keep_hydrated import litres
import pytest

@pytest.mark.its_hydrated

def test_its_hydrated():
    assert litres(2) == 1
    assert litres(1.4) == 0
    assert litres(12.3) == 6
    assert litres(0.82) == 0
    assert litres(11.8) == 5
    assert litres(1787) == 893
    assert litres(0) == 0