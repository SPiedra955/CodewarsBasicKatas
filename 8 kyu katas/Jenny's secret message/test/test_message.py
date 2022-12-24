from src.message import greet
import pytest

@pytest.mark.jenny_message_to_normal_people

def testing_message():
    assert greet("James") == "Hello, James!"
    assert greet("Jane") == "Hello, Jane!"
    assert greet("Jim") == "Hello, Jim!"