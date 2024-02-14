from jar import Jar
import pytest

@pytest.fixture
def jar():
    return Jar(12)  # Creating a Jar instance with capacity 12

def test_deposit_valid(jar):
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(1)
    assert jar.size == 6

def test_withdraw_valid(jar):
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_deposit_error(jar):
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw_error(jar):
    with pytest.raises(ValueError):
        jar.withdraw(23)

if __name__ == "__main__":
    main()
