from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from Bite242.Bite242 import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_get_sign_with_most_famous_people(signs):
    actual = get_sign_with_most_famous_people(signs)
    expected = ('Scorpio', 35)
    assert actual == expected


def test_signs_are_mutually_compatible_false(signs):
    actual = signs_are_mutually_compatible(signs, 'Scorpio', 'Leo')
    expected = False
    assert actual == expected


def test_signs_are_mutually_compatible_true(signs):
    actual = signs_are_mutually_compatible(signs, 'Aries', 'Leo')
    expected = True
    assert actual == expected


def test_get_sign_by_date(signs):
    date_to_use = datetime(2022, 3, 7)
    actual = get_sign_by_date(signs, date_to_use)
    expected = 'Pisces'
    assert actual == expected
    assert get_sign_by_date(signs, datetime(2022, 2, 19)) == expected
    assert get_sign_by_date(signs, datetime(2022, 3, 20)) == expected
