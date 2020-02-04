sentence = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019"

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    result = sorted(sorted(words, key=str.casefold), key=lambda s: True if (s[0].isnumeric()) else False)
    return result