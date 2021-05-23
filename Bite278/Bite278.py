from collections import Counter

def major_n_minor(numbers: list) -> tuple:
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    list_counter = Counter(numbers)
    distinct_numbers = len(list_counter)
    major = list_counter.most_common(distinct_numbers)[0][0]
    minor = list_counter.most_common(distinct_numbers)[-1][0]

    return major, minor

print(major_n_minor([1, 2, 3, 2, 2, 2, 3]))