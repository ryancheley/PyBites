from datetime import datetime
from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')

naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)

def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    es_tz = naive_utc_dt.astimezone(SPAIN)
    au_tz = naive_utc_dt.astimezone(AUSTRALIA)
    return au_tz, es_tz




