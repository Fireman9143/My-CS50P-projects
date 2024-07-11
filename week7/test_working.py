from working import convert, bug_convert
from pytest import raises


def test_convert():
    assert convert("9 AM to 5 PM") == "0900 to 1700"
    assert convert("9:00 AM to 5:00 PM") == "0900 to 1700"
    assert convert("10 PM to 8 AM") == "2200 to 0800"
    assert convert("10:30 PM to 8:50 AM") == "2230 to 0850"
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM") == ValueError
    with raises(ValueError):
        convert("9 AM - 5 PM") == ValueError
    with raises(ValueError):
        convert("09:00 AM - 17:00 PM") == ValueError

def test_bug_convert():
    assert bug_convert("9 AM to 5 PM") == "0900 to 1700"
    assert bug_convert("9:00 AM to 5:00 PM") == "0900 to 1700"
    assert bug_convert("10 PM to 8 AM") == "2200 to 0800"
    assert bug_convert("10:30 PM to 8:50 AM") == "2230 to 0850"
    with raises(ValueError):
        bug_convert("9:60 AM to 5:60 PM") == ValueError
    with raises(ValueError):
        bug_convert("9 AM - 5 PM") == ValueError
    with raises(ValueError):
        bug_convert("09:00 AM - 17:00 PM") == ValueError