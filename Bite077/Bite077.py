my_cities = ['Rome', 'Paris', 'Madrid']
other_cities = ['Chicago', 'Seville', 'Berlin']

def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my_result = [m for m in my_cities if m not in other_cities]
    other_result = [o for o in other_cities if o not in my_cities]
    result = my_result + other_result
    return len(result)



t = uncommon_cities(my_cities, other_cities)
print(t)