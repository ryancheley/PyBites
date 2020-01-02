import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    data_points =[]
    result = defaultdict(list)
    with open(MOVIE_DATA, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                year = int(row['title_year'])
            except ValueError:
                pass
            data_points.append(
                (row['director_name'],
                Movie(
                    title=row['movie_title'],
                    year=year,
                    score=float(row['imdb_score']))
                 )
            )
    for k, v in data_points:
        if v.year >= MIN_YEAR:
            result[k].append(v)
    return result

director_movies = get_movies_by_director()

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    director_mean_score_list = []
    for m in movies:
        director_mean_score_list.append(m.score)
    result = mean(director_mean_score_list)
    result = round(result, 1)
    return result
    # return movies


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    result = []
    for d in directors:
        if len(directors[d]) >= MIN_MOVIES:
            result.append((d, calc_mean_score(directors[d])))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result

gas = get_average_scores(director_movies)
print(gas[0:9])