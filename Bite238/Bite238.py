from Bite238.fibonacci import fib
import pytest


# write one or more pytest functions below, they need to start with test_

def test_error_if_less_than_zero():
    with pytest.raises(ValueError):
        fib(-1)


def test_value_for_zero_and_one():
    assert fib(0) == 0
    assert fib(1) == 1


def test_value_greater_than_one():
    assert fib(5) == fib(4) + fib(3)
    assert fib(6) == fib(5) + fib(4)