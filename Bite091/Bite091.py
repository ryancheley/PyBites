VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    result = False
    total = 0
    test_vowels = VOWELS.lower()+VOWELS.upper()
    for i in input_str:
        if i not in test_vowels:
            total = total + 1
    if total == 0:
        result = True

    return result


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    result = False
    total = 0
    test_python = PYTHON.lower()+PYTHON.upper()
    for i in input_str:
        if i in test_python:
            total = total + 1
    if total > 0:
        result = True

    return result


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    result = False
    total = 0
    test_digit = '1234567890'
    for i in input_str:
        if i in test_digit:
            total = total + 1
    if total >0:
        result = True

    return result
