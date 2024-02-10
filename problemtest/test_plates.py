from plates import is_valid

def test_is_valid_ok():
    assert is_valid("AA4343") == True

def test_is_valid_number():
    assert is_valid("426547") == False

def test_is_valid_alpha():
    assert is_valid("usanow") == True
    assert is_valid("ASDdsd") == True
    assert is_valid("AcAsDD") == True

def test_is_valid_short():
    assert is_valid("A") == False

def test_is_valid_wrong():
    assert is_valid("532gho") == False

def test_is_valid_zero():
    assert is_valid("abc075") == False

def test_is_valid_len():
    assert is_valid("abcdfs542575") == False

def test_is_valid_num():
    assert is_valid("abc54s") == False
    assert is_valid("") == False

def test_is_valid_punc():
    assert is_valid("!?.") == False
    assert is_valid("adn!?.") == False
