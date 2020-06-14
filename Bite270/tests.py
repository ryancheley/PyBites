import pytest

from Bite270.Bite270 import freq_digit


@pytest.mark.parametrize("data, expected", [
    (2020, 2), (177, 7), (1998, 9),
    (12345, 1), (994145467, 4),
    (748791789189717891789, 7)
])
def test_freq_digit(data, expected):
    assert freq_digit(data) == expected