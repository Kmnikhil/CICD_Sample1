from src.math_operations import add,sub

def test_add():
    assert add(2,4) == 6
    assert add(4,4) == 8
    assert add(-4,4) == 0

def test_sub():
    assert sub(2,3) == -1
    assert sub(3,3) == 0