from src.frog_mouth_size import mouth_size
import pytest

@pytest.mark.sizeMouth

def testing_size():
    assert mouth_size("toucan") == "wide"
    assert mouth_size("ant bear") == "wide"
    assert mouth_size("alligator") == "small"
    assert mouth_size("tiger") == "wide"
    assert mouth_size("cow") == "wide"
    assert mouth_size("cat") == "wide"
    assert mouth_size("dog") == "wide"
    assert mouth_size("ALligator") == "small"