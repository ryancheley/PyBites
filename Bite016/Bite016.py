from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    d = PYBITES_BORN
    yield d + timedelta(days=100)
    yield d + timedelta(days=200)
    yield d + timedelta(days=300)
    yield d + timedelta(days=400)
    yield d + timedelta(days=500)
    yield d + timedelta(days=600)
    yield d + timedelta(days=700)
    yield d + timedelta(days=800)
    yield d + timedelta(days=365)
    yield d + timedelta(days=365*2)



gen = gen_special_pybites_dates()

dates = list(islice(gen, 10))

print(dates)