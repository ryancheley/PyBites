from unicodedata import name


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    result = set()
    text = text.lower()
    for l in text:
        if 'WITH' in name(l):
            result.add(l)
    return sorted(result)