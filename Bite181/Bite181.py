import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        return bisect.insort_left(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)

order = OrderedList()
order.add(10)
print(order)  # __str__ already provided
order.add(1)
print(order)
order.add(16)
print(order)
order.add(5)
print(order)