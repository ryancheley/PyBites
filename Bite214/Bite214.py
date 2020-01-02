from itertools import islice

def countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while num > 0:
        try:
            yield num
            num -= 1
        except StopIteration:
            break

cd = countdown()
print(next(cd))