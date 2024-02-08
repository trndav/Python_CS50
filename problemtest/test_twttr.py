from twttr import shorten

def test_shorten():
    assert shorten("") == ""

def test_shorten_a():
    assert shorten("Banana") == "Bnn"

def test_shorten_e():
    assert shorten("Elephant") == "lphnt"

def test_shorten_io():
    assert shorten("How you doin?") == "Hw y dn?"

def test_shorten_u():
    assert shorten("Umbrela") == "mbrl"

def test_shorten_numbers():
    assert shorten("123ula") == "123l"

