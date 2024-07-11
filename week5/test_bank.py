from week1.bank import value, bug

def test_hello():
    assert value("hello") == 0
    assert bug("hello") == 0
def test_hey():
    assert value("hey") == 20
    assert bug("hey") ==20
def test_not():
    assert value("any") == 100
    assert bug("any") ==100