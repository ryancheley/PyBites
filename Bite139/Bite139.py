from datetime import datetime, timedelta, date
import re

data = """
+------------+------------+---------+
| date       | activity   | count   |
|------------+------------+---------|
| 2018-11-10 | pcc        | 1       |
| 2018-11-09 | 100d       | 1       |
| 2018-11-07 | 100d       | 2       |
| 2018-10-23 | pcc        | 1       |
| 2018-10-15 | pcc        | 1       |
| 2018-10-05 | bite       | 1       |
| 2018-09-21 | bite       | 4       |
| 2018-09-18 | bite       | 2       |
| 2018-09-18 | bite       | 4       |
+------------+------------+---------+
"""

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', data)
    result = []
    for d in dates:
        if datetime.strptime(d, '%Y-%m-%d').date() not in result:
            result.append(datetime.strptime(d, '%Y-%m-%d').date())

    return result


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    dates = extract_dates(dates)
    streak_dates = []
    most_recent_date = sorted(dates, reverse=True)[0]
    yesterday = TODAY - timedelta(days=1)
    if most_recent_date >= yesterday:
        for i, item in enumerate(dates):
            try:
                if i <= (TODAY-dates[i]).days == 1:
                    streak_dates.append(item)
            except IndexError:
                pass

    result = 0
    try:
        streak_start_date = sorted(streak_dates)[0]
        streak_end_date = sorted(streak_dates)[-1]
        if streak_end_date == TODAY:
            result = (TODAY - streak_start_date).days + 1
        else:
            result = (TODAY - streak_start_date).days
    except IndexError:
        pass

    return result


c = calculate_streak(data)
print(c)

