PYBITES = "pybites"

the_string = "Pharetra massa massa ultricies mi quis"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    test_string = PYBITES.lower()+PYBITES.upper()
    result = ''
    for t in text:
        if t.islower() and t in test_string:
            result = result + t.upper()
        elif t.islower() and t not in test_string:
            result = result + t
        elif t.isupper() and t in test_string:
            result = result + t.lower()
        elif t.isupper() and t not in test_string:
            result = result + t
        else:
            result = result + t
    return result

c = convert_pybites_chars(the_string)
print(c)

# pharETra maSSa maSSa ulTrIcIES mI quIS
# PharETra maSSa maSSa ulTrIcIES mI quIS
