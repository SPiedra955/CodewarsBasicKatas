from src.personalized_message import greet
import pytest

@pytest.mark.message

def test_message_personalized():
    assert greet('Daniel', 'Daniel') == 'Hello boss'
    assert greet('Greg', 'Daniel') == 'Hello guest'  