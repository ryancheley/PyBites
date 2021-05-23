import math
from random import choice


def round_to_next(number: int, multiple: int):
    try:
        if number % multiple == 0:
            result = math.floor(number / multiple) * multiple
        else:
            result = (math.floor(number / multiple) + 1) * multiple
    except ZeroDivisionError:
        result = 0

    return result


print(round_to_next(-10, 10)) #-10
print(round_to_next(0, 0)) # 0
print(round_to_next(15, choice([3, 5, 15]))) #15


