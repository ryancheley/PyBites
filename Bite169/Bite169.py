def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    try:
        type(value) == 'int' or type(value) == 'float'
        if fmt == 'in':
            result = value / 2.54
        elif fmt == 'cm':
            result = value * 2.54
        else:
            err = f"Only 'in' or 'cm' are accepted. You entred {fmt} which is not valid!"
            raise ValueError(err)
        return float("{0:.4f}".format(result))
    except TypeError:
        err = f"The value of 'value' must be a number. You entered '{value}' which is not. Please try again."
        raise TypeError(err)


c = convert('153.67', 'in')
print(c)
