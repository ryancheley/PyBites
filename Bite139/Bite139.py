from datetime import datetime, timedelta, date
import re

data = """
+------------+------------+---------+
| date       | activity   | count   |
|------------+------------+---------|
| 2018-11-11 | pcc        | 1       |
| 2018-11-10 | 100d       | 1       |
| 2018-11-09 | 100d       | 2       |
| 2018-11-08 | pcc        | 1       |
| 2018-11-07 | pcc        | 1       |
| 2018-11-05 | bite       | 4       |
| 2018-11-04 | bite       | 2       |
| 2018-11-03 | bite       | 4       |
| 2018-11-02 | 100d       | 2       |
+------------+------------+---------+
"""

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    the_dates = re.findall(r'\d{4}-\d{2}-\d{2}', data)
    result = []
    for d in the_dates:
        if datetime.strptime(d, '%Y-%m-%d').date() not in result:
            result.append(datetime.strptime(d, '%Y-%m-%d').date())

    return sorted(result, reverse=True)


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
    result = []
    yesterday = TODAY + timedelta(days=-1)
    start_list = [TODAY, yesterday]
    for i in range(len(dates)):
        if dates[i]+timedelta(days=i) in start_list:
            result.append(dates[i])

    return len(result)

c = calculate_streak(extract_dates(data))
print(c)

