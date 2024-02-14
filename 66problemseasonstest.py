from seasons import check_date, calculate_mins
import pytest

def test_check_date_ok():
    assert check_date("2023-2-12") == True
    assert check_date("2003-12-31") == True

def test_check_date_fail():
    with pytest.raises(SystemExit):
        check_date("2023-22-12")
    #with pytest.raises(ValueError):
        #check_date("January 1, 1999")

if __name__ == "__main__":
    main()
