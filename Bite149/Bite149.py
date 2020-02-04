sentence = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019"

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    naive_sort = sorted(words, key=str.casefold)
    result = sorted(naive_sort, key=lambda s: True if (s[0].isnumeric()) else False)
    return result

s = sort_words_case_insensitively(sentence.split())
print(s)