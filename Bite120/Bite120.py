from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def wrapper(*numbers):
        for n in numbers:
            if n < 0:
                raise ValueError
            if not isinstance(n, int):
                raise TypeError
        return sum(numbers)
    return wrapper