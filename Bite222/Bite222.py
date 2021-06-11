import types
from itertools import islice


def group(iterable, n):
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    results = []
    iterable = list(iterable)
    whole_list = len(iterable) // n
    remainder = len(iterable) % n
    for i in range(whole_list):
        starting = i*n
        ending = (i+1)*n
        results.append(list(islice(iterable, starting, ending)))
        print(starting, ending, list(islice(iterable, starting, ending)))
    if remainder > 0:
        results.append(list(iterable[-remainder:]))
    return results


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen = (i for i in iterable)
    n = 3
    ret = group(iterable, n)
    print(ret)