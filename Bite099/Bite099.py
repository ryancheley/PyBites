import string
from itertools import product


def sequence_generator():
    letters = string.ascii_uppercase
    numbers = range(1, len(letters)+1)
    letters_and_numbers = zip(numbers, letters)
    return list(letters_and_numbers)


s = sequence_generator()
print(s)
