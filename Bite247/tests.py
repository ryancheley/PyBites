from unittest.mock import patch
import pytest
from random import seed
from random import sample


def gen_hex_color():
    while True:
        r, g, b = sample(range(0, 256), 3)
        yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()


@pytest.fixture(scope="module")
def gen():
    return gen_hex_color()


def test_gen_hex_color(gen):
    seed(0)
    with patch('random.sample', gen):
        assert next(gen) == '#C5D714'
