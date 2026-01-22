from app import add

# Make sure the function name is 'test_add'
def test_add(): 
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

