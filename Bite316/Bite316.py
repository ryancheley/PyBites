from datetime import date
from typing import Dict, Sequence, NamedTuple
import collections


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'

test_history = [MovieRented('Spider-Man', 12, date(2020, 12, 28)),
     MovieRented('Sonic', 10, date(2020, 11, 4)),
     MovieRented('Die Hard', 3, date(2020, 11, 3))]

def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    my_list = []
    for item in renting_history:
        key = item.date.strftime('%Y-%m')
        value = item.price
        my_dict = {key: value}
        my_list.append(collections.Counter(my_dict))

    monthly_cost = sum(my_list, collections.Counter())

    result = {}
    for i in monthly_cost.items():
        if i[1] > streaming_cost_per_month:
            result[i[0]] = 'stream'
        else:
            result[i[0]] = 'rent'

    return result




        # my_list.append(collections.Counter(my_dict))




answer = rent_or_stream(test_history, STREAMING_COST_PER_MONTH)
print(answer)