# when denominator is 0 catch the corresponding exception and return 0.
# when numerator or denominator are not of the right type reraise the corresponding exception.
# if the result of the division (after surviving the exceptions) is negative, raise a ValueError


def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError

    if result < 0:
        raise ValueError
    else:
        return result



p = positive_divide(1, 0)
print(p)