cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    s = ', '
    s = s.join(cars.get('Jeep'))
    return s


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_list = []
    for first in list(cars.keys()):
        f = cars.get(first)[0]
        first_list.append(f)
    return first_list


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    all_cars_list = []
    for i in list(cars.keys()):
        f = cars.get(i)
        for c in f:
            if grep.lower() in c.lower():
                all_cars_list.append(c)
    all_cars_list.sort()
    return all_cars_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_dict = {}
    for key in sorted(cars.keys()):
        sorted_dict[key] = sorted(cars.get(key))
    return sorted_dict