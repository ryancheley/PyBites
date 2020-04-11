import string
from itertools import islice


def sequence_generator():
    letters = string.ascii_uppercase
    numbers = range(1, len(letters)+1)
    while True:
        i = 0
        while i < 26:
            yield numbers[i]
            yield letters[i]
            i += 1

s = sequence_generator()
print(list(islice(s, 52, 62)))
