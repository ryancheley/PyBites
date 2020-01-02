inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )

# return {x: bites[x] for x in bites if x not in bites_done}

def get_index_different_char(chars):
    alphanumeric_filter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alphanumeric = [c for c in chars if str(c) in alphanumeric_filter and str(c)]
    nonalphanumeric = [c for c in chars if str(c) not in alphanumeric_filter and str(c)]
    if len(alphanumeric) == 1:
        result = chars.index(alphanumeric[0])
    else:
        result = chars.index(nonalphanumeric[0])
    return result


# [2, 4, 1, 5, 8, 0]
t = get_index_different_char(inputs[3])
print(t)