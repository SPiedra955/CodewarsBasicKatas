from src.you_only_need_one import check_elem_in_seq
import pytest

@pytest.mark.elementFound

def test_elementFound():
    assert check_elem_in_seq([66, 101],66) == True
    assert check_elem_in_seq([101, 45, 75, 105, 99, 107],107) == True
    assert check_elem_in_seq([80, 117, 115, 104, 45, 85, 112, 115], 45) == True
    assert check_elem_in_seq(['t', 'e', 's', 't'],'e') == True
    assert check_elem_in_seq([66, "codewars", 11, "alex loves pushups"],"alex loves pushups") == True
    assert check_elem_in_seq(["when's", "the", "next", "Katathon?", 9, 7],"Katathon?") == True
    assert check_elem_in_seq(["anyone", "want", "to", "hire", "me?"],"me?") == True


