from src.mathematical_ops import basic_op
import pytest

@pytest.mark.filter_by_operand
def test_ops():
    assert basic_op('+', 4, 7) == 11
    assert basic_op('-', 15, 18) == -3
    assert basic_op('*', 5, 5) == 25
    assert basic_op('/', 49, 7) == 7