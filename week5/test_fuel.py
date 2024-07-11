from week3.fuel import convert, gauge, bug_convert, bug_gauge

def test_convert():
    assert convert("0/4") == "0"
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("5/4") == False
    assert convert("cat") == False
    assert bug_convert("0/4") == "0"
    assert bug_convert("1/4") == 25
    assert bug_convert("3/4") == 75
    assert bug_convert("4/4") == 100
    assert bug_convert("5/4") == False
    assert bug_convert("cat") == False


def test_gauge():
    assert gauge("0") == "E"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert bug_gauge("0") == "E"
    assert bug_gauge(25) == "25%"
    assert bug_gauge(75) == "75%"
    assert bug_gauge(100) == "F"