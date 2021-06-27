from typing import Generator
import json
import math

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values = json.loads(values)
    for idx, value in enumerate(values):
        try:
            first_display = values[idx]
            second_display = values[(idx + 1)]
            total = format(round_half_up(first_display + second_display, 2), '.2f')
            result = f"The sum of {first_display} and {second_display}, rounded to two decimal places, is {total}."
            yield result
        except:
            pass


calc_sums()