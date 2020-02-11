import re


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    result = 0
    input_numbers = re.findall('[+-]?\d+', calculation)
    try:
        if ' + ' in calculation:
            result = int(input_numbers[0]) + int(input_numbers[1])
        elif ' - ' in calculation:
            result = int(input_numbers[0]) - int(input_numbers[1])
        elif ' * ' in calculation:
            result = int(input_numbers[0]) * int(input_numbers[1])
        elif ' / ' in calculation:
            try:
                result = round(int(input_numbers[0]) / int(input_numbers[1]), 2)
            except:
                raise ValueError
        else:
            raise ValueError
    except IndexError:
        raise ValueError

    return result

c = simple_calculator('1 / 0')
print(c)