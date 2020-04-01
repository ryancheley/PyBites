import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    result = []
    zipped_items = zip(*args)
    for item in zipped_items:
        result.append(SEPARATOR.join((str(i) for i in item)))
    return result