from fuel import gauge, convert
import pytest

def test_convert_ok():
    assert convert("3/4") == 75
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_gauge_percent():
    assert gauge(5) == "5%"

def test_convert_zero():
    with pytest.raises(ValueError):
        convert("8/2")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")

if __name__ == "__main__":
    main()
