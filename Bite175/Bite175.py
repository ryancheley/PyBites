import pandas as pd


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    min_date = min(dates)
    max_date = max(dates)
    df = pd.period_range(min_date, max_date)
    missing_date_range = []
    for i in df:
        if i.to_timestamp() not in dates:
            missing_date_range.append(i.to_timestamp())

    return missing_date_range