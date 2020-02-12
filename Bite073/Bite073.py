import pytz
from datetime import datetime

dt = datetime(2018, 4, 18, 13, 28)
timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    truth_list = []
    try:
        for t in timezones:
            if utc.astimezone(pytz.timezone(t)).hour in MEETING_HOURS:
                truth_list.append(0)
            else:
                truth_list.append(1)

        if sum(truth_list) == 0:
            result = True
        else:
            result = False

        return result
    except pytz.exceptions.UnknownTimeZoneError:
        raise ValueError




w = within_schedule(dt, *timezones)
print(w)