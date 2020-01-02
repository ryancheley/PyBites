

def sum_numbers(numbers=None):
    i, j = 0, 0
    if numbers is None:
        for i in range(1, 101):
            j = j + i
    else:
        for i in numbers:
            j = j + i
    return j


t = sum_numbers(range(1, 11))
u = sum_numbers([1, 2, 3])
v = sum_numbers((1, 2, 3))
w = sum_numbers([])
x = sum_numbers()
y = sum_numbers(None)

print(t, u, v, w, x, y)