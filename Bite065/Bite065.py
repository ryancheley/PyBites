import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    final_word_list = []
    word_list = _get_permutations_draw(draw)
    for i in word_list:
        if i.lower() in dictionary:
            final_word_list.append(i.lower())
    return final_word_list


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    # draw = draw.split(', ')
    word_list = []
    for p in range(7):
        two_letter_tups = set(itertools.permutations(draw, p+1))
        word_list = word_list + [''.join(tups) for tups in two_letter_tups]
    return word_list


draw = 'O, N, V, R, A, Z, H'
g = get_possible_dict_words(draw)
print(g)
