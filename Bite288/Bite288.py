from typing import List


def minimum_number(digits: List[int]) -> int:
    digits = sorted(set(digits))
    if len(digits) == 0:
        return 0
    s = [str(i) for i in digits]
    res = int("".join(s))
    return res


print(minimum_number([0, 9, 5, 9]))
