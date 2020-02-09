# Inspiration from https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if type(decimal_number) == str:
        raise ValueError
    if decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while decimal_number > 0:
        for _ in range(decimal_number // val[i]):
            roman_num += syb[i]
            decimal_number -= val[i]
        i += 1
    return roman_num

r = romanize(1000)
print(r)