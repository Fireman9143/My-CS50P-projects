from week2.twttr import shorten , bug

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"

def test_bug():
    assert bug("hello") == "hll"
    assert bug("HELLO") == "HLL"