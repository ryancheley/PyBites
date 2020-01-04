import json
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'
MOVIES = os.path.join(TMP, DATA)
if not os.path.isfile(MOVIES):
    urlretrieve(os.path.join(S3, DATA), MOVIES)

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    result = []
    with open(files, 'r') as file:
        for line in file:
            result.append(line.split())
    return result

m = get_movie_data(MOVIES)
print(m[0])


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    pass


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    pass


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    pass