from datetime import datetime
from freezegun import freeze_time


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = (datetime.today() - datetime(datetime.today().year, 1, 1)).days
    book_goal_percent = books_read / books_goal
    first_day_of_year = datetime(datetime.today().year, 1, 1)
    last_day_of_year = datetime(datetime.today().year, 12, 31)
    days_in_year = (last_day_of_year - first_day_of_year).days+1
    year_progress_percent = day_of_year / days_in_year

    return book_goal_percent >= year_progress_percent



print(ontrack_reading(60, 31))

