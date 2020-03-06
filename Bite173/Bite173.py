from datetime import datetime, timedelta
import re
from collections import namedtuple

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)

TimeParts = namedtuple('TimeParts', 'days hours minutes seconds')


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    t1 = TimeParts(0, 0, 0, 0)
    for d in delay_time.split():
        if 'd' in d:
            t1 = TimeParts(int(re.search(r'\d{1,}', d).group()), t1.hours, t1.minutes, t1.seconds)
        if 'h' in d:
            t1 = TimeParts(t1.days, int(re.search(r'\d{1,}', d).group()), t1.minutes, t1.seconds)
        if 'm' in d:
            t1 = TimeParts(t1.days, t1.hours, int(re.search(r'\d{1,}', d).group()), t1.seconds)
        if 's' in d:
            t1 = TimeParts(t1.days, t1.hours, t1.minutes, int(re.search(r'\d{1,}', d).group()))
        if d.isdigit():
            t1 = TimeParts(t1.days, t1.hours, t1.minutes, int(re.search(r'\d{1,}', d).group()))
    delta = timedelta(
        days=t1.days,
        hours=t1.hours,
        minutes=t1.minutes,
        seconds=t1.seconds
    )

    due_datetime = start_time + delta
    result = f'{task} @ {due_datetime}'

    return result


a = add_todo("45", "Finish this Test")
print(a)