from src.sexy_primes import sexy_prime
import pytest

@pytest.mark.not_prime

def test_not_prime_numbers():
    assert sexy_prime(1,11) == False
    assert sexy_prime(10,19) == False
    assert sexy_prime(63,99) == False