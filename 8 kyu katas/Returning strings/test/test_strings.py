from src.returning_strings import greet
import pytest

@pytest.mark.testing_strings

def test_strings():
    assert greet('Ryan') ==  "Hello, Ryan how are you doing today?"
    assert greet('Shingles') ==  "Hello, Shingles how are you doing today?"
    assert greet('Miguel') ==  "Hello, Miguel how are you doing today?"
    assert greet('Elias') ==  "Hello, Elias how are you doing today?"
  