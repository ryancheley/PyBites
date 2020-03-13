import pytest

from Bite241.tests import list_to_decimal


def test_type_error_bool():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])


def test_type_error_decimal():
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 4, 1])


def test_type_error_string():
    with pytest.raises(TypeError):
        list_to_decimal(['4', 5, 3, 1])


def test_range_error():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])


def test_check_nums():
    assert pytest.raises(ValueError, list_to_decimal, [10])


def test_value_checking():
    assert list_to_decimal([0, 4, 2, 8]) == 428
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([3]) == 3