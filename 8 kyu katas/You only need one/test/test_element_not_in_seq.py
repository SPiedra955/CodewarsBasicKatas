from src.you_only_need_one import check_elem_in_seq
import pytest

@pytest.mark.elementNotFound

def test_element_not_found():
    assert check_elem_in_seq([78, 117, 110, 99, 104, 117, 107, 115],8) == False
    assert check_elem_in_seq(["what", "a", "great", "kata"],"kat") == False
    assert check_elem_in_seq(["come", "on", 110, "2500", 10, '!', 7, 15],"Come") == False
    assert check_elem_in_seq([8, 7, 5, "bored", "of", "writing", "tests", 115],45) == False
