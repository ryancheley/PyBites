from typing import List, TypeVar
T = TypeVar('T', int, float)


def _transform(i, n):
    if i < 0:
        return int(str(i * 10 ** n)[:n+1])
    else:
        return int(str(i * 10**n)[:n])


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n <= 0:
        raise ValueError
    result = [_transform(i, n) for i in numbers]
    return result


print(n_digit_numbers([8, 9, 10], 2))
print(n_digit_numbers([], 1))
print(n_digit_numbers([-1.1, 2.22, -3.333], 3))
print(n_digit_numbers([-1.1, 2.22, -3.333, 4444, 55555], 4))