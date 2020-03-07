from datetime import date
import calendar


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    if c.monthdatescalendar(2016, 5)[0][0].month == 5:
        return c.monthdatescalendar(year, 5)[1][0]
    else:
        return c.monthdatescalendar(year, 5)[2][0]