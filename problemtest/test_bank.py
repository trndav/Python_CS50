from bank import value

def test_hi():
    assert value("Hi") == 20

def test_number():
    assert value("5345") == 100

def test_hello():
    assert value("hello") == 0

def test_punc():
    assert value("...!!") == 100
