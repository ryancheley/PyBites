def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    mod_string_1 = string[n:]
    mod_string_2 = string[:n]

    return mod_string_1+mod_string_2


t = rotate('bob and julian love pybites!', 15)

print(t)