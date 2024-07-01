import pytest
from factorial_function import factorial

def test_factorial():
    # Test cases for valid inputs for question 1
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    # Test case that handles exceptions for question 2 and handling raises for question 3.
    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial(-10)

if __name__ == "__main__":
    pytest.main()
