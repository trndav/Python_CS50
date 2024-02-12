import pytest
from working import convert

def test_convert_both():
    assert convert("9:30 PM to 11:30 PM") == "21:30 to 23:30"
    assert convert("9:30 PM to 11:30 AM") == "21:30 to 11:30"
    assert convert("9:30 AM to 11:30 AM") == "09:30 to 11:30"
    assert convert("9:30 AM to 11:30 PM") == "09:30 to 23:30"

def test_convert_int():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
    assert convert("9 PM to 10 PM") == "21:00 to 22:00"
    assert convert("9 PM to 10 AM") == "21:00 to 10:00"

def test_convert_last():
    assert convert("9 PM to 11:30 PM") == "21:00 to 23:30"
    assert convert("9 PM to 11:30 AM") == "21:00 to 11:30"
    assert convert("9 AM to 11:30 PM") == "09:00 to 23:30"
    assert convert("9 AM to 11:30 AM") == "09:00 to 11:30"

def test_convert_first():
    assert convert("9:30 AM to 10 AM") == "09:30 to 10:00"
    assert convert("9:30 AM to 10 PM") == "09:30 to 22:00"
    assert convert("9:30 PM to 10 PM") == "21:30 to 22:00"
    assert convert("9:30 PM to 10 AM") == "21:30 to 10:00"

def test_convert_error():
    with pytest.raises(ValueError):
        convert("39:30 AM to 11:30 PM")
    with pytest.raises(ValueError):
        convert("9:30 AM - 11:30 PM")

if __name__ == "__main__":
    main()
