from src.message import greet
import pytest

@pytest.mark.message_to_johnny

def test_special_message():
    assert greet("Johnny") == "Hello, my love!"