def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    n, d, value = None, None, None
    try:
        n = int(numerator)
        try:
            d = int(denominator)
            try:
                value = n / d
            except ZeroDivisionError as err:
                return 0
                raise err
        except ValueError as err:
            raise err
    except ValueError as err:
        raise err
    if value is not None:
        return value

t = divide_numbers(2, 0)

print(t)