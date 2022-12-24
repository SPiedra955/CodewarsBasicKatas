from src.string_repeat import repeat_str
import pytest

@pytest.mark.repetitions

def test_repeating_string():
    assert repeat_str(4, 'a') == 'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'
    assert repeat_str(6, 'c') == 'cccccc'
    assert repeat_str(10, 'home ') == 'home home home home home home home home home home '
