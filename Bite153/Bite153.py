from math import floor, ceil

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        result = [ceil(t) for t in transactions]
    else:
        result = [floor(t) for t in transactions]

    return result


t1 = round_up_or_down(transactions1, True)
t2 = round_up_or_down(transactions2, False)

print(t1)
print(t2)