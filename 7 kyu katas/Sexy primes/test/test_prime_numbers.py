from src.sexy_primes import sexy_prime
import pytest

@pytest.mark.is_prime

def test_prime_numbers():
    assert sexy_prime(5,11) == True
    assert sexy_prime(13,19) == True
    assert sexy_prime(83,89) == True
   
