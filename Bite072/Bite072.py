from collections import OrderedDict
from itertools import takewhile


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    try:
        belt_bound = list(takewhile(lambda x: x <= user_score, HONORS.keys()))[-1]
        belt_color = HONORS[belt_bound]
    except IndexError:
        belt_color = None
    return belt_color