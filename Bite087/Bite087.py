import collections

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    result = ''
    roman = collections.OrderedDict()
    roman['1'] = 'I'
    roman['5'] = 'V'
    roman['10'] = 'X'
    roman['50'] = 'L'
    roman['100'] = 'C'
    roman['500'] = 'D'
    roman['1000'] = 'M'
    if decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError





r = romanize(42)
print(r)