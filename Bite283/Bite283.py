import datetime


def tomorrow(selected_date=datetime.date(2020, 7, 9)):
    delta = datetime.timedelta(days=1)
    result = selected_date + delta
    return result