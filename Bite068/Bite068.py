PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    results = input_string
    for p in PUNCTUATION:
        results = results.replace(p, '')
    return results


t = remove_punctuation('test ... test \\ !! $%# ~~~')
print(t)