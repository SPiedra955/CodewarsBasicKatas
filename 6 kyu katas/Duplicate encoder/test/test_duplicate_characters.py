from src.duplicate import duplicate_encode
import pytest

@pytest.mark.character_in_strings
def test_duplicate_characters():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("