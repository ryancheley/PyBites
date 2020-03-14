from Bite239.tests import fizzbuzz

# write one or more pytest functions below, they need to start with test_


def test_fizz():
    assert fizzbuzz(15) == 'Fizz Buzz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(4) == 4
