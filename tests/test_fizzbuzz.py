
def test_fizz_buzz():
    # Test case 1: n is divisible by 3
    assert fizz_buzz(9) == "Fizz"

    # Test case 2: n is divisible by 5
    assert fizz_buzz(10) == "Buzz"

    # Test case 3: n is divisible by both 3 and 5
    assert fizz_buzz(15) == "FizzBuzz"

    # Test case 4: n is not divisible by 3 or 5
    assert fizz_buzz(7) == 7

    # Test case 5: n is 0
    assert fizz_buzz(0) == "FizzBuzz"

    # Test case 6: n is negative
    assert fizz_buzz(-6) == "Fizz"

    # Test case 7: n is a float
    assert fizz_buzz(7.5) == 7.5

test_fizz_buzz()
from fizzbuzz import fizz_buzz
