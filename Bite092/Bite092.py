from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


# My Way ... brute force

def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    try:
        if date > NOW:
            raise ValueError
    except TypeError:
        raise ValueError

    if (NOW - date).days >= 2:
        return date.strftime('%m/%d/%y')
    elif 0 < (NOW-date).days < 2:
        return 'yesterday'

    if 2*HOUR <= (NOW-date).seconds < DAY:
        hours = int((NOW-date).seconds / HOUR)
        return f'{hours} hours ago'

    if HOUR <= (NOW-date).seconds < 2*HOUR:
        return 'an hour ago'

    if 2 * MINUTE <= (NOW-date).seconds < HOUR:
        minutes = int((NOW-date).seconds / MINUTE)
        return f'{minutes} minutes ago'

    if MINUTE <= (NOW-date).seconds < 2*MINUTE:
        return 'a minute ago'
    if 10 <= (NOW-date).seconds < MINUTE:
        return f'{(NOW - date).seconds} seconds ago'
    if (NOW-date).seconds < 10:
        return 'just now'

# The pythonic way:

def pretty_date_actual(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError('expecting past datetime')

    # using total_seconds because seconds only goes till max 1 day
    seconds = int((NOW - date).total_seconds())

    for time in TIME_OFFSETS:
        if seconds < time.offset:
            amount = time.divider and int(seconds/time.divider) or seconds
            return time.date_str.format(amount)
    else:
        # beyond yesterday just print date string
        return date.strftime('%m/%d/%y')


p = pretty_date(123)
print(p)