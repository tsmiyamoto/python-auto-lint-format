from utils.fizzbuzz import fizz_buzz  # fizz_buzz関数が含まれるモジュールをインポート


def test_fizz_buzz():
    assert fizz_buzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_fizz():
    result = fizz_buzz(3)
    assert result == ["1", "2", "Fizz"]


def test_buzz():
    result = fizz_buzz(5)
    assert result == ["1", "2", "Fizz", "4", "Buzz"]


def test_fizzbuzz():
    result = fizz_buzz(15)
    assert "FizzBuzz" in result


def test_length():
    result = fizz_buzz(20)
    assert len(result) == 20
