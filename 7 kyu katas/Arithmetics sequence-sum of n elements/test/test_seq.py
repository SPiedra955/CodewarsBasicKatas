from src.arithmetic_seq import arithmetic_sequence_sum
import pytest

@pytest.mark.sum_of_seq
def test_the_sum_of_seq():
    assert arithmetic_sequence_sum(3, 2, 20) == 440
    assert arithmetic_sequence_sum(2, 2, 10) == 110
    assert arithmetic_sequence_sum(1, -2, 10) == -80