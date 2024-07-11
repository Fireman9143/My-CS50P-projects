from um import count, bug_count

def test_count():
    assert count("Um, it's yummy um in um, my tummy") == 3


def test_bug_count():
    assert bug_count("Um, it's yummy um in um, my tummy") == 3