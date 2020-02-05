"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import string

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    result = False
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word if ch not in exclude)
    word = word.replace(' ', '')
    word = word.replace('’', '')
    lower_word = word.lower()
    stringlength = len(lower_word)
    reverse_lower_word = lower_word[stringlength::-1]
    if lower_word == reverse_lower_word:
        result = True

    return result


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = load_dictionary()
    palindrome_list = []

    for w in words:
        if is_palindrome(w):
            palindrome_list.append((w, len(w)))

    palindrome_list = sorted(palindrome_list, key=lambda x: x[1], reverse=True)

    return palindrome_list[0][0]
