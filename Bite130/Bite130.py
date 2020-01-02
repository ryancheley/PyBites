from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    models = []
    for d in data:
        if d.get('year') == year:
            models.append(d.get('automaker'))
    most_common = Counter(models).most_common()[0][0]
    return most_common


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = set()
    for d in data:
        if d.get('year') == year and d.get('automaker') == automaker:
            models.add(d.get('model'))
    return models



g = get_models('Mercedes-Benz', 2007)
print(g)