numbers = [0, -1, -3, -5]

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    filtered_list = [i for i in numbers if i % 2 == 0 and i > 0]

    return filtered_list

t = filter_positive_even_numbers(numbers)

print(t)