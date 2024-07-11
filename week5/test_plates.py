from week2.plates import is_valid, bug

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("outatime") == False

def test_bug():
    assert bug("CS50") == True
    assert bug("CS05") == False
    assert bug("CS50P") == False
    assert bug("PI3.14") == False
    assert bug("H") == False
    assert bug("outatime") == False
