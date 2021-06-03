import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    non_empties = [x for x in args if x]
    try:
        result = functools.reduce(lambda x, y: set(x).intersection(y), non_empties)
        result = set(result)
    except TypeError:
        result = set()
    return result


test1 = intersection(({1, 2, 3}, {2, 3, 4}, {3, 4}))
test2 = intersection(([1,2,3,"1"], {1,-1}, {}))
test3 = intersection(((None, "this is a string")))
print(test3)