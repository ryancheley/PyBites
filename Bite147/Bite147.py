from datetime import date, datetime

from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    weekday_list = [MO, TU, WE, TH, FR]
    dt_result = list(rrule(DAILY, count=100, dtstart=start_date, byweekday=weekday_list))
    result = [datetime.strptime(d.strftime('%m-%d-%Y'), '%m-%d-%Y').date() for d in dt_result]
    return result

g = get_hundred_weekdays()
print(g)