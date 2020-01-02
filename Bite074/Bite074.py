import calendar
from date import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    results = calendar.day_name[date.weekday()]
    return results


t = weekday_of_birth_date(date=date(1974, 11, 11))
print(t)