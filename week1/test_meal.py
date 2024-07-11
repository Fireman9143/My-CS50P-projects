from week2.meal import convert
from week2.meal import letters

def test_breakfast():
    assert convert("7:00") == 7.0
    assert convert("7:30") == 7.5
    assert convert("0730") == 7.5
    assert convert("800") == 8.0
    assert convert(letters("8:00am")) == 8.0
    assert convert(letters("8:00 am")) == 8.0
    assert convert(letters("8:00a.m.")) == 8.0
    assert convert(letters("8:00 a.m.")) == 8.0


def test_lunch():
    assert convert("12:00") == 12.0
    assert convert("12:30") == 12.5
    assert convert("1300") == 13.0
    assert convert(letters("12:00 pm")) == 12.0
    assert convert("1200") == 12.0
    assert convert(letters("12:00 p.m.")) == 12.0
    assert convert(letters("12:00pm")) == 12.0
    assert convert(letters("12:00p.m.")) == 12.00
    assert convert(letters("12:00am")) == 24.0
    assert convert(letters("12:00 am")) == 24.0
    assert convert(letters("12:00a.m.")) == 24.00
    assert convert(letters("12:00 a.m.")) == 24.0


def test_dinner():
    assert convert("18:00") == 18.0
    assert convert("18:30") == 18.5
    assert convert(letters("6:00 pm")) == 18.0
    assert convert(letters("6:00pm")) == 18.0
    assert convert(letters("6:00p.m.")) == 18.0
    assert convert(letters("6:00 p.m.")) == 18.0