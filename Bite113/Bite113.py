from string import printable

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    result = []
    p = printable
    for i in text.split(' '):
        for l in i:
            if l not in p and i not in result:
                result.append(i)

    return result

e = extract_non_ascii_words('He wonede at Ernleȝe at æðelen are chirechen')
print(e)