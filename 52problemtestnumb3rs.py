from numb3rs import validate

def main():
    test_validate()
    test_validate_fail()
    test_validate_str()

def test_validate():
    assert validate("255.0.98.199") == True
    assert validate("12.24.3.123") == True
    assert validate("1.24.123") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_validate_fail():
    assert validate("10.30.98.199") == True

    assert validate('0,0,0,0') == False
    assert validate('-1.0.0.0') == False

    assert validate("10.30.98.199.255") == False
    assert validate("0.0.98.199") == True
    assert validate("371.98.99.41") == False
    assert validate("11.958.19.41") == False
    assert validate("121.98.499.11") == False
    assert validate("12.98.149.411") == False
    assert validate("12.98.849.411") == False
    assert validate("12.398.649.411") == False
    assert validate("412.598.669.411") == False
    assert validate("1.98.149.411") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_validate_str():
    assert validate("cat") == False
    assert validate("44.44.44.44") == True

if __name__ == "__main__":
    main()

# def test_zero_division():
#     with pytest.raises(SystemExit):
#         assert validate("11.0.98.199.11")
