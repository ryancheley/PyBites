import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    result = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}', text)
    try:
        result.span()
        return True
    except AttributeError:
        pass


def is_integer(number):
    """Return True if number is an integer"""
    return type(number) == int


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return re.search(r'\w+(?:-\w+)+', text) is not None


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    replacement_string_list = re.findall(' \([a-zA-Z]*\)| \([0-9]\.[0-9]\)', text)
    for i in replacement_string_list:
        text = text.replace(i, '')
    return text


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    result = []
    res = re.split(r'\?|!|\.|\, |;', text)
    for r in res:
        if r != '':
            result.append(r.strip())
    return result


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return ' '.join(text.split())


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return re.search(r'[aeiou]{3,}', word) is not None


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    date_list = date.split('/')
    if len(date_list) == 3:
        return date_list[1]+'/'+date_list[0]+'/'+date_list[2]
    else:
        return 'none'

c = convert_emea_date_to_amer_date('none')
print(c)