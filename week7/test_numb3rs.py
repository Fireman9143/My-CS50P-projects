from numb3rs import validate, bug_validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

def test_bug_validate():
    assert bug_validate("127.0.0.1") == True
    assert bug_validate("255.255.255.255") == True
    assert bug_validate("256.256.256.256") == False
    assert bug_validate("1.2.3.1000") == False
    assert bug_validate("cat") == False